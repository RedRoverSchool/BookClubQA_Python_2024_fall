import allure
from playwright.sync_api import Page
from core.settings import login_url
from dotenv import load_dotenv
import os

load_dotenv()


class Login:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Проверяем URL страницы 'Логин'")
    def check_url_login_page(self, expected_part: str):
        current_url = self.page.url
        assert (
            expected_part in current_url
        ), f"Ожидалось, что '{expected_part}' будет частью '{current_url}'"

    @allure.step("Проверяем наличие кнопки 'Регистрация'")
    def check_title_of_registration(self):
        title = self.page.get_by_title("Регистрация")
        assert "Регистрация", title

    def open_login_page(self):
        self.page.goto(login_url)

    @allure.step("Вводим логин пользователя")
    def enter_username(self, username: str):
        username_field = self.page.locator("#id_username")
        username_field.fill(username)

    @allure.step("Вводим пароль пользователя")
    def enter_password(self, password: str):
        password_field = self.page.locator("#id_password")
        password_field.fill(password)

    @allure.step("Нажимаем кнопку 'Войти'")
    def click_login_button(self):
        self.page.get_by_text("Войти").click()

    @allure.step("Выполняем полный вход пользователя")
    def full_login(self, username: str, password: str):
        """
        Выполняет полный процесс входа на сайт.
        :param username: Логин пользователя.
        :param password: Пароль пользователя.
        """
        self.click_login_button()
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit_button()

    @allure.step("Выполняем вход с не корректным логином")
    def check_enter_invalid_username(self, username):
        self.enter_username(username)

    def should_be_valid_message(self, expected_text):
        expected_messege_field = self.page.locator(
            "//*[contains(text(), 'Пожалуйста,')]"
        )
        actual_text = expected_messege_field.text_content()
        assert (
            expected_messege_field.is_visible()
        ), "Сообщение с текстом 'Пожалуйста' не найдено"
        assert expected_text == actual_text

    def click_submit_button(self):
        self.page.locator("//*[@type='submit']").click()

    @allure.step("Логинимся как учитель с персональными данными")
    def login_as_tutor(self, header):
        header.visit()
        header.click_login_button()
        try:
            email = os.getenv("EMAIL_TUTOR")
            password = os.getenv("PASSWORD_TUTOR")
            print(f"Email: {email}")
            print(f"Password: {password}")
            email_field = self.page.locator('input[name="username"]')
            email_field.fill(email)
            password_input = self.page.locator('input[name="password"]')
            password_input.fill(password)
            submit_button = self.page.locator('button:has-text("Войти")')
            submit_button.click()
            print("Login successful!")
        except Exception as e:
            print(f"An error occurred: {e}")
