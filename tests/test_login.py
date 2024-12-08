""""Для проверки CI"""""


def test_login_as_tutor_btn_create_listing(header, login):
    login.open_login_page()
    header.click_on_login_button
    login.enter_username("test_auth_login")
    login.enter_password("test_auth_pass")
    login.click_login_button()
    header.create_listing_button_should_be_visible
