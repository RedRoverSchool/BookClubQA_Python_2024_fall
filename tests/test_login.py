import allure
from Data.data import *


def test_login_as_tutor_btn_create_listing(header, login):
    login.open_login_page()
    header.click_on_login_button
    login.enter_username("test_auth_login")
    login.enter_password("test_auth_pass")
    login.click_login_button()
    header.create_listing_button_should_be_visible


# @allure.title("TC_03.001.004 ")
# @allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/17")
def test_check_enter_invalid_username(header, login):
    header.visit()
    header.click_on_login_button()
    login.check_enter_invalid_username(invalid_login)
    login.enter_password(valid_password)
    login.click_login_button()
    login.should_be_valid_message("Пожалуйста, введите правильные имя пользователя и пароль. Оба поля могут быть "
                                  "чувствительны к регистру.")
