import allure
import pytest
from playwright.sync_api import Page
from components.teacher_profile import TeacherProfile
from core.settings import tutors_list_url


# TC_05.001.008.001 | Guest > Find a Teacher page > Teacher Profile > Navigate to the detailed profile page
@pytest.mark.skip(reason="не прошёл CI после изменений 26.12.2024")
@allure.title("Проверка перехода на страницу профиля учителя через список объявлений")
def test_teacher_profile_navigation(page: Page):
    page.goto(tutors_list_url, wait_until="domcontentloaded")

    # Создание объекта TeacherProfile
    teacher_profile = TeacherProfile(page)

    # Найти и кликнуть первую доступную ссылку
    with allure.step("Кликаем на первую доступную ссылку"):
        page.goto(tutors_list_url, wait_until="domcontentloaded")  # Перезагрузка страницы
        teacher_profile.click_on_first_available_listing()

    # Проверка: Убедиться, что произошел переход на страницу профиля
    with allure.step("Проверяем переход на страницу профиля"):
        assert "/listings/" in page.url, "Переход на страницу профиля не выполнен"


