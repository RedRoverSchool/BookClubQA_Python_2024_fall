from playwright.sync_api import Page

from conftest import announcement


def test_create_announcement(login, header, announcement):
    header.visit()
    header.click_on_login_button()
    login.full_login("Test2", "testpassword1")
    header.click_on_create_announcement_btn()
    announcement.fill_out_fullname()
    announcement.fill_out_descripption()
    # announcement.upload_photo()
    announcement.pick_category()
    announcement.fill_out_experience()
    announcement.checkbox_degree()
    announcement.checkbox_free_first_lesson()
    announcement.fill_out_price()
    announcement.fill_out_class_duration()
    announcement.add_contact_info()
    # announcement.click_create_announcement_btn()