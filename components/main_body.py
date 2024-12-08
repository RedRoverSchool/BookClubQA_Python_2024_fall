from playwright.sync_api import Page, expect
import allure


class MainBodyPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("check_info_main_page")
    def check_info_main_page(self):
        self.page.get_by_role("main").text_content().split()

    @allure.step("check_info_main_page_before_and_after_reload")
    def reload(self):
        self.page.reload()
