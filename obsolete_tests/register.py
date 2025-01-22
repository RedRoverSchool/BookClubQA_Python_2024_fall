import pytest


@pytest.mark.skip(reason="Функциональность изменена, тест устарел.")
def test_check_placeholders_on_the_register_page(header, register):
    header.visit()
    header.click_registration_button()
    register.check_username_placeholder_visibility()
    register.check_username_placeholder_text()
    register.check_password1_placeholder_visibility()
    register.check_password1_placeholder_text()
    register.check_password2_placeholder_visibility()
    register.check_password2_placeholder_text()
