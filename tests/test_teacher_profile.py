from playwright.sync_api import Page
from components.teacher_profile import TeacherProfile
from core.settings import tutors_list_url


# TC_05.001.008.001 | Guest > Find a Teacher page > Teacher Profile > Navigate to the detailed profile page

def test_my_teachers_btn_click(teacher_profile, page: Page):
    """Проверка клика на кнопку 'Подробнее'."""
    page.goto(tutors_list_url, wait_until="domcontentloaded")
    more_details_button = TeacherProfile(page)
    more_details_button.click_more_details_btn()









