import allure
from playwright.sync_api import Page, expect
from Data import data
from faker import Faker

fake = Faker()


class Register:
    def __init__(self, page: Page):
        self.password = None
        self.page = page

    @allure.step("Проверяем заголовок 'Регистрация'")
    def header_should_contain_text(self, title_text):
        expect(self.page.get_by_test_id("registration-header")).to_contain_text(
            title_text
        )

    @allure.step("Заполняем поле 'Придумайте ник'")
    def fill_nick(self, nick):
        self.page.get_by_placeholder("Придумайте ник").fill(nick)

    @allure.step("Заполняем поле 'Придумайте пароль'")
    def fill_password(self, password):
        self.page.get_by_placeholder("Придумайте пароль").fill(password)

    @allure.step("Заполняем поле 'Подтвердите пароль'")
    def fill_confirm_password(self, password):
        self.page.get_by_placeholder("Подтвердите пароль").fill(password)

    @allure.step("Кликаем на кнопку 'Я преподаватель'")
    def click_on_become_a_teacher_button(self):
        self.page.locator("#id_is_tutor").check()

    @allure.step("Кликаем на кнопку 'Зарегистрироваться'")
    def click_on_registration_button(self):
        self.page.get_by_test_id("submit-button").click()

    @allure.step("Проверяем, что страница регистрации открыта")
    def verify_registration_page_opened(self):
        registration_title = self.page.locator("h1").inner_text()
        assert (
            registration_title == "Регистрация"
        ), f"Ожидался заголовок 'Регистрация', но найдено: {registration_title}"

    @allure.step("Создаем случайный пароль")
    def generate_valid_password(self):
        self.password = data.generate_valid_password()

    @allure.step('Регистрируем преподавателя')
    def registration_as_tutor(self, header, register):
        header.visit()
        header.click_on_registration_button()
        register.header_should_contain_text("Регистрация")
        register.fill_nick(fake.user_name())
        register.fill_password("sdjflsfdjlksdjflksdjf")
        register.fill_confirm_password("sdjflsfdjlksdjflksdjf")
        register.click_on_become_a_teacher_button()
        register.click_on_registration_button()
        header.create_listing_button_should_be_visible()

    @allure.step('Регистрируемcя как студент')
    def registration_as_student(self):
        self.verify_registration_page_opened()
        self.fill_nick(fake.user_name())
        self.generate_valid_password()
        self.fill_password(self.password)
        self.fill_confirm_password(self.password)
        self.click_on_registration_button()
