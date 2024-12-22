import allure
from playwright.sync_api import Page
from core.settings import list_url, tutors_list_url
from faker import Faker

fake = Faker()


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
        assert (
            message.strip() == expected_message
        ), f"Expected text is '{expected_message}', but received '{message.strip()}'"


    @allure.step("Проверяем фильтр по категории")
    def check_filter_form(self):
        self.page.wait_for_load_state()
        frw_btn = self.page.get_by_role("link", name="Вперед")
        all_tutors_math = self.page.get_by_role("heading", name = "Математика").count()

        while frw_btn.count() > 0:
            frw_btn.click()
            self.page.wait_for_load_state()
            all_tutors_math += self.page.get_by_role("heading", name="Математика").count()

        self.page.get_by_label("Категория").select_option('Математика')
        self.page.get_by_role("button", name="Фильтровать").click()
        self.page.wait_for_load_state()
        all_tutors_math_filtered = self.page.get_by_role("heading", name="Математика").count()

        while frw_btn.count() > 0:
            frw_btn.click()
            self.page.wait_for_load_state()
            all_tutors_math_filtered += self.page.get_by_role("heading", name="Математика").count()

        assert all_tutors_math == all_tutors_math_filtered


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

    @allure.step('Проверяем видимость кнопки "Фильтровать"')
    def check_filter_btn_is_visible(self):
        filter_btn = self.page.locator('//button[@type="submit" and contains(@class, "btn-dark") and text()="Фильтровать"]')
        assert filter_btn.is_visible()


    @allure.step('Определяем случайную минимальную цену')
    def set_random_min_price(self, fake, min_value: int, max_value: int):
        min_price = fake.random_int(min=min_value, max=max_value)
        return min_price

    @allure.step("Вводим значение минимального опыта преподавания")
    def enter_min_experience(self, min_experience: int):
        experience_field = self.page.locator('#minExperience')
        experience_field.wait_for(state="visible", timeout=3000)
        assert experience_field.is_visible(), "The 'Minimum Teaching Experience' field is not visible."
        assert experience_field.is_enabled(), "The 'Minimum Teaching Experience' field is not enabled."
        experience_field.fill(str(min_experience))

    @allure.step("Проверяем, что опыт преподавания репетиторов больше или равен заданному значению")
    def check_experience_over_min_value(self, min_experience: int):
        teachers_list_experience = self.page.locator(".card-text")
        if teachers_list_experience.count() > 0:
            for i in range(teachers_list_experience.count()):
                text_content = teachers_list_experience.nth(i).text_content().strip()
                if "Опыт:" in text_content:
                    try:
                        actual_experience = int(''.join(filter(str.isdigit, text_content.split("Опыт:")[1])))
                        assert actual_experience >= min_experience, f"Found tutor with experience {actual_experience} < {min_experience}"
                    except (IndexError, ValueError) as e:
                        raise AssertionError(f"Failed to parse experience from text: '{text_content}'. Error: {e}")
                else:
                    continue
        else:
            text = self.page.locator("//div[@class='alert alert-info']").text_content().strip()
            assert "Нет результатов" in text, f"Unexpected message: '{text}'"
