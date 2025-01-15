from playwright.sync_api import Page, expect
import allure


class MyTeachersPage:
    def __init__(self, page: Page) -> object:
        self.page = page

    @allure.step("Проверяем наличие кнопки 'Мои репетиторы'")
    def check_my_teachers_btn_exists(self):
        expect(
            self.page.locator("#navbarNav > ul > li:nth-child(2) > a")
        ).to_be_visible()

    @allure.step("Кликаем на кнопку 'Мои репетиторы'")
    def click_my_teachers_btn(self):
        self.page.locator("#navbarNav > ul > li:nth-child(2) > a").click()

    @allure.step("Проверяем заголовок - страница Мои репетиторы открылась")
    def verify_page_my_teachers_opened(self):
        title = self.page.get_by_title("Объявления")
        assert "Объявления", title

    @allure.step("Проверяем, что список репетиторов отображается или нет")
    def check_teachers_list(self) -> object:
        # Проверяем, есть ли элементы репетиторов на странице
        teachers_list = self.page.locator(".card-body")
        if teachers_list.count() > 0:
            # Если репетиторы есть, проверяем их
            for i in range(teachers_list.count()):
                teacher = teachers_list.nth(i)
                expect(
                    teacher.locator(".card-img-top")
                ).to_be_visible()  # Проверка, что есть картинка
                expect(
                    teacher.locator(".card-title")
                ).to_have_text()  # Проверка, что есть имя
                expect(
                    teacher.locator(".card-subtitle mb-2 text-muted")
                ).to_have_text()  # Дополнительная информация
        else:
            # Если репетиторов нет, проверяем сообщение
            no_teachers_message = self.page.locator(
                'text="У вас пока нет Репетиторов. Попросите репетитора отправить вам приглашение."'
            )
            expect(no_teachers_message).to_be_visible()
