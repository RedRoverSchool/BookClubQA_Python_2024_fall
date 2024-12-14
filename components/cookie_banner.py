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
            accept_cookie_banner = self.page.wait_for_selector('#cookie-consent-banner', timeout=5000)
            assert accept_cookie_banner.is_visible(), "Cookie banner is not visible!"
            return True
        except TimeoutError:
            raise AssertionError("Cookie banner not found within 5 seconds")

    @allure.step("Проверяем видимость кнопки 'Согласиться'")
    def cookie_button_should_be_visible(self):
        try:
            accept_button = self.page.wait_for_selector('#accept-cookies', timeout=5000)
            assert accept_button.is_visible(), "Accept button is not visible!"
            return True
        except TimeoutError:
            raise AssertionError("Cookie banner not found within 5 seconds")

    @allure.step("Проверяем активность кнопки 'Согласиться'")
    def cookie_button_should_be_enable(self):
        try:
            enable_button = self.page.wait_for_selector('#accept-cookies', timeout=5000)
            assert enable_button.is_enabled(), "Accept button is not enabled!"
            return True
        except TimeoutError:
            raise AssertionError("Cookie banner not found within 5 seconds")

    @allure.step("Проверяем контекст сообщения о согласии использования куки")
    def cookie_text_matches(self):
        try:
            cookie_text = self.page.wait_for_selector('#cookie-consent-banner p.mb-2', timeout=5000)
            actual_text = cookie_text.text_content()
            expected_text = "Мы используем куки для улучшения вашего опыта на нашем сайте."
            assert (actual_text == expected_text), f"Ожидается '{expected_text}', но получен '{actual_text}'"
            return True
        except TimeoutError:
            raise AssertionError("Cookie banner not found within 5 seconds")

    @allure.step("Нажимаем на кнопку 'Согласиться'")
    def click_accept_button(self):
        try:
            accept_button = self.page.wait_for_selector('#accept-cookies', timeout=5000)
            accept_button.click()
        except TimeoutError:
            raise AssertionError("Cookie banner not found within 5 seconds")

    @allure.step("Проверяем что сообщения больше не отображается после нажатия кнопки 'Согласиться'")
    def cookie_banner_is_missing(self):
        try:
            self.page.wait_for_selector('#cookie-consent-banner', state='hidden', timeout=5000)
        except TimeoutError:
            raise AssertionError("Cookie banner did not disappear as expected")

    @allure.step("Проверяем, что сообщение не появляется при повторном запуске приложения ")
    def banner_does_not_reappear(self):
        self.page.reload()
        try:
            self.page.wait_for_selector('#cookie-consent-banner', state='hidden', timeout=5000)
        except TimeoutError:
            raise AssertionError("Cookie banner reappeared after reopening the app")

