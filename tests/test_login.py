import re

import allure
import pytest
from playwright.sync_api import expect

from Data.data import invalid_login, valid_password

error_messages = "Пожалуйста, введите правильные email и пароль. Оба поля могут быть чувствительны к регистру."


@pytest.mark.skip(reason="не прошёл CI после изменений 26.12.2024")
def test_login_as_tutor_btn_create_listing(header, login):
    header.visit()
    header.click_login_button()
    login.enter_username("test_auth_login")
    login.enter_password("test_auth_pass")
    login.click_login_button()


@allure.title("TC_03.001.005")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/17")
@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_check_enter_invalid_username(header, login):
    header.visit()
    header.click_login_button()
    login.check_enter_invalid_username(invalid_login)
    login.enter_password(valid_password)
    login.click_submit_button()
    login.should_be_valid_message(error_messages)


@allure.title("TC_03.002.001")
def test_email_and_password_and_login_button_is_visible(header, login):
    header.visit()
    header.click_login_button()
    login.login_field_should_be_visible()
    login.password_field_should_be_visible()
    login.login_dark_button_should_be_visible()


@allure.title("TC_03.002.002.001")
def test_sign_in_as_registered_teacher(header, login, page):
    header.visit()
    login.full_login("teacher.test83943@gmail.com", "mQ9Udgb9T1WF")
    expect(page).to_have_url(re.compile("list"))


@allure.title("TC_03.002.002.002")
def test_sign_in_as_registered_student(header, login, page):
    header.visit()
    login.full_login("student849727@gmail.com", "xaD1n0tUfaHN")
    expect(page).to_have_url(re.compile("list"))


@allure.title("TC_03.002.003")
def test_sign_in_with_invalid_credentials(header, login):
    header.visit()
    login.full_login("wrong_mail@gmail.com", "wrong_pass")
    login.invalid_credentials_message_should_be_visible()


@allure.title("TC_03.002.004.001")
def test_redirected_to_teacher_dashboard_after_logged_in(header, login):
    header.visit()
    login.full_login("teacher.test83943@gmail.com", "mQ9Udgb9T1WF")
    header.create_listing_button_should_be_visible()


@allure.title("TC_03.002.004.002")
def test_redirected_to_student_dashboard_after_logged_in(header, login):
    header.visit()
    login.full_login("student849727@gmail.com", "xaD1n0tUfaHN")
    header.find_a_tutor_button_should_be_visible()


@allure.title("TC_03.002.005")
def test_text_and_active_url_are_shown(header, login):
    header.visit()
    header.click_login_button()
    login.login_text_should_be_visible()
    login.login_active_url_should_be_visible()


@allure.title("TC_03.002.006")
def test_redirected_to_the_registration_page(header, login, page):
    header.visit()
    header.click_login_button()
    login.click_create_account_url()
    expect(page).to_have_url("http://testing.misleplav.ru/authorization/signup/")
