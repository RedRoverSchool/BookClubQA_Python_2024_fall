import pytest
from api_clients.user_api import create_fake_user_with_role, delete_fake_user

@pytest.fixture
def fake_teacher():
    user = create_fake_user_with_role("teacher")
    yield user  # Передаем данные пользователя в тест
    delete_fake_user(user["email"])  # Удаляем пользователя после теста

@pytest.fixture
def fake_student():
    user = create_fake_user_with_role("student")
    yield user  # Передаем данные пользователя в тест
    delete_fake_user(user["email"])  # Удаляем пользователя после теста


def test_login_button_opens_login_page(header, login):
    header.visit()
    header.click_login_button()
    login.check_url_login_page("/login")


def test_verify_registration_options_on_registration_page(header, register):
    header.visit()
    header.click_registration_button()
    register.header_should_contain_text("Регистрация")


def test_verify_registration_options_on_login_page(header, login):
    header.visit()
    header.click_login_button()
    login.check_title_of_registration()


def test_verify_registration_options_on_find_tutor_page(header, find_tutor):
    header.visit()
    header.click_find_tutor_button()
    find_tutor.check_title_of_registration()


def test_support_visibility_as_teacher(login, header, fake_teacher):
    header.visit()
    header.click_login_button()
    login.full_login(fake_teacher["email"], fake_teacher["password"])
    header.support_button_should_be_visible()


def test_support_clickability_as_teacher(login, header, fake_teacher):
    header.visit()
    header.click_login_button()
    login.full_login(fake_teacher["email"], fake_teacher["password"])
    header.click_support_button()


def test_support_visibility_as_student(login, header, fake_student):
    header.visit()
    header.click_login_button()
    login.full_login(fake_student["email"], fake_student["password"])
    header.support_button_should_be_visible()


def test_support_clickability_as_student(login, header, fake_student):
    header.visit()
    header.click_login_button()
    login.full_login(fake_student["email"], fake_student["password"])
    header.click_support_button()


def test_hover_support_button_as_student(login, header, fake_student):
    header.visit()
    header.click_login_button()
    login.full_login(fake_student["email"], fake_student["password"])
    header.hover_support_button_color_check()


def test_verify_redirection_on_profile_page(login, header, create_user, register):
    register.select_role(is_teacher=True)
    register.click_registration_button()
    header.click_profile_button()
    header.profile_button_should_be_visible()


def test_login_button_is_visible(header):
    header.visit()
    header.login_button_should_be_visible()


def test_become_a_tutor_button_is_visible(header):
    header.visit()
    header.become_a_tutor_button_should_be_visible()


@pytest.mark.skip("Need to be fixed")
def test_see_list_of_tutors_profiles(header, find_tutor):
    header.visit()
    header.find_a_tutor_button_should_be_visible()
    header.click_find_tutor_button()
    find_tutor.check_list_of_tutors_is_opened()
    find_tutor.check_picture_of_tutor_is_visible()
    find_tutor.check_name_of_tutor_is_visible()
    find_tutor.check_subject_of_tutor_is_visible()
    find_tutor.check_price_is_visible()


def test_login_button_is_enabled(header):
    header.visit()
    header.login_button_is_enabled()


def test_statistics_button_is_visible(header, register):
    register.registration_as_tutor(header, register)
    header.statistics_button_is_visible()


def test_verify_redirection_on_statistics_page(login, header, register):
    register.registration_as_tutor(header, register)
    header.statistics_button_is_visible()
    header.click_statistics_button()


# TC_11.004.001.001 | Header - Teacher > "Выйти" - button is not available when user don't logined
def test_header_logout_is_absent(header):
    """
    Проверяем отсутствие в хеадер кнопки "Выход" для незарегистрированного пользователя
    """
    header.visit()
    header.check_logout_is_absent()


# TC_11.006.003 [Teacher] Header > My students(button) > "Мои студенты" button is not available when logged out
def test_my_students_btn_is_not_visible_for_guests(header, homepage):
    homepage.visit()
    assert header.my_students_button_is_hidden() is True


# TC_11.006.005 [Teacher] Header > My students(button) > "Мои студенты" button is not available for students
def test_my_students_btn_is_not_visible_for_students(register, header, homepage):
    header.visit()
    header.click_registration_button()
    register.select_role(is_teacher=None)
    register.registration_new_user(user_type='student')
    assert header.my_students_button_is_hidden() is True


# TC_11.006.004 [Teacher] Header > My students(button) > "Мои студенты" button is not available when no announcement is created
def test_my_students_btn_is_not_visible_for_teacher_with_no_announcement(register, header, homepage):
    header.visit()
    header.click_registration_button()
    register.select_role(is_teacher=True)
    register.registration_new_user(user_type='tutor')
    assert header.my_students_button_is_hidden() is True


def test_filter_tutor_by_category(header, find_tutor):
    header.visit()
    header.click_find_tutor_button()
    find_tutor.check_filter_form()

#TC_02.001.001.002 | Guest-Header > Sign in(button) > Verify background color of the button "Войти" is changed while hovering
def test_login_button_change_color_on_hover(header):
    header.visit()
    header.hover_login_button_color_check()
