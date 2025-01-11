# import allure
# from playwright.sync_api import Page, expect
# from core.settings import first_teacher_announcement_url


# class TeacherAnnouncement:
#     def __init__(self, page: Page):
#         self.page = page

# @allure.step("")
# def redirection_to_teacher_announcement(self):
#     self.page.locator('a.btn.btn-outline-dark[href="/listings/1/"]').click()
#     expect(self.page).to_have_url(first_teacher_announcement_url)
