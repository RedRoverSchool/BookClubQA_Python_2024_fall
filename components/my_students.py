import allure
from playwright.sync_api import Page, expect
from Data import data
from Data import constants
from faker import Faker

fake = Faker()


class MyStudents:
    def __init__(self, page: Page):
        self.password = None
        self.page = page

    @allure.step("Кликаем кнопку 'Генерировать пригласительную ссылку'")
    def click_generate_invite_button(self):
        self.page.locator('#generate-link-btn').click()
        # invite_create_failure = self.page.locator('#alert-container [role=alert]')
        # expect(invite_create_failure).not_to_be_visible()
        self.page.wait_for_timeout(30000)

    @allure.step("Копируем пригласительную ссылку")
    def get_invite_link(self):
        return 'http://testing.misleplav.ru/dashboard/accept_invitation/099e45c0-deca-4b6e-a142-160877241a77/'

    @allure.step("Выбираем студента")
    def navigate_to_student_dashboard(self, student_name):
        self.page.locator('section.list-group').get_by_text(student_name).click()



