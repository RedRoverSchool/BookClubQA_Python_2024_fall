import allure
from playwright.sync_api import Page, expect
from Data import data
from Data import constants
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
        self.page.locator('#id_first_name').fill(nick)

    @allure.step("Заполняем поле 'Придумайте пароль'")
    def fill_password(self, password):
        self.page.locator('#id_password1').fill(password)

    @allure.step("Заполняем поле 'Почта'")
    def fill_email(self, email):
        self.page.locator('#id_email').fill(email)

    @allure.step("Заполняем поле 'Подтвердите пароль'")
    def fill_confirm_password(self, password):
        self.page.locator("#id_password2").fill(password)

    @allure.step("Кликаем на кнопку 'Я преподаватель'")
    def click_on_become_a_teacher_button(self):
        self.page.locator("#id_is_tutor").check()

    @allure.step("Кликаем на кнопку 'Зарегистрироваться'")
    def click_on_registration_button(self):
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

    @allure.step('Регистрируем пользователя с генерацией данных')
    def registration_new_user(self, user_type):
        if user_type == 'tutor':
            self.click_on_become_a_teacher_button()
        if user_type not in ['tutor', 'student']:
            assert False, 'Wrong user type'
        name = fake.user_name()
        email = fake.email()

        self.generate_valid_password()
        self.fill_email(email)
        self.fill_nick(name)
        self.fill_password(self.password)
        self.fill_confirm_password(self.password)
        self.click_on_registration_button()
        print('133', email, self.password)
        return {'name': name, 'password': self.password, 'email': email}
