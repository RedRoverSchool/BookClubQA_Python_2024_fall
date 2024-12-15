import pytest

from Data.data import valid_login, valid_password


def test_login_button_opens_login_page(header, login):
    header.visit()
    header.click_on_login_button()
    login.check_url_login_page("/login")


def test_verify_registration_options_on_registration_page(header, register):
    header.visit()
    header.click_on_registration_button()
    register.header_should_contain_text("Регистрация")


def test_verify_registration_options_on_login_page(header, login):
    header.visit()
    header.click_on_login_button()
    login.check_title_of_registration()


def test_verify_registration_options_on_find_tutor_page(header, find_tutor):
    header.visit()
    header.click_on_find_tutor_button()
    find_tutor.check_title_of_registration()


def test_support_visibility_as_teacher(login, header):
    header.visit()
    header.click_on_login_button()
    login.full_login("teacher_test", "a.9QA{!@HDB;en2")
    header.support_button_should_be_visible()


def test_support_clickability_as_teacher(login, header):
    header.visit()
    header.click_on_login_button()
    login.full_login("teacher_test", "a.9QA{!@HDB;en2")
    header.click_on_support_button()


def test_support_visibility_as_student(login, header):
    header.visit()
    header.click_on_login_button()
    login.full_login("student_test", "]<c%ZTHH8EZ3L–+")
    header.support_button_should_be_visible()


def test_support_clickability_as_student(login, header):
    header.visit()
    header.click_on_login_button()
    login.full_login("student_test", "]<c%ZTHH8EZ3L–+")
    header.click_on_support_button()


def test_hover_support_button_as_student(login, header):
    header.visit()
    header.click_on_login_button()
    login.full_login("student_test", "]<c%ZTHH8EZ3L–+")
    header.hover_support_button_color_check()



@pytest.mark.skip("Need fix this test")
def test_verify_redirection_on_profile_page(login, header):
    header.visit()
    header.click_on_login_button()
    login.enter_username(valid_login)
    login.enter_password(valid_password)
    login.click_login_button()
    header.click_on_profile_button()



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
    header.click_on_find_tutor_button()
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
    header.click_on_statistics_button()
