import allure
from playwright.sync_api import Page, expect

from core.settings import my_student_url


class MyStudentsPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открываем страницу 'Мои студенты'")
    def visit(self):
        self.page.goto(my_student_url)

    @allure.step("Проверяем наличие стандартного текста при отсутствии студентов")
    def check_no_students_message(self):
        no_students_message = self.page.locator('text="У вас пока нет студентов."')
        expect(no_students_message).to_be_visible()
