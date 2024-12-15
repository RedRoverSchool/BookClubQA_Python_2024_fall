from random import randint
from playwright.sync_api import Page, expect
import allure
from faker import Faker
fake = Faker()


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


    def select_random_dropdown_option(self, select_locator):
        select_locator.wait_for()
        options_element_list = select_locator.locator('option').all()
        option_list = {x.get_attribute('value'): x.inner_text() for x in options_element_list if x.get_attribute('value')}
        option_values = list(option_list.keys())
        rand_el = randint(0, len(option_values) - 1)
        option_to_select = option_list[option_values[rand_el]]
        selected_option_value = select_locator.select_option(option_to_select)
        selected_option = select_locator.locator(f'[value="{selected_option_value[0]}"]').inner_text()
        return {'value': option_values[rand_el], 'text': selected_option}


    @allure.step("Создаём объявление")
    def fill_new_announcement_form(self):
        # locators
        fio_field = self.page.locator('#id_name')
        body_field = self.page.locator('#id_description')
        photo_field = self.page.locator('#id_photo')
        subject_category_dropdown = self.page.locator('#id_category')
        experience_field = self.page.locator('#id_years_of_experience')
        education_checkbox = self.page.locator('#id_has_degree')
        price_field = self.page.locator('#id_price')
        duration_field = self.page.locator('#id_class_duration')
        free_first_lesson_checkbox = self.page.locator('#id_free_first_lesson')
        phone_field = self.page.locator('#id_phone')
        telegram_field = self.page.locator('#id_telegram')
        email_field = self.page.locator('#id_email')
        add_contact_button = self.page.locator('#addContactBtn')
        contact_method_dropdown = self.page.locator('.form-control.contact-method')
        contact_field = self.page.locator('.form-control.contact-detail')
        save_button = self.page.locator("button", has_text="Сохранить")

        # values
        fio_value = f'{fake.first_name()} {fake.last_name()}'
        body_value = fake.text(500)
        photo_value = "../Data/upload_files/stock-photo-handsome-cheerful-man.jfif"
        experience_value = randint(0, 120) / 10
        price_value = randint(100, 1000)
        duration_value = randint(10, 120)
        phone_value = fake.phone_number()
        telegram_value = fake.word()
        email_value = fake.email()

        # logic
        fio_field.fill(fio_value)
        body_field.fill(body_value)
        photo_field.set_input_files(files=[photo_value])
        category_selected_option = self.select_random_dropdown_option(subject_category_dropdown)['text']
        experience_field.fill(str(experience_value))
        education_checkbox.check()
        price_field.fill(str(price_value))
        duration_field.fill(str(duration_value))
        free_first_lesson_checkbox.check()
        phone_field.fill(phone_value)
        telegram_field.fill(telegram_value)
        email_field.fill(email_value)
        '''contact_values = []
        for i in range(2):
            add_contact_button.click()
            current_contact_method_dropdown = contact_method_dropdown.nth(i)
            contact_method_selected_option = self.select_random_dropdown_option(current_contact_method_dropdown)['text']
            contact_value = fake.word()
            current_contact_field = contact_field.nth(i)
            current_contact_field.fill(contact_value)
            contact_values.append([contact_method_selected_option, contact_value])'''
        save_button.click()
        self.page.wait_for_timeout(15000)

        return {
            'fio_value': fio_value,
            'body_value': body_value,
            'photo_value': photo_value,
            'category_value': category_selected_option,
            'experience_value': experience_value,
            'education_checkbox': True,
            'price_value': price_value,
            'duration_value': duration_value,
            'free_first_lesson_checkbox': True,
            'phone_value': phone_value,
            'telegram_value': telegram_value,
            'email_value': email_value,
        }

    @allure.step("Перехват")
    def intercept(self):
        # self.page.wait_for_timeout(10000)
        print('end wait')
        def handle_route(route, request):
            print('129aaa', route.request)
            print('129aaa', request)
            print('129aaa', request.headers)
            print('129aaa', route)
            route.continue_()
        url = 'http://testing.misleplav.ru/dashboard/generate_invitation_link/'
        # self.page.route(url, handle_route)
        # self.page.goto(url)
        self.page.wait_for_timeout(5000)
        print('end route')
        self.page.locator('#generate-link-btn').click()
        self.page.wait_for_timeout(20000)
        # with self.page.expect_response(url) as first:
        #     self.page.locator('#generate-link-btn').click()
        #     # self.page.get_by_text("trigger request").click()
        #     first_request = first.value
        #     print('123', first_request)
            # response = self.page.request.post('http://testing.misleplav.ru/dashboard/generate_invitation_link/')
        # print(response)
        self.page.on('request', lambda x: print(x))
        self.page.on('response', lambda x: print(x))
        self.page.wait_for_event('response', lambda x: print(x))
        self.page.wait_for_event('request', lambda x: print(x))
