from playwright.sync_api import Page, expect

import allure


class HeaderStudentPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Проверяем наличие кнопки 'Мыслеплав'")
    def check_mysleplav_btn_exists(self):
        expect(self.page.get_by_test_id("logo")).to_be_visible()

    @allure.step("Кликаем на кнопку 'Мыслеплав'")
    def click_omysleplav_btn(self):
        self.page.get_by_test_id("logo").click()



    @allure.step("Проверяем наличие кнопки 'Мои репетиторы'")
    def check_my_teachers_btn_exists(self):
        expect(self.page.locator('a', has_text="Мои репетиторы")).to_be_visible()

    @allure.step("Кликаем на кнопку 'Мои репетиторы'")
    def click_my_teachers_btn(self):
        self.page.locator('a', has_text="Мои репетиторы").click()

    @allure.step("Проверяем заголовок - страница Мои репетиторы открылась")
    def verify_page_my_teachers_opened(self):
        title = self.page.get_by_title("Объявления")
        assert "Объявления", title
