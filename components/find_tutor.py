import allure
from playwright.sync_api import Page


class FindTutor:

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Проверяем наличие кнопки 'Регистрация'")
    def check_title_of_registration(self):
        title = self.page.get_by_title("Регистрация")
        assert "Регистрация", title
