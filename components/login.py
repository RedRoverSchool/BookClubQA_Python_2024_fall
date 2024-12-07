from playwright.sync_api import Page, expect
from core.settings import base_url
import allure


class Login:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Проверяем URL страницы 'Логин'")
    def check_url_login_page(self, expected_part: str):
        current_url = self.page.url
        assert expected_part in current_url, f"Ожидалось, что '{expected_part}' будет частью '{current_url}'"