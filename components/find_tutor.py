import allure

from playwright.sync_api import Page, expect
from core.settings import list_url


class FindTutor:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Проверяем наличие кнопки 'Регистрация'")
    def check_title_of_registration(self):
        title = self.page.get_by_title("Регистрация")
        assert "Регистрация", title

    @allure.step("Проверяем открытие окна со списком аккаунтов преподавателей")
    def check_list_of_tutors_is_opened(self):
        assert self.page.url == list_url

    @allure.step("Проверяем видимость картинок в списке преподавателей")
    def check_picture_of_tutor_is_visible(self):
        picture = self.page.locator('//img[@class="card-img-top"]').nth(0)
        assert picture.is_visible()

    @allure.step("Проверяем видимость имён преподавателей")
    def check_name_of_tutor_is_visible(self):
        name = self.page.locator('//h5[@class="card-title"]').nth(0)
        assert name.is_visible()

    @allure.step("Проверяем видимость названия предмета")
    def check_subject_of_tutor_is_visible(self):
        subject = self.page.locator('//h6[@class="card-subtitle mb-2 text-muted"]').nth(
            0
        )
        assert subject.is_visible()

    @allure.step("Проверяем видимость цены")
    def check_price_is_visible(self):
        assert self.page.get_by_text("Цена").nth(0).is_visible()

    @allure.step("Проверяем наличие сообщения об успешной регистрации")
    def check_message_of_registration(self, expected_message):
        message = self.page.locator("//div[@role='alert']").text_content()
        assert message.strip() == expected_message

    @allure.step("Выбор категории")
    def select_category(self):
        value = self.page.get_by_label('Категория')
        value.select_option('1')

    @allure.step("Выбор бесплатного урока")
    def free_first_lesson(self):
        self.page.locator('//input[@id="firstLessonCheck"]').check()

    @allure.step("Фильтр")
    def filter(self):
        self.page.get_by_text('Фильтровать').click()

    @allure.step("Проверяем и подтверждаем наличия преподавателей")
    def list_of_card_teacher(self):
        lst = []
        locator = self.page.locator("//div[@class = 'card h-100']")
        lst.append(locator)
        size_list = len(lst)
        assert size_list, size_list > 0

