import allure
from playwright.sync_api import Page
from components.teacher_profile import TeacherProfile
from core.settings import tutors_list_url


@allure.title("TC_05.001.008.001 | Navigate to the detailed profile page")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/296")
def test_teacher_profile_navigation(page: Page):
    page.goto(tutors_list_url, wait_until="domcontentloaded")

    # Создание объекта TeacherProfile
    teacher_profile = TeacherProfile(page)

    # Найти и кликнуть первую доступную ссылку
    with allure.step("Кликаем на первую доступную ссылку"):
        page.goto(
            tutors_list_url, wait_until="domcontentloaded"
        )  # Перезагрузка страницы
        teacher_profile.click_on_first_available_listing()

    # Проверка: Убедиться, что произошел переход на страницу профиля
    with allure.step("Проверяем переход на страницу профиля"):
        assert "/listings/" in page.url, "Переход на страницу профиля не выполнен"
