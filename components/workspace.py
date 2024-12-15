import allure
from playwright.sync_api import Page, expect
from core.settings import login_url


class Workspace:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открываем пригласительную ссылку")
    def navigate_to_invite_link(self, invite_link):
        self.page.goto(invite_link)

    @allure.step("Кликаем кнопку 'Добавить ресурсы'")
    def navigate_to_add_resources(self):
        self.page.locator("a", has_text="Добавить ресурсы").click()

    @allure.step("Убедиться, что текст ресурсов совпадает с введенным текстом")
    def verify_resource_text(self, original_text: str):
        trimmed_original_text = ' '.join(original_text.replace('\n', ' ').split())
        displayed_resource_text = self.page.locator("section.resources p").inner_text().rstrip()
        assert displayed_resource_text == trimmed_original_text

