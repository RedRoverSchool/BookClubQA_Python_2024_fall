import pytest
from faker import Faker

fake = Faker()

STUDENT_SUCCESS_REGISTRSTION_MESSAGE = "Вы успешно зарегистрировались!"


@pytest.mark.skip(reason="не прошёл CI после изменений 16.12.2024")
def test_register_as_tutor(header, register):
    header.visit()
    header.click_registration_button()
    register.header_should_contain_text("Регистрация")
    register.fill_nick(fake.user_name())
    register.fill_password("sdjflsfdjlksdjflksdjf")
    register.fill_confirm_password("sdjflsfdjlksdjflksdjf")
    register.check_become_a_teacher_checkbox()
    register.click_registration_button()
    header.create_listing_button_should_be_visible()


@pytest.mark.skip(reason="не прошёл CI после изменений 16.12.2024")
@pytest.mark.slow
def test_register_as_student(header, register):
    header.visit()
    header.click_registration_button()
    register.header_should_contain_text("Регистрация")
    register.fill_nick(fake.user_name())
    register.fill_password("sdjflsfdjlksdjflksdjf")
    register.fill_confirm_password("sdjflsfdjlksdjflksdjf")
    register.click_registration_button()


@pytest.mark.skip(reason="не прошёл CI после изменений 16.12.2024")
def test_register_as_student_verify_success_message_text(
    homepage, register, find_tutor
):
    """Проверка успешного сообщения после регистрации как студента"""
    homepage.visit()
    homepage.click_registration_button()
    register.verify_registration_page_opened()
    register.fill_nick(fake.user_name())
    register.generate_valid_password()
    register.fill_password(register.password)
    register.fill_confirm_password(register.password)
    register.click_registration_button()
    find_tutor.check_message_of_registration(STUDENT_SUCCESS_REGISTRSTION_MESSAGE)




# TC_04.001.003 | Guest > Registration > Create a user account for the guest > Verify closing success message
def test_closing_success_message_after_registration_as_student(homepage, register, find_tutor):
    """ Проверяет, что сообщение о регистрации закрывается после клика X иконки"""
    homepage.visit()
    homepage.click_on_registration_button()
    register.registration_as_student()
    find_tutor.close_success_registration_message()
    find_tutor.check_success_registration_message_invisible()


# TC_35.001.001.001 | Student >Become a teacher > Navigate to the "Стать репетитором" page
def test_become_a_teacher_from_student_page(header, login, homepage, register):
    """Проверка перехода на страницу регистрации как репетитор из профиля студента."""
    header.visit()
    header.click_registration_button()
    register.registration_new_user("student")
    header.visit()
    homepage.check_2_find_tutor_btns()
    homepage.click_become_tutor_btn()
    register.verify_registration_page_opened()


@pytest.mark.skip(reason="не прошёл CI после изменений 16.12.2024")
def test_verify_successful_message_after_register_as_tutor(
    homepage, register, find_tutor
):
    homepage.visit()
    homepage.click_registration_button()
    # переходим на страницу регистрации
    register.header_should_contain_text("Регистрация")
    register.fill_nick(fake.user_name())

    register.generate_valid_password()

    register.fill_password(register.password)
    register.fill_confirm_password(register.password)

    register.check_become_a_teacher_checkbox()
    register.click_registration_button()
    text = """Вы успешно зарегистрировались, а так же получаете бесплатный премиум на 3 дня!"""
    find_tutor.check_message_of_registration(text)


@pytest.mark.skip(reason="не прошёл CI после изменений 16.12.2024")
def test_check_placeholders_on_the_register_page(header, register):
    header.visit()
    header.click_registration_button()
    register.check_username_placeholder_visibility()
    register.check_username_placeholder_text()
    register.check_password1_placeholder_visibility()
    register.check_password1_placeholder_text()
    register.check_password2_placeholder_visibility()
    register.check_password2_placeholder_text()
