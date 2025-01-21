import pytest
from faker import Faker
from Data.data import EMAIL_STUDENT_KM, PASSWORD_STUDENT_KM

fake = Faker()

STUDENT_SUCCESS_REGISTRSTION_MESSAGE = "Вы успешно зарегистрировались!"
text = "Вы успешно зарегистрировались, а так же получаете бесплатный премиум на 3 дня!"


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_register_as_tutor(header, register):
    header.visit()
    header.click_registration_button()
    register.header_should_contain_text("Регистрация")
    register.registration_new_user("tutor")
    # header.create_listing_button_should_be_visible()


# @pytest.mark.slow
@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_register_as_student(header, register):
    header.visit()
    header.click_registration_button()
    register.header_should_contain_text("Регистрация")
    register.registration_new_user("student")


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_register_as_student_verify_success_message_text(
    homepage, register, find_tutor
):
    """Проверка успешного сообщения после регистрации как студента"""
    homepage.visit()
    homepage.click_registration_button()
    register.verify_registration_page_opened()
    register.registration_new_user("student")
    find_tutor.check_message_of_registration(STUDENT_SUCCESS_REGISTRSTION_MESSAGE)


# TC_35.001.001.001 | Student >Become a teacher > Navigate to the "Стать репетитором" page


def test_become_a_teacher_from_student_page(
    header, login, homepage, register, find_tutor
):
    """Проверка перехода на страницу регистрации как репетитор из профиля студента."""
    header.visit()
    login.full_login(EMAIL_STUDENT_KM, PASSWORD_STUDENT_KM)
    header.click_logo_misleplav()
    homepage.click_become_tutor_btn()
    register.register_page_contains_register_btn()


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_verify_successful_message_after_register_as_tutor(
    homepage, register, find_tutor
):
    homepage.visit()
    homepage.click_registration_button()
    # переходим на страницу регистрации
    register.header_should_contain_text("Регистрация")
    register.registration_new_user("tutor")
    find_tutor.check_message_of_registration(text)


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_check_placeholders_on_the_register_page(header, register):
    header.visit()
    header.click_registration_button()
    register.check_username_placeholder_visibility()
    register.check_username_placeholder_text()
    register.check_password1_placeholder_visibility()
    register.check_password1_placeholder_text()
    register.check_password2_placeholder_visibility()
    register.check_password2_placeholder_text()
