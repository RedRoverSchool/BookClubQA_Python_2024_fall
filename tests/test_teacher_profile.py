import allure


@allure.title("TC_13.005.002")
def test_teacher_able_get_announcement_page(header, login, announcement):
    login.open_login_page()
    login.enter_username("kick01@mail.ru")
    login.enter_password("123QW654")
    login.click_login_button()
    announcement.click_my_announcement_button()
    announcement.verify_my_announcements_page_endpoint()









