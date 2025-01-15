import allure
from playwright.sync_api import Page, expect
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
        pictures = self.page.locator("img")
        pictures_count = pictures.count()
        assert pictures_count > 0, "Нет изображений аватарок преподавателей на странице"
        for i in range(pictures_count):
            picture = pictures.nth(i)
            picture.wait_for(state="visible", timeout=5000)
            assert picture.is_visible(), f"Аватарка преподавателя {i + 1} не видна"
            image_src = picture.get_attribute("src")
            assert image_src, f"Изображение {i + 1} не имеет атрибута 'src'"

    @allure.step("Проверяем видимость имён преподавателей")
    def check_name_of_tutor_is_visible(self):
        names = self.page.locator("//h5[@class='fw-bold text-dark mb-0']")
        names_count = names.count()
        assert names_count > 0, "Нет имен преподавателей на странице"
        for i in range(names_count):
            name_element = names.nth(i)
            name_text = name_element.text_content()
            name_element.wait_for(state="visible", timeout=5000)
            assert name_text.strip() != "", f"Имя преподавателя {i + 1} пустое"
            assert name_element.is_visible()

    @allure.step("Проверяем видимость названия предмета")
    def check_subject_of_tutor_is_visible(self):
        subjects = self.page.locator("//p[@class='text-secondary']")
        subjects_count = subjects.count()
        assert subjects_count > 0, "Нет предметов на странице"
        for i in range(subjects_count):
            subject = subjects.nth(i)
            subject.wait_for(state="visible", timeout=5000)
            assert subject.is_visible(), f"Предмет {i + 1} не виден"

    @allure.step("Проверяем видимость цены")
    def check_price_is_visible(self):
        assert self.page.get_by_text("Стоимость занятия:").nth(0).is_visible()

    @allure.step("Проверяем наличие сообщения об успешной регистрации")
    def check_message_of_registration(self, expected_message):
        alert_locator = self.page.locator("//div[@role='alert']")
        self.page.wait_for_selector("//div[@role='alert']", timeout=7000)
        message = alert_locator.text_content()
        assert (
            message.strip() == expected_message
        ), f"Expected text is '{expected_message}', but received '{message.strip()}'"

    @allure.step("Проверяем фильтр по категории")
    def check_filter_form(self):
        self.page.wait_for_load_state()
        frw_btn = self.page.get_by_role("link", name="Вперед")
        all_tutors_math = self.page.get_by_role("heading", name="Математика").count()

        while frw_btn.count() > 0:
            frw_btn.click()
            self.page.wait_for_load_state()
            all_tutors_math += self.page.get_by_role(
                "heading", name="Математика"
            ).count()

        self.page.locator("//select[@id='categorySelect']").select_option("Математика")
        self.page.locator("button.btn.btn-primary.btn-lg.me-2").click()
        self.page.wait_for_load_state()
        all_tutors_math_filtered = self.page.get_by_role(
            "heading", name="Математика"
        ).count()

        while frw_btn.count() > 0:
            frw_btn.click()
            self.page.wait_for_load_state()
            all_tutors_math_filtered += self.page.get_by_role(
                "heading", name="Математика"
            ).count()

        assert all_tutors_math == all_tutors_math_filtered

    @allure.step("Нажимаем на кнопку Фильтровать")
    def click_filter_button(self):
        self.page.get_by_text("Применить").click()

    @allure.step("Разворачиваем раздел фильтрации")
    def open_filter_widget(self):
        self.page.locator("#filterButton").click()

    @allure.step("Вводим значение минимальной цены")
    def enter_min_price(self, min_price: float):
        price_field = self.page.locator("#minPrice")
        price_field.fill(str(min_price))

    @allure.step(
        "Проверяем, что цены за занятие репетиторов больше или равны заданного значения"
    )
    def check_prices_over_min_price(self, min_price: float) -> object:
        # Проверяем, есть ли репетиторы на странице
        price_siblings_list = self.page.get_by_text("Стоимость занятия:")
        if price_siblings_list.count() > 0:
            # Если репетиторы есть, то проверяем, что их стоимость занятия >= установленной минимальной цены
            for i in range(price_siblings_list.count()):
                price_sibling = price_siblings_list.nth(i)
                actual_price_in_string = (
                    price_sibling.locator("+ p").text_content().strip()
                )
                actual_price = float(actual_price_in_string.split(" ")[0])
                assert actual_price >= min_price
        else:
            # Если список репетиторов пустой, то проверяем сообщение
            text = self.page.locator(".bg-white.p-3.mt-3").text_content()
            assert "По вашему запросу нет результатов.", text

    @allure.step(
        "Проверяем, что опыт преподавания репетиторов больше или равен заданному значению"
    )
    def check_experience_over_min_value(self, min_experience: int):
        filtered_cards = self.page.locator("//div[@class='row']/div")

        card_count = filtered_cards.count()
        assert card_count > 0, "The filter returned an empty list"

        for i in range(card_count):
            card = filtered_cards.nth(i)
            more_details_btn = card.get_by_text("Подробнее")
            more_details_btn.click()
            experience_text = self.page.locator(
                "//p[contains(text(),'лет')]"
            ).inner_text()
            experience_value = int(experience_text.split()[0])
            assert (
                experience_value >= min_experience
            ), f"The Teaching Experience {experience_value} less than expected minimum {min_experience}"

            self.page.go_back()

    @allure.step('Проверяем видимость кнопки "Фильтровать"')
    def check_filter_btn_is_visible(self):
        filter_btn = self.page.locator(
            'button.btn.btn-primary.btn-lg.me-2[type="submit"]'
        )
        assert filter_btn.is_visible()

    @allure.step('Нажимаем на кнопку "Фильтровать"')
    def click_filter_btn(self):
        filter_btn = self.page.locator(
            '//button[@type="submit" and contains(@class, "btn-dark") and text()="Вперед"]'
        )
        filter_btn.click()
        assert self.page.url == (
            "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/listings/list/?category=&min_experience=0&min_price=&max_price="
        )

    @allure.step('Проверяем видимость кнопки "Подробнее"')
    def check_btn_more_is_visible(self):
        btn_more = self.page.locator('(//a[text()="Подробнее"])[1]')
        assert btn_more.is_visible()

    @allure.step('Проверяем кнопку "Подробнее" на клиабильность')
    def check_btn_more_is_clickable(self):
        btn_more = self.page.locator('(//a[text()="Подробнее"])[1]')
        btn_more.click()
        assert self.page.url == (
            "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/listings/1/"
        )

    @allure.step('Проверяем каждый профиль содержит кнопку "Подробнее"')
    def check_btn_more_has_each_profile(self):
        self.page.wait_for_load_state("networkidle", timeout=5000)
        btn_more = self.page.locator('//a[@class="btn btn-primary btn-lg mt-3"]')
        expect(btn_more).not_to_have_count(0, timeout=3000)

        for i in range(btn_more.count()):
            expect(btn_more.nth(i)).to_be_visible()

    @allure.step("Определяем случайную минимальную цену")
    def set_random_min_price(self, fake, min_value: int, max_value: int):
        min_price = fake.random_int(min=min_value, max=max_value)
        return min_price

    @allure.step("Вводим значение минимального опыта преподавания")
    def enter_min_experience(self, min_experience: int):
        experience_field = self.page.locator("#minExperience")
        experience_field.wait_for(state="visible", timeout=3000)
        assert (
            experience_field.is_visible()
        ), "The 'Minimum Teaching Experience' field is not visible."
        assert (
            experience_field.is_enabled()
        ), "The 'Minimum Teaching Experience' field is not enabled."
        experience_field.fill(str(min_experience))
