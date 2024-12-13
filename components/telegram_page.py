import allure
from playwright.sync_api import Page, expect


class TelegramPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открываем компонент More info about students from the homepage")
    def students_info_should_be_opened(self):
        expect(self.page).to_have_url("https://t.me/misleplav_students/9")

    @allure.step("check_telegram_channel_should_have_title_for_students")
    def check_telegram_channel_should_have_title_for_students(self):
        expect(self.page).to_have_title("Telegram: Contact @misleplav_students")

    @allure.step("Открываем компонент More info about tutors from the main(body)")
    def tutors_info_should_be_opened(self):
        expect(self.page).to_have_url("https://t.me/misleplav_tutors/11")

    @allure.step("check_telegram_channel_should_have_title_for_tutor")
    def check_telegram_channel_should_have_title_for_tutors(self):
        expect(self.page).to_have_title("Telegram: Contact @misleplav_tutors")
