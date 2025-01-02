from random import randint
import os
from playwright.sync_api import Page, expect
import allure
from faker import Faker

fake = Faker()


class CreateAnnouncement:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Убедиться, что все поля объявления пусты")
    def verify_the_announcement_form_is_blank(self):
        NO_CATEGORY_SELECTED_TEXT = "---------"
        # locators
        first_name_field = self.page.locator('input[name="first_name"]')
        last_name_field = self.page.locator('input[name="last_name"]')
        telegram_field = self.page.locator('input[name="telegram"]')
        phone_number_field = self.page.locator('input[name="phone"]')
        body_field = self.page.locator("#id_description")
        photo_field = self.page.locator("#id_photo")
        subject_category_field = self.page.locator("#id_category option[selected]")
        experience_field = self.page.locator("#id_years_of_experience")
        education_checkbox = self.page.locator("#id_has_degree")
        price_field = self.page.locator("#id_price")
        duration_field = self.page.locator('input[name="class_duration"]')
        discount_checkbox = self.page.locator("#id_package_discounts")
        convenient_time_field = self.page.locator('#id_convenient_time_slots')

        photo_field_file_number = photo_field.evaluate("el => el.files.length")

        # assertions
        expect(first_name_field).to_be_empty()
        expect(last_name_field).to_be_empty()
        expect(telegram_field).to_be_empty()
        expect(phone_number_field).to_be_empty()
        expect(body_field).to_be_empty()
        expect(subject_category_field).to_have_text(NO_CATEGORY_SELECTED_TEXT)
        expect(experience_field).to_be_empty()
        expect(education_checkbox).not_to_be_checked()
        expect(price_field).to_be_empty()
        expect(duration_field).to_be_empty()
        assert photo_field_file_number == 0
        expect(discount_checkbox).not_to_be_checked()
        expect(convenient_time_field).to_be_empty()


    @allure.step("Кликаем на кнопку 'Создать' на странице формы объявления")
    def click_finalize_announcement_button(self):
        self.page.locator(
            '//button[@type="submit" and contains(@class, "btn-dark") and text()="Сохранить"]'
        ).click()

    @allure.step(
        "Убедиться, что пользователь находится на странице 'Создать объявление'"
    )
    def verify_create_announcement_page_endpoint(self):
        create_announcement_endpoint = "/listings/create/"
        current_url = self.page.url
        assert create_announcement_endpoint in current_url

    def select_random_dropdown_option(self, select_locator):
        select_locator.wait_for()
        options_element_list = select_locator.locator("option").all()
        option_list = {
            x.get_attribute("value"): x.inner_text()
            for x in options_element_list
            if x.get_attribute("value")
        }
        option_values = list(option_list.keys())
        rand_el = randint(0, len(option_values) - 1)
        option_to_select = option_list[option_values[rand_el]]
        selected_option_value = select_locator.select_option(option_to_select)
        selected_option = select_locator.locator(
            f'[value="{selected_option_value[0]}"]'
        ).inner_text()
        return {"value": option_values[rand_el], "text": selected_option}

    @allure.step("Создаём объявление")
    def fill_submit_new_announcement_form(self):
        # locators
        fio_field = self.page.locator("#id_name")
        body_field = self.page.locator("#id_description")
        photo_field = self.page.locator("#id_photo")
        subject_category_dropdown = self.page.locator("#id_category")
        experience_field = self.page.locator("#id_years_of_experience")
        education_checkbox = self.page.locator("#id_has_degree")
        price_field = self.page.locator("#id_price")
        duration_field = self.page.locator("#id_class_duration")
        free_first_lesson_checkbox = self.page.locator("#id_free_first_lesson")
        phone_field = self.page.locator("#id_phone")
        telegram_field = self.page.locator("#id_telegram")
        email_field = self.page.locator("#id_email")
        save_button = self.page.locator("button", has_text="Сохранить")

        # values
        fio_value = f"{fake.first_name()} {fake.last_name()}"
        body_value = fake.text(max_nb_chars=500)
        root_dir = os.environ.get("ROOT_DIR")
        photo_path = os.path.join(root_dir, "Data", "upload_files", "silver_angel.png")
        experience_value = randint(0, 120) / 10
        price_value = randint(100, 1000)
        duration_value = randint(10, 120)
        phone_value = fake.phone_number()
        telegram_value = fake.word()
        email_value = fake.email()

        # logic
        fio_field.fill(fio_value)
        body_field.fill(body_value)
        photo_field.set_input_files(photo_path)
        category_selected_option = self.select_random_dropdown_option(
            subject_category_dropdown
        )["text"]
        experience_field.fill(str(experience_value))
        education_checkbox.check()
        price_field.fill(str(price_value))
        duration_field.fill(str(duration_value))
        free_first_lesson_checkbox.check()
        phone_field.fill(phone_value)
        telegram_field.fill(telegram_value)
        email_field.fill(email_value)
        save_button.click()

        return {
            "fio_value": fio_value,
            "body_value": body_value,
            "photo_value": photo_path,
            "category_value": category_selected_option,
            "experience_value": experience_value,
            "education_checkbox": True,
            "price_value": price_value,
            "duration_value": duration_value,
            "free_first_lesson_checkbox": True,
            "phone_value": phone_value,
            "telegram_value": telegram_value,
            "email_value": email_value,
        }
