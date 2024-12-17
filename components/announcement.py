import allure
from playwright.sync_api import Page, expect


class Announcement:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Заполняем Ф.И.О")
    def fill_out_fullname(self):
        self.page.fill('input[name="name"]', "Jon Snow")

    @allure.step('Заполняем поле "Опишите себя"')
    def fill_out_descripption(self):
        self.page.fill(
            'trix-editor[input="id_description"]', "Teacher, that knows everything"
        )

    @allure.step("Загружаем фото")
    def upload_photo(self):
        self.page.locator('input[name="photo"]').set_input_files(
            "Data/upload_files/stock-photo-handsome-cheerful-man.jfif"
        )

    @allure.step("Выбираем категорию")
    def pick_category(self):
        dropdown = self.page.locator("#id_category")
        dropdown.select_option(value="1")
        selected_value = dropdown.input_value()
        assert selected_value == "1", "The category 'Математика' should be selected"

    @allure.step("Указываем опыт")
    def fill_out_experience(self):
        years_of_experience_input = self.page.locator("#id_years_of_experience")
        years_of_experience_input.fill("5")
        filled_value = years_of_experience_input.input_value()
        assert filled_value == "5", "The years of experience should be 5"

    @allure.step("Есть профильное образование")
    def checkbox_degree(self):
        degree_checkbox = self.page.locator("#id_has_degree")
        degree_checkbox.check()
        assert (
            degree_checkbox.is_checked()
        ), "The 'has degree' checkbox should be checked"

    @allure.step("Бесплатное первое занятие")
    def checkbox_free_first_lesson(self):
        free_first_lesson_checkbox = self.page.locator("#id_free_first_lesson")
        free_first_lesson_checkbox.check()
        assert (
            free_first_lesson_checkbox.is_checked()
        ), "The 'free first lesson' checkbox should be checked"

    @allure.step("Вводим стоимость занятия")
    def fill_out_price(self):
        price_input = self.page.locator("#id_price")
        price_input.fill("1000")
        filled_value = price_input.input_value()
        assert filled_value == "1000", "The price should be 1000"

    @allure.step("Длительность занятия")
    def fill_out_class_duration(self):
        class_duration_input = self.page.locator("#id_class_duration")
        class_duration_input.fill("60")
        filled_value = class_duration_input.input_value()
        assert filled_value == "60", "The class duration should be 60 minutes"

    @allure.step("Добавляем контактную информацию")
    def add_contact_info(self):
        add_contact_button = self.page.locator("#addContactBtn")
        add_contact_button.click()
        contact_detail_input = self.page.locator("input.form-control.contact-detail")
        contact_detail_input.fill("5555555555")
        filled_value = contact_detail_input.input_value()
        assert filled_value == "5555555555", "Phone number should be 5555555555"

    @allure.step('Нажимаем на кнопку "Создать объявление"')
    def click_create_announcement_btn(self):  # click_create_announcement_btn
        create_button = self.page.locator('button.btn.btn-dark.me-2[type="submit"]')
        create_button.click()
        assert (
            self.page.url
            == "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/listings/list/"
        )

    @allure.step("Пройти на страницу объявлений пользователя-учителя")
    def navigate_to_users_announcement_list(self):
        announcement_list_url = "http://testing.misleplav.ru/listings/my_listing/"
        self.page.goto(announcement_list_url)

    @allure.step("Убедиться, что количество объявлений пользователя-учителя равно нулю")
    def verify_number_of_announcements_is_zero(self):
        announcement_list = self.page.locator("main .container h5")
        expect(announcement_list).to_have_count(0)

    @allure.step("Убедиться, что пользователь на странице объявлений")
    def verify_announcements_page_endpoint(self):
        announcement_page_endpoint = "/listings/list/"
        current_url = self.page.url
        print(current_url)
        assert announcement_page_endpoint in current_url
