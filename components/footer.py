import allure
from playwright.sync_api import Page, expect

from core.settings import base_url, policy_url, list_url, signup_url, login_url


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
    def click_privacy_policy_url(self):
        try:
            self.page.get_by_role("link", name="Политика конфиденциальности").click()
        except TimeoutError:
            raise AssertionError("URL 'Политика конфиденциальности' not found")

    @allure.step("Ждем завершения навигации")
    def wait_for_navigation(self):
        self.page.wait_for_url(policy_url)

    @allure.step("Проверяем видимость url 'Политика конфиденциальности'")
    def privacy_policy_url_should_be_visible(self):
        expect(self.page.get_by_role("link", name="Политика конфиденциальности")).to_be_visible()

    @allure.step("Проверяем доступность url 'Политика конфиденциальности'")
    def privacy_policy_url_should_be_enabled(self):
        expect(self.page.get_by_role("link", name="Политика конфиденциальности")).to_be_enabled()

    @allure.step("Проверяем успешность перехода на страницу 'Политика Конфиденциальности'")
    def verify_privacy_policy_page(self):
        try:
            expect(self.page).to_have_url("http://testing.misleplav.ru/policy/")
            title = "Политика конфиденциальности"
            expect(self.page.get_by_role("heading", name="Политика конфиденциальности")).to_contain_text(title)
        except Exception as e:
            print(f"Ошибка проверки страницы: {e}")
            raise
