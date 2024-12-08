import allure
import pytest
from components.header import Header
from core.settings import base_url
from conftest import valid_password, valid_login, invalid_login, invalid_password

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

def test_verify_registration_options_on_find_tutor_page(header, find_tutor ):
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

def test_verify_redirection_on_profile_page(login, header):
    header.visit()
    header.click_on_login_button()
    login.full_login("Garry", "Potter1$")
    header.click_on_profile_button()
    header.profile_button_should_be_visible()
    
def test_login_button_is_visible(header):
    header.visit()
    header.login_button_should_be_visible()

def test_become_a_tutor_button_is_visible(header):
    header.visit()
    header.become_a_tutor_button_should_be_visible()




@allure.title("TC_03.001.004 ")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/17")
def test_check_enter_invalid_username(header, login):
    header.visit()
    header.click_on_login_button()
    login.check_enter_invalid_username(invalid_login)
    login.enter_password(valid_password)
    login.click_login_button()
    login.should_be_valid_message("Пожалуйста, введите правильные имя пользователя и пароль. Оба поля могут быть "
                                  "чувствительны к регистру.")