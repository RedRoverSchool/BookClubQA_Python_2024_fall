import allure
from playwright.sync_api import Page, expect
from Data import data
from Data import constants


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
                self.page.locator("#id_username").get_attribute(
                    "placeholder") == constants.REGISTER_USERNAME_PLACEHOLDER_TEXT
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
                self.page.locator("#id_password1").get_attribute(
                    "placeholder") == constants.REGISTER_PASSWORD1_PLACEHOLDER_TEXT
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
                self.page.locator("#id_password2").get_attribute(
                    "placeholder") == constants.REGISTER_PASSWORD2_PLACEHOLDER_TEXT
        ), "Incorrect placeholder text in the 'password2' field"
