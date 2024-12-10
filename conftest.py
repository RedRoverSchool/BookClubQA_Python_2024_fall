import os


import allure
import pytest
from pytest import Item
from components.find_tutor import FindTutor
from components.header import Header
from components.login import Login
from playwright.sync_api import Page, sync_playwright
from components.footer import Footer


from components.main_body import MainBodyPage
from components.register import Register


@pytest.fixture
def header(page: Page):
    return Header(page)


@pytest.fixture
def register(page: Page):
    return Register(page)


@pytest.fixture
def main_body(page: Page):
    return MainBodyPage(page)


@pytest.fixture
def login(page: Page):
    return Login(page)


@pytest.fixture
def find_tutor(page: Page):
    return FindTutor(page)


@pytest.fixture
def footer(page: Page):
    return Footer(page)


# дубль -удалить 25 строка
# @pytest.fixture
# def main_body(page: Page):
#     return MainBodyPage(page)


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
