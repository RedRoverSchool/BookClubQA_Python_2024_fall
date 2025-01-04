import allure
from playwright.sync_api import Page
from core.settings import base_url


class CookieBanner:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открываем главную страницу")
    def open_main_page(self):
        self.page.goto(base_url)

    @allure.step("Проверяем видимость сообщения о принятии куки")
    def cookie_banner_should_be_visible(self):
        try:
            accept_cookie_banner = self.page.wait_for_selector(
                "#cookie-consent-banner", timeout=10000
            )
            assert accept_cookie_banner.is_visible(), "Cookie banner is not visible!"
            return True
        except TimeoutError:
            raise AssertionError("Cookie banner not found within 5 seconds")

    @allure.step("Проверяем видимость кнопки 'Согласиться'")
    def cookie_button_should_be_visible(self):
        try:
            accept_button = self.page.wait_for_selector(
                "#cookie-consent-banner", state="hidden", timeout=5000
            )
        except TimeoutError:
            raise AssertionError("Cookie banner reappeared after reopening the app")
