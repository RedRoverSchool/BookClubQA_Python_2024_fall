import allure
from playwright.sync_api import Page, expect
from Data import data
from Data import constants
from faker import Faker
from dotenv import load_dotenv
import os
load_dotenv()
fake = Faker()


class Register:
    def __init__(self, page: Page):
        self.password = None
        self.page = page

    @allure.step("Проверяем заголовок 'Регистрация'")
    def header_should_contain_text(self, title_text):
        expect(self.page.get_by_role("link", name=" Регистрация")).to_contain_text(
            title_text
        )

    @allure.step("Заполняем поле 'Почта'")
    def fill_email(self, email):
        self.page.locator("#id_email").fill(email)

    @allure.step("Заполняем поле 'Имя'")
    def fill_nick(self, name):
        self.page.locator("#id_first_name").fill(name)

    @allure.step("Заполняем поле 'Пароль'")
    def fill_password(self, password):
        self.page.locator("#id_password1").fill(password)

    @allure.step("Заполняем поле 'Подтверждение пароля'")
    def fill_confirm_password(self, password):
        self.page.locator("#id_password2").fill(password)

    @allure.step("Включаем флаг 'Я преподаватель'")
    def check_become_a_teacher_checkbox(self):
        self.page.locator("#id_is_tutor").check()

    @allure.step("Кликаем на кнопку 'Зарегистрироваться'")
    def click_registration_button(self):
        self.page.locator("button", has_text="Зарегистрироваться").click()

    @allure.step("Проверяем, что страница регистрации открыта")
    def verify_registration_page_opened(self):
        registration_title = self.page.locator("h1").inner_text()
        assert (
            registration_title == "Регистрация"
        ), f"Ожидался заголовок 'Регистрация', но найдено: {registration_title}"

    @allure.step("Создаем случайный пароль")
    def generate_valid_password(self):
        self.password = data.generate_valid_password()

    @allure.step("Проверяем, что плейсхолдер виден в поле 'username'")
    def check_username_placeholder_visibility(self):
        is_placeholder_visible = self.page.locator("#id_username").evaluate("""
                (el) => {
                    const placeholderStyle = window.getComputedStyle(el, '::placeholder');
                    return placeholderStyle && placeholderStyle.visibility !== 'hidden' && placeholderStyle.opacity > 0;
                }
            """)
        assert is_placeholder_visible, "The placeholder for 'username' is not visible"

    @allure.step("Проверяем текст плейсхолдера в поле 'username'")
    def check_username_placeholder_text(self):
        assert (
            self.page.locator("#id_username").get_attribute("placeholder")
            == constants.REGISTER_USERNAME_PLACEHOLDER_TEXT
        ), "Incorrect placeholder text in the 'username' field"

    @allure.step("Проверяем, что плейсхолдер виден в поле 'password1'")
    def check_password1_placeholder_visibility(self):
        is_placeholder_visible = self.page.locator("#id_password1").evaluate("""
                    (el) => {
                        const placeholderStyle = window.getComputedStyle(el, '::placeholder');
                        return placeholderStyle && placeholderStyle.visibility !== 'hidden' && placeholderStyle.opacity > 0;
                    }
                """)
        assert is_placeholder_visible, "The placeholder for 'password1' is not visible"

    @allure.step("Проверяем текст плейсхолдера в поле 'password1'")
    def check_password1_placeholder_text(self):
        assert (
            self.page.locator("#id_password1").get_attribute("placeholder")
            == constants.REGISTER_PASSWORD1_PLACEHOLDER_TEXT
        ), "Incorrect placeholder text in the 'password1' field"

    @allure.step("Проверяем, что плейсхолдер виден в поле 'password2'")
    def check_password2_placeholder_visibility(self):
        is_placeholder_visible = self.page.locator("#id_password2").evaluate("""
                        (el) => {
                            const placeholderStyle = window.getComputedStyle(el, '::placeholder');
                            return placeholderStyle && placeholderStyle.visibility !== 'hidden' && placeholderStyle.opacity > 0;
                        }
                    """)
        assert is_placeholder_visible, "The placeholder for 'password2' is not visible"

    @allure.step("Проверяем текст плейсхолдера в поле 'password2'")
    def check_password2_placeholder_text(self):
        assert (
            self.page.locator("#id_password2").get_attribute("placeholder")
            == constants.REGISTER_PASSWORD2_PLACEHOLDER_TEXT
        ), "Incorrect placeholder text in the 'password2' field"

    @allure.step("Регистрируем преподавателя")
    def registration_as_tutor(self, header, register):
        header.visit()
        header.click_registration_button()
        register.header_should_contain_text("Регистрация")
        register.fill_email(fake.email())
        register.fill_nick(fake.user_name())
        register.fill_password("sdjflsfdjlksdjflksdjf")
        register.fill_confirm_password("sdjflsfdjlksdjflksdjf")
        register.check_become_a_teacher_checkbox()
        register.click_registration_button()
        header.create_listing_button_should_be_visible()

    @allure.step("Регистрируем пользователя с генерацией данных")
    def registration_new_user(self, user_type):
        if user_type == "tutor":
            self.check_become_a_teacher_checkbox()
        if user_type not in ["tutor", "student"]:
            assert False, "Wrong user type"
        name = fake.user_name()
        email = fake.email()

        self.generate_valid_password()
        self.fill_email(email)
        self.fill_password(self.password)
        self.fill_confirm_password(self.password)
        self.click_registration_button()
        return {"name": name, "password": self.password, "email": email}

    @allure.step("Логинимся как учитель с персональными данными")
    def login_as_tutor(self, header):
        header.visit()
        header.click_login_button()
        try:
            email = os.getenv("EMAIL")
            password = os.getenv("PASSWORD")
            print(f"Email: {email}")
            print(f"Password: {password}")
            email_field = self.page.locator('input[name="username"]')
            email_field.fill(email)
            password_input = self.page.locator('input[name="password"]')
            password_input.fill(password)
            submit_button = self.page.locator('button:has-text("Войти")')
            submit_button.click()
            print("Login successful!")
        except Exception as e: print(f"An error occurred: {e}")