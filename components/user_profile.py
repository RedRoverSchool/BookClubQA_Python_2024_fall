import allure
from playwright.sync_api import Page, expect

class UserProfile:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Проверяем видимость кнопки 'Профиль'")
    def visibility_profile_btn_check(self):
        expect(self.page.locator("//a[@data-testid='profile']")).to_be_visible()

    @allure.step("Наводим курсор на кнопку 'Профиль' и проверяем изменение ее цвета")
    def hover_profile_btn_color_check(self):
        button = self.page.locator("//a[@data-testid='profile']")
        original_color = button.evaluate("el => getComputedStyle(el).backgroundColor")
        button.hover()
        expect(button).not_to_have_css("background-color", original_color)

    @allure.step("Кликакем кнопку 'Профиль'")
    def click_profile_btn(self):
        self.page.locator("//a[@data-testid='profile']").click()

    @allure.step("Проверяем URL страницы 'Профиль'")
    def profile_btn_redirection_check(self):
        assert self.page.url == "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/subscription/profile/"
