import pytest
from faker import Faker

fake = Faker()


def test_register_as_tutor(header, register):
    header.visit()
    header.click_on_registration_button()
    register.header_should_contain_text("Регистрация")
    register.fill_nick(fake.user_name())
    register.fill_password("sdjflsfdjlksdjflksdjf")
    register.fill_confirm_password("sdjflsfdjlksdjflksdjf")
    register.click_on_become_a_teacher_button()
    register.click_on_registration_button()
    header.create_listing_button_should_be_visible()


@pytest.mark.slow
def test_register_as_student(header, register):
    header.visit()
    header.click_on_registration_button()
    register.header_should_contain_text("Регистрация")
    register.fill_nick(fake.user_name())
    register.fill_password("sdjflsfdjlksdjflksdjf")
    register.fill_confirm_password("sdjflsfdjlksdjflksdjf")
    register.click_on_registration_button()
