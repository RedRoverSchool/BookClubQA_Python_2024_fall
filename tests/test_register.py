from core.settings import fake_name_for_registration


def test_register_as_tutor(header, register):
    header.visit()
    header.click_on_registration_button()
    register.header_should_contain_text("Регистрация")
    register.fill_nick(fake_name_for_registration)
    register.fill_password("sdjflsfdjlksdjflksdjf")
    register.fill_confirm_password("sdjflsfdjlksdjflksdjf")
    register.click_on_become_a_teacher_button()
    register.click_on_registration_button()
    header.create_listing_button_should_be_visible()
