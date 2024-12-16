import allure
from playwright.sync_api import Page
from core.settings import list_url, tutors_list_url


class FindTutor:
    def __init__(self, page: Page):
        self.page = page


    @allure.step("Открываем Найти Репетитора на главной странице")
    def open_find_tutor_page(self):
        self.page.goto(tutors_list_url)


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
        assert message.strip() == expected_message, f"Expected text is \'{expected_message}\', but received \'{message.strip()}\'"


    @allure.step("Нажимаем на кнопку Фильтровать")
    def click_filter_button(self):
        self.page.get_by_text("Фильтровать").click()


    @allure.step("Вводим значение минимальной цены")
    def enter_min_price(self, min_price: float):
        price_field = self.page.locator("#minPrice")
        price_field.fill(str(min_price))


    @allure.step("Проверяем, что цены за занятие репетиторов больше или равны заданного значения")
    def check_prices_over_min_price(self, min_price: float) -> object:
        # Проверяем, есть ли репетиторы на странице
        teachers_list_price = self.page.locator(".card-text")

        if teachers_list_price.count() > 0:
            # Если репетиторы есть, то проверяем, что их стоимость занятия >= установленной минимальной цены
            for i in range(teachers_list_price.count()):
                actual_price = float(teachers_list_price.nth(i).text_content().strip().split(" ")[1])
                assert actual_price >= min_price
        else:
            # Если список репетиторов пустой, то проверяем сообщение
            text = self.page.locator("//div[@class='alert alert-info']").text_content()
            assert "Нет результатов", text