import os
import allure
from playwright.sync_api import Page, expect
from core.settings import list_url
from core.settings import edit_announcement_url
import re
import random


class Announcement:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Заполняем 'Ваше имя'")
    def fill_first_name(self, first_name):
        self.page.fill('input[name="first_name"]', first_name)

    @allure.step("Заполняем 'Ваша фамилия'")
    def fill_last_name(self, last_name):
        self.page.fill('input[name="last_name"]', last_name)

    @allure.step("Заполняем 'Telegram'")
    def fill_telegram(self, telegram_id):
        self.page.fill('input[name="telegram"]', telegram_id)

    @allure.step("Заполняем 'Телефон'")
    def fill_phone_number(self, phone_number):
        self.page.fill('input[name="phone"]', phone_number)

    @allure.step('Заполняем поле "Опишите себя"')
    def fill_out_description(self, description):
        self.page.fill("#id_description", description)

    @allure.step("Загружаем фото")
    def upload_photo(self):
        try:
            root_dir = os.environ.get("ROOT_DIR")
            photo_path = os.path.join(
                root_dir,
                "Data",
                "upload_files",
                "stock-photo-handsome-cheerful-man.jfif",
            )
            photo_field = self.page.locator("input#photoInput")
            photo_field.set_input_files(photo_path)
        except Exception as e:
            print(f"First upload error: {e}")
            try:
                self.page.locator("input#photoInput").set_input_files(
                    "Data/upload_files/stock-photo-handsome-cheerful-man.jfif"
                )
            except Exception as e:
                print(f"Second upload failed with error: {e}")

    @allure.step("Выберите возрастные категории учеников")
    def pick_student_age_category(self):
        age_category_elements = self.page.query_selector_all(
            '//div[@id="div_id_student_categories"]//input[@type="checkbox"]'
        )
        random_choice = random.choice(age_category_elements)
        random_choice.click()
        assert random_choice.is_checked()

    @allure.step("Выбираем категорию")
    def pick_category(self, category):
        dropdown = self.page.locator("#id_category")
        dropdown.select_option(value=category)
        selected_value = dropdown.input_value()
        if category == 1:
            assert selected_value == "1", "The category 'Математика' should be selected"

    @allure.step("Указываем опыт")
    def fill_out_experience(self, years_experience):
        years_of_experience_input = self.page.locator("#id_years_of_experience")
        years_of_experience_input.fill(years_experience)
        filled_value = years_of_experience_input.input_value()
        if years_experience == 5:
            assert filled_value == "5", "The years of experience should be 5"

    @allure.step("Есть профильное образование")
    def checkbox_degree(self):
        degree_checkbox = self.page.locator("#id_has_degree")
        degree_checkbox.check()
        assert degree_checkbox.is_checked(), (
            "The 'has degree' checkbox should be checked"
        )

    @allure.step("Вводим стоимость занятия")
    def fill_out_price(self, price):
        price_input = self.page.locator("#id_price")
        price_input.fill(price)
        filled_value = price_input.input_value()
        if price == "1000":
            assert filled_value == "1000", "The price should be 1000"

    @allure.step("Продолжительность занятия")
    def fill_out_class_duration(self, duration):
        class_duration_input = self.page.locator('input[name="class_duration"]')
        class_duration_input.fill(duration)
        filled_value = class_duration_input.input_value()
        if duration == "60":
            assert filled_value == "60", "The class duration should be 60 minutes"

    @allure.step("Отчищаем чекбоксы категорий учеников")
    def clear_student_category_checkboxes(self):
        checkboxes = self.page.locator(
            '//div[@id="div_id_student_categories"]//input[@type="checkbox"]'
        )
        count = checkboxes.count()
        for i in range(count):
            if checkboxes.nth(i).is_checked():
                checkboxes.nth(i).uncheck()

    @allure.step("С чем вы можете помочь")
    def fill_out_can_help_field(self, text):
        self.page.fill("#id_can_help", text)

    @allure.step("Расскажите о том как проходит урок")
    def fill_out_lesson_style(self, text):
        self.page.fill("#id_lesson_style", text)

    @allure.step('Нажимаем на кнопку "Сохранить"')
    def click_save_announcement_btn(self):
        self.page.locator('//button[@type="submit"]').click()

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
        try:
            assert announcement_page_endpoint in current_url, (
                f"Expected '{announcement_page_endpoint}' to be in '{current_url}'"
            )
        except AssertionError as e:
            (print(e))

    @allure.step("Кликаем на кнопку 'Мое объявление' в хедере")
    def click_my_announcement_button(self):
        self.page.locator("a", has_text="Мое объявление").click()
        expect(self.page).to_have_url(
            "http://testing.misleplav.ru/listings/my_listing/"
        )

    @allure.step("Кликаем на кнопку 'Сделать объявление видимым для учеников'")
    def click_make_announcement_invisible(self):
        self.page.get_by_role(
            "link", name="Сделать обьявление видимым для учеников"
        ).click()

    @allure.step(
        "Проверяем изменение текста кнопки на 'Сделать объявление невидимым для учеников'"
    )
    def check_button_text_invisible(self):
        expect(self.page.get_by_role("main")).to_contain_text(
            "Сделать обьявление невидимым для учеников"
        )

    @allure.step("Кликаем на кнопку 'Сделать объявление невидимым для учеников'")
    def click_make_announcement_visible(self):
        self.page.get_by_role(
            "link", name="Сделать обьявление невидимым для учеников"
        ).click()

    @allure.step(
        "Проверяем изменение текста кнопки на 'Сделать объявление невидимым для учеников'"
    )
    def check_button_text_visible(self):
        expect(self.page.get_by_role("main")).to_contain_text(
            "Сделать обьявление видимым для учеников"
        )

    @allure.step("Кликаем кнопку 'Редактировать объявление'")
    def click_edit_announcement_button(self):
        self.page.locator("a", has_text="Редактировать").click()

    @allure.step("Кликаем кнопку 'Просмотреть объявление'")
    def click_view_announcement_button(self):
        self.page.locator("a", has_text="Просмотреть").click()

    @allure.step("Проверяем URL страницы объявления по шаблону")
    def check_announcement_url_by_template(self):
        current_url = self.page.url
        pattern = r"^http://tester:dslfjsdfblkhew%40122b1klbfw@testing\.misleplav\.ru/listings/\d+/$"
        assert re.match(pattern, current_url), (
            f"URL не соответствует ожидаемому шаблону: {current_url}"
        )

    @allure.step("Проверяем URL страницы редактирования объявления")
    def check_edit_announcement_page_url(self):
        expect(self.page).to_have_url(edit_announcement_url)

    @allure.step("Проверяем видимость счетчика просмотров")
    def check_view_counter_visible(self):
        expect(self.page.locator("p.mt-4.text-center.text-secondary")).to_be_visible()

    @allure.step(
        "Проходим по всему списку обьявлений и проверяем, что карточки с именем учителя нет"
    )
    def check_teacher_announcement_invisible(self):
        self.page.get_by_role("link", name="Мое объявление").click()
        self.page.get_by_role("link", name="Редактировать").click()
        name_field = self.page.get_by_label("ФИО*")
        teacher_name = name_field.input_value()
        print("teacher_name", teacher_name)
        self.page.goto(list_url)

        current_page = 1
        teacher_found = False
        while True:
            allure.step(f"Проверяем страницу {current_page}")
            if self.page.get_by_text(teacher_name, exact=True).count() > 0:
                teacher_found = True
                break

            next_button = self.page.get_by_role("link", name="Вперед").first
            if not next_button.is_visible():
                break

            self.page.get_by_role("link", name="Вперед").click()
            self.page.wait_for_load_state("networkidle")
            current_page += 1

        assert not teacher_found, f"Объявление с именем '{teacher_name}' найдено!"

    @allure.step("Убедиться что имя в объявлении совпадает с заданным")
    def verify_announcement_tutor_name(self, expected_name):
        tutor_name_announcement = self.page.locator("h5").inner_text()
        assert expected_name == tutor_name_announcement

    @allure.step("Убедиться, что обязательные поля не заполнены")
    def verify_required_fields_are_not_filled(self):
        error_message_count = self.page.locator(
            '//strong[text()="Обязательное поле."]'
        ).count()
        print(f"Found {error_message_count} error messages.")
        assert error_message_count == 12, (
            f"Expected 12 error messages, but found {error_message_count}"
        )

    @allure.step("Создаем объявление")
    def create_announcement(self):
        self.fill_first_name("John")
        self.fill_last_name("Pak")
        self.fill_telegram("@JPak")
        self.fill_phone_number("5555555")
        self.fill_out_description("Great teacher")
        self.pick_student_age_category()
        self.upload_photo()
        self.fill_out_lesson_style("Fast")
        self.fill_out_can_help_field("Guaranteed success")
        self.pick_category("1")
        self.fill_out_experience("5")
        self.checkbox_degree()
        self.fill_out_price("1000")
        self.fill_out_class_duration("60")
        self.click_save_announcement_btn()

    @allure.step("Создаем объявление с обязательными полями")
    def create_announcement_with_only_required_fields(self):
        self.fill_first_name("Thomas")
        self.fill_last_name("Peters")
        self.fill_telegram("ThomasP")
        self.fill_phone_number("14103902623")
        self.fill_out_description("Great teacher")
        self.fill_out_can_help_field()
        self.fill_out_lesson_style()
        self.pick_student_age_category()
        self.upload_photo()
        self.pick_category("1")
        self.fill_out_experience("5")
        self.fill_out_price("1000")
        self.fill_out_class_duration("60")
        self.click_save_announcement_btn()

    @allure.step(
        "Проверяем, что все обязательные поля отмечены '*'/ 'Обязательное поле'"
    )
    def verify_mandatory_fields_are_marked(self):
        fields_to_check = [
            (
                "//label[@for='id_first_name']//span[@class='asteriskField']",
                "id_first_name",
            ),
            (
                "//label[@for='id_last_name']//span[@class='asteriskField']",
                "id_last_name",
            ),
            (
                "//label[@for='id_telegram']//span[@class='asteriskField']",
                "id_telegram",
            ),
            ("//label[@for='id_phone']//span[@class='asteriskField']", "id_phone"),
            (
                "//label[@for='id_description']//span[@class='asteriskField']",
                "id_description",
            ),
            (
                "//legend[@class='form-label requiredField']//span[@class='asteriskField']",
                "student_category",
            ),
            (
                "//label[@for='id_can_help']//span[@class='asteriskField']",
                "id_can_help",
            ),
            (
                "//label[@for='id_category']//span[@class='asteriskField']",
                "id_category",
            ),
            (
                "//label[@for='id_years_of_experience']//span[@class='asteriskField']",
                "id_years_of_experience",
            ),
            ("//label[@for='id_price']//span[@class='asteriskField']", "id_price"),
            (
                "//label[@for='id_class_duration']//span[@class='asteriskField']",
                "id_class_duration",
            ),
        ]

        for locator, field_name in fields_to_check:
            field_mark = self.page.locator(locator)
            assert field_mark.is_visible(), (
                f"Отметка поля с локатором {field_name} не найдена"
            )

        download_photo_title_text = self.page.get_by_text(
            "Рекомендуемое разрешение:"
        ).inner_text()
        assert "Обязательное поле." in download_photo_title_text, (
            f"Текст 'Обязательное поле.' не найден в {download_photo_title_text}"
        )

    @allure.step("Отчищаем все обязательные поля")
    def clear_mandatory_fields(self):
        self.fill_first_name("")
        self.fill_last_name("")
        self.fill_telegram("")
        self.fill_phone_number("")
        self.fill_out_description("")
        self.clear_student_category_checkboxes()
        self.fill_out_can_help_field("")
        self.fill_out_lesson_style("")
        self.pick_category("")
        self.fill_out_experience("")
        self.fill_out_price("")
        self.fill_out_class_duration("")
        self.click_save_announcement_btn()

    @allure.step("Проверяем наличие сообщений 'Обязательное поле' в пустых полях")
    def verify_mandatory_field_error_messages(self):
        error_message_locators = [
            "#error_1_id_first_name strong",
            "#error_1_id_last_name strong",
            "#error_1_id_telegram strong",
            "#error_1_id_phone strong",
            "#error_1_id_description strong",
            "#error_1_id_student_categories strong",
            "#error_1_id_can_help strong",
            "#error_1_id_lesson_style strong",
            "#error_1_id_category strong",
            "#error_1_id_years_of_experience strong",
            "#error_1_id_years_of_experience strong",
            "#error_1_id_class_duration strong",
        ]
        for locator in error_message_locators:
            message = self.page.locator(locator)
            assert message.inner_text() == "Обязательное поле."
