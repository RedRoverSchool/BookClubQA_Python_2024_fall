import allure
from playwright.sync_api import Page, expect

from core.settings import base_url, policy_url, list_url, signup_url, login_url, title


class Footer:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открываем Footer на главной странице")
    def open_main_page(self):
        self.page.goto(base_url)

    @allure.step("Открываем Footer на странице Найти Репетитора")
    def open_find_tutor_page(self):
        self.page.goto(list_url)

    @allure.step("Открываем Footer на странице Регистрации")
    def open_signup_page(self):
        self.page.goto(signup_url)

    @allure.step("Открываем Footer на странице Входа")
    def open_login_page(self):
        self.page.goto(login_url)

    @allure.step("Прокручиваем страницу до Футера")
    def scroll_down_to_the_footer(self):
        self.page.get_by_text(
            "© 2024 Мыслеплав. Все права защищены."
        ).scroll_into_view_if_needed()

    @allure.step("Кликаем на название url 'Политика конфиденциальности'")
    def click_on_privacy_policy_url(self):
        self.page.get_by_text("Политика конфиденциальности").click()

    @allure.step("Ждем завершения навигации")
    def wait_for_navigation(self):
        self.page.wait_for_url(policy_url)

    @allure.step("Проверяем видимость url 'Политика конфиденциальности'")
    def privacy_policy_url_should_be_visible(self):
        expect(self.page.get_by_text("Политика конфиденциальности")).to_be_visible()

    @allure.step("Проверяем доступность url 'Политика конфиденциальности'")
    def privacy_policy_url_should_be_enabled(self):
        expect(self.page.get_by_text("Политика конфиденциальности")).to_be_enabled()

    @allure.step("Проверяем перенаправление на страницу 'Политика Конфиденциальности'")
    def privacy_policy_page_should_contain_text(self):
        expect(self.page.get_by_text("Example Domain")).to_contain_text(title)
