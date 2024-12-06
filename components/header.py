from playwright.sync_api import Page, expect
from core.settings import base_url
import allure


class Header:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открываем Хэдер на главной странице")
    def visit(self):
        self.page.goto(base_url)

    @allure.step("Кликаем на кнопку 'Войти'")
    def click_on_login_button(self):
        self.page.locator('(//a[@class="btn btn-outline-light mb-2 me-2 ms-3"])[1]').click()

    @allure.step("Кликаем на кнопку 'Регистрация'")
    def click_on_registration_button(self):
        self.page.get_by_test_id("signup").click()

    @allure.step("Проверяем видимость кнопки 'Создать объявление'")
    def create_listing_button_should_be_visible(self):
        expect(self.page.get_by_test_id("create-listing")).to_be_visible()

    @allure.step("Кликаем на кнопку 'Найти репетитора'")
    def click_on_find_tutor_button(self):
        self.page.locator("//li/a[@href = '/list/']").click()