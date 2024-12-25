import allure
from playwright.sync_api import Page


class UserProfile:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Проверяем URL страницы 'Профиль'")
    def profile_btn_redirection_check(self):
        assert (
                self.page.url
                == "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/subscription/profile/"
        )