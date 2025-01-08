import allure
from playwright.sync_api import Page, expect


class UserProfile:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Проверяем URL страницы 'Профиль'")
    def profile_btn_redirection_check(self):
        assert (
                self.page.url
                == "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/subscription/profile/"
        )

    @allure.step("Проверяем наличие кнопки 'Выйти' в профиле студента")

    def check_exit_btn_exists_for_student(self):
        exit_button = self.page.get_by_role("link", name="Выйти из аккаунта")
        return exit_button.is_visible()

    @allure.step("Кликаем кнопку 'Выйти' в профиле студента")
    def click_exit_btn_for_student(self):
        button = self.page.locator("//a[@href= '/authorization/logout/']")
        button.click()
        expect(self.page).to_have_url(
            "http://testing.misleplav.ru/")
