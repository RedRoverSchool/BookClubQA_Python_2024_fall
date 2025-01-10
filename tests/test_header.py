import pytest
import time


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


def test_support_visibility_as_teacher(login, header):
    header.visit()
    header.click_login_button()
    login.full_login("teacher_test", "a.9QA{!@HDB;en2")
    header.support_button_should_be_visible()


@pytest.mark.skip(reason="не прошёл CI после изменений 16.12.2024")
def test_support_clickability_as_teacher(login, header):
    header.visit()
    header.click_login_button()
    login.full_login("teacher_test", "a.9QA{!@HDB;en2")
    header.click_support_button()


def test_support_visibility_as_student(login, header):
    header.visit()
    header.click_login_button()
    login.full_login("student_test", "]<c%ZTHH8EZ3L–+")
    header.support_button_should_be_visible()


def test_support_clickability_as_student(register, login, header):
    header.visit()
    header.click_registration_button()
    register.registration_new_user("student")
    header.click_support_button()


@pytest.mark.skip(reason="не прошёл CI 17.12.2024")
def test_hover_support_button_as_student(register, login, header):
    header.visit()
    header.click_registration_button()
    register.registration_new_user("student")
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


def test_statistics_button_is_visible(header, login, register):
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


def test_filter_tutor_by_category(header, find_tutor):
    header.visit()
    header.click_find_tutor_button()
    find_tutor.check_filter_form()

# TC_31.003.001.001 | [Student ] Header > My Tutor(button) > Visibility check #326
def test_my_tutor_btn_visibility_as_student(login, header):
    header.visit()
    header.click_login_button()
    login.full_login("timo_s@gmail.com", "Test123$")
    header.student_my_tutors_button_is_visible()

# TC_31.003.001.003 | [Student ] Header > My Tutor(button) > Visibility check #326
def test_my_tutor_btn_clickable_redirection_as_student(login, header):
    header.visit()
    header.click_login_button()
    login.full_login("timo_s@gmail.com", "Test123$")
    header.student_my_tutors_button_clickable_redirect()

# TC_31.004.001.001 | [Student ] Header > Find Teacher(button) > Visibility check #321
def test_find_tutor_btn_visibility_as_student(login, header):
    header.visit()
    header.click_login_button()
    login.full_login("timo_s@gmail.com", "Test123$")
    header.student_find_tutor_button_is_visible()

# TC_31.004.001.003 | [Student ] Header > Find Teacher(button) > Visibility check #321
def test_find_tutor_btn_clickable_redirection_as_student(login, header):
    header.visit()
    header.click_login_button()
    login.full_login("timo_s@gmail.com", "Test123$")
    header.student_find_tutor_button_clickable_redirect()