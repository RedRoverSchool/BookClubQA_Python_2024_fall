import allure
from playwright.sync_api import Page, expect

first_profile_page = "http://testing.misleplav.ru/listings/1/"

class TeacherProfile:
    def __init__(self, page: Page):
        self.page = page


    @allure.step("Кликаем кнопку 'Подробнее' на первой карточке учителя")
    def click_more_details_btn(self):
        self.page.locator("a", has_text="Подробнее").nth(0).click()
        expect(self.page).to_have_url(first_profile_page)
