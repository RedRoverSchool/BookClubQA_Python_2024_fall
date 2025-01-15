import os
import allure
import pytest
import logging

from faker import Faker
from playwright.sync_api import Page, sync_playwright
from pytest import Item

from components.announcement import Announcement
from components.cookie_banner import CookieBanner
from components.create_announcement import CreateAnnouncement
from components.find_tutor import FindTutor
from components.footer import Footer
from components.header import Header
from components.homepage import Homepage
from components.login import Login
from components.my_teachers import MyTeachersPage
from components.register import Register
from components.teacher_profile import TeacherProfile
from components.telegram_page import TelegramPage
from components.user_profile import UserProfile
from api_clients.user_api import ApiClient
from Data.constants import AUTH_CREDENTIALS, BASE_URL
from Data.data import UserFactory
from models.user_model import RegisterRequest

fake = Faker()
logger = logging.getLogger(__name__)


@pytest.fixture
def header(page: Page):
    return Header(page)


@pytest.fixture
def my_teachers(page: Page):
    return MyTeachersPage(page)


@pytest.fixture
def teacher_profile(page: Page):
    return TeacherProfile(page)


@pytest.fixture
def register(page: Page):
    return Register(page)


@pytest.fixture
def homepage(page: Page):
    return Homepage(page)


@pytest.fixture
def login(page: Page):
    return Login(page)


@pytest.fixture
def find_tutor(page: Page):
    return FindTutor(page)


@pytest.fixture
def footer(page: Page):
    return Footer(page)


@pytest.fixture
def telegram_page(page: Page):
    return TelegramPage(page)


@pytest.fixture
def user_profile(page: Page):
    return UserProfile(page)


@pytest.fixture(scope="function", autouse=True)
def video_and_screenshot(page: Page):
    yield  # здесь выполняется тест

    # Сохранить скриншот
    screenshot = page.screenshot()
    allure.attach(
        screenshot,
        name="screenshot",
        attachment_type=allure.attachment_type.PNG,
    )

    # Сохранить видео
    video = page.video.path()
    page.context.close()  # Закрыть контекст, чтобы видео сохранилось на диск
    allure.attach.file(
        video,
        name="video",
        attachment_type=allure.attachment_type.WEBM,
    )


@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_runtest_call(item: Item):
    yield
    allure.dynamic.title(" ".join(item.name.split("_")[1:]).title())


@pytest.fixture
def browser_context():
    with sync_playwright() as p:
        # Запускаем Chromium
        browser = p.chromium.launch(
            headless=os.environ.get(
                "CI_RUN", False
            ),  # Запуск в headless режиме, если это CI/CD
            args=[
                "--start-maximized",  # Максимизация окна
                "--no-sandbox",
                "--disable-dev-shm-usage",
            ]
            if os.environ.get("CI_RUN")
            else [],
        )
        context = (
            browser.new_context()
        )  # Создаем контекст браузера без изменения размера окна
        yield context
        context.close()
        browser.close()


@pytest.fixture(autouse=True, scope="session")
def set_root_dir():
    ci_root_dir = os.environ.get("GITHUB_WORKSPACE", False)
    os.environ["ROOT_DIR"] = ci_root_dir or ".."


@pytest.fixture
def cookie_banner(page: Page):
    return CookieBanner(page)


@pytest.fixture
def announcement(page: Page):
    return Announcement(page)


@pytest.fixture
def create_announcement_page(page: Page):
    return CreateAnnouncement(page)


@pytest.fixture()
def api_request(page: Page):
    return ApiClient(page, base_url=BASE_URL, auth_credentials=AUTH_CREDENTIALS)


@pytest.fixture()
def create_user_data():
    return UserFactory.generate_user()


@pytest.fixture()
def status_user():
    return RegisterRequest


@pytest.fixture(scope="function")
def user_registration_cleanup(request, api_request):
    role, is_premium, is_writer = request.param
    # Генерация данных пользователя с заданной ролью и статусами
    user_data = UserFactory.generate_user(
        role=role, is_premium=is_premium, is_writer=is_writer
    )
    # Регистрация пользователя перед тестом
    api_request.post("/api/users/", user_data.model_dump())
    logger.info(f"User registered: Email - {user_data.email}")
    # Передача данных пользователя в тест
    yield user_data.email, user_data.password
    # Удаление пользователя после завершения теста
    api_request.delete(endpoint="/api/users/", email=user_data.email)
    logger.info(f"User deleted: Email - {user_data.email}")
