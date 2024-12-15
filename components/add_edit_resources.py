import allure
from playwright.sync_api import Page, expect
from Data import data
from Data import constants
from faker import Faker

fake = Faker()


class AddEditResources:
    def __init__(self, page: Page):
        self.password = None
        self.page = page

    @allure.step("Вводим текст ресурсов")
    def fill_resource_textarea(self):
        resource_textarea = self.page.locator('#resources')
        resource_text = fake.text()
        resource_textarea.fill(resource_text)
        return resource_text

    @allure.step("Нажимаем кнопку 'Сохранить'")
    def click_save_resources_button(self):
        self.page.locator("button", has_text="Сохранить").click()

    @allure.step("Добавляем ресурсы")
    def add_resources(self):
        resource_textarea = self.page.locator('#resources')
        resource_text = fake.text()
        resource_textarea.fill(resource_text)
        self.page.locator("button", has_text="Сохранить").click()
        return resource_text


