from playwright.sync_api import Page, expect
import allure


class CreateAnnouncement:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Убедиться, что все поля объявления пусты")
    def verify_the_announcement_form_is_blank(self):
        NO_CATEGORY_SELECTED_TEXT = '---------'
        # locators
        fio_field = self.page.get_by_placeholder('Ваше ФИО')
        body_field = self.page.locator('//trix-editor')
        photo_field = self.page.locator('#photo')
        subject_category_field = self.page.locator('#id_category option[selected]')
        experience_field = self.page.locator('#id_years_of_experience')
        education_checkbox = self.page.locator('#id_has_degree')
        free_first_lesson_checkbox = self.page.locator('#id_free_first_lesson')
        price_field = self.page.locator('#id_price')
        duration_field = self.page.locator('#id_class_duration')
        # contact_table_blank = self.page.locator('#contactTableBody:not(:has(tr))')
        contact_table_blank = self.page.locator('#contactTableBody', has_not=self.page.locator('tr'))

        photo_field_file_number = photo_field.evaluate('el => el.files.length')

        # assertions
        expect(fio_field).to_be_empty()
        expect(body_field).to_be_empty()
        expect(subject_category_field).to_have_text(NO_CATEGORY_SELECTED_TEXT)
        expect(experience_field).to_be_empty()
        expect(education_checkbox).not_to_be_checked()
        expect(free_first_lesson_checkbox).not_to_be_checked()
        expect(price_field).to_be_empty()
        expect(duration_field).to_be_empty()
        assert photo_field_file_number == 0
        expect(contact_table_blank).to_have_count(1)

    @allure.step("Кликаем на кнопку 'Создать' на странице формы объявления")
    def click_finalize_announcement_button(self):
        self.page.locator("button", has_text="Создать").click()

    @allure.step("Убедиться, что пользователь находится на странице 'Создать объявление'")
    def verify_create_announcement_page_endpoint(self):
        create_announcement_endpoint = '/listings/create/'
        current_url = self.page.url
        assert create_announcement_endpoint in current_url
