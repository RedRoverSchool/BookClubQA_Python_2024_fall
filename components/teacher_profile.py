import allure
from playwright.sync_api import Page, expect


class TeacherProfile:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Кликаем на кнопку 'Выйти'")
    def click_teacher_logout_button(self):
        self.page.locator("a", has_text="Выйти").click()

