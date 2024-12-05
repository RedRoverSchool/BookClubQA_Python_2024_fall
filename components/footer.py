from playwright.sync_api import Page, expect
from core.settings import base_url
import allure


class Footer:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открываем Footer на главной странице")
    def visit(self):
        self.page.goto(base_url)

    @allure.step("Прокучиваем страницу до Футера")
    def scroll_down_to_the_footer(self):
        self.page.get_by_text("© 2024 Мыслеплав. Все права защищены.").scroll_into_view_if_needed()