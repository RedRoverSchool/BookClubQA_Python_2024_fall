import allure
import pytest
from core.settings import pages_urls_for_guest
from core.settings import site_pages_urls
from playwright.sync_api import Page
from Data import data


@allure.label("test_case_id", "TC_02.001.001.004")
def test_login_button_opens_login_page(header, login):
    header.visit()
    header.click_login_button()
    login.check_url_login_page("/login")


@allure.label("test_case_id", "TC_02.002.001.001")
def test_verify_registration_options_on_registration_page(header, register):
    header.visit()
    header.click_registration_button()
    register.register_page_contains_register_btn()


def test_verify_registration_options_on_login_page(header, login):
    header.visit()
    header.click_login_button()
    login.check_title_of_registration()


def test_verify_registration_options_on_find_tutor_page(header, find_tutor):
    header.visit()
    header.click_find_tutor_button()
    find_tutor.check_title_of_registration()


@allure.label("test_case_id", "TC_11.003.001.001")
def test_support_visibility_as_teacher(login, header):
    header.visit()
    login.full_login("teacher-test@gmail.com", "Auah7bD2hS5Si7H")
    header.support_button_should_be_visible()


@allure.label("test_case_id", "TC_11.003.001.002")
def test_support_clickability_as_teacher(header, login):
    header.visit()
    login.full_login(data.EMAIL_TUTOR_KM, data.PASSWORD_TUTOR_KM)
    header.click_support_button()


def test_support_visibility_as_student(login, header):
    header.visit()
    login.full_login("teststudent12345@yahoo.com", "!!test!!123")
    header.support_button_should_be_visible()


def test_support_clickability_as_student(login, header):
    header.visit()
    login.full_login("student849727@gmail.com", "xaD1n0tUfaHN")
    header.click_support_button()


def test_hover_support_button_as_student(login, header):
    header.visit()
    login.full_login("student849727@gmail.com", "xaD1n0tUfaHN")
    header.hover_support_button_color_check()


def test_verify_redirection_on_profile_page(login, header):
    header.visit()
    login.full_login("zayatest55@gmail.com", "RM7tAgSYSh7X")
    header.click_profile_button()
    header.profile_button_should_be_visible()


def test_login_button_is_visible(header):
    header.visit()
    header.login_button_should_be_visible()


def test_become_a_tutor_button_is_visible(header):
    header.visit()
    header.become_a_tutor_button_is_visible()


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
def test_my_students_btn_is_not_visible_for_students(login, header):
    header.visit()
    login.full_login("acc.python.test@gmail.com", "jUvJ5ZSxzdIr")
    assert header.my_students_button_is_hidden() is True


# TC_11.006.004 [Teacher] Header > My students(button) >
# "Мои студенты" button is not available when no announcement is created
def test_my_students_btn_is_not_visible_for_teacher_with_no_announcement(login, header):
    header.visit()
    login.full_login("zpak7760@gmail.com", "q4fLncSv9Lgx")
    assert header.my_students_button_is_hidden() is True


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_filter_tutor_by_category(header, find_tutor):
    header.visit()
    header.click_find_tutor_button()
    find_tutor.open_filter_widget()
    find_tutor.check_filter_form()


# TC_02.001.001.002 | Guest-Header > Sign in(button) >
# Verify background color of the button "Войти" is changed while hovering
def test_login_button_change_color_on_hover(header):
    header.visit()
    header.hover_login_button_color_check()


# TC_02.006.001.001 | Guest - Header > "Мыслеплав" button redirects to the Home page >
# "Мыслеплав" button (Home button) in the header is visible
def test_header_home_btn_is_visible_on_all_pages_for_guest(header):
    # Iterate through all the urls available for Guest
    for page_url in pages_urls_for_guest:
        header.page.goto(page_url)
        home_btn = header.header_home_btn_is_present()

        assert home_btn.is_visible(), (
            f"Home button is not visible on the page with url {page_url}"
        )


# TC_31.002.001.001 Header-Student > Sign out > Visibility "Выйти" button


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_exit_button_is_visible_for_student(header, register):
    header.visit()
    header.click_registration_button()
    register.registration_new_user("student")
    assert header.check_exit_btn_exists_for_student()


# TC_31.002.001.002 Header-Student > Sign out > Clickability "Выйти" button


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_exit_button_is_clickable_for_student(header, register):
    header.visit()
    header.click_registration_button()
    register.registration_new_user("student")
    assert header.check_exit_btn_exists_for_student()
    header.click_exit_btn_for_student()


# TC_31.002.001.003 Header-Student > Sign out > Hover Effect on the "Выйти" button


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_hover_exit_button_for_student_color_check(header, register):
    header.visit()
    header.click_registration_button()
    register.registration_new_user("student")
    header.hover_exit_button_for_student_color_check()


@pytest.mark.parametrize(
    "data", site_pages_urls, ids=[u["name"] for u in site_pages_urls]
)
# TC_11.002.01.001 | [Teacher ] Header > "Профиль" button > Visibility check
def test_profile_btn_visibility(header, login, data, page: Page):
    """Проверка видимости кнопки 'Профиль'"""
    header.visit()
    login.full_login("teacher-test@yopmail.com", "5uR94zLhF80r")
    page_url = data["url"]
    page.goto(page_url)
    header.profile_button_should_be_visible()


@pytest.mark.parametrize(
    "data", site_pages_urls, ids=[u["name"] for u in site_pages_urls]
)
# TC_11.002.01.002 | [Teacher ] Header > "Профиль" button > Hover support check
def test_profile_btn_hover(header, login, data, page: Page):
    """Проверка смены цвета кнопки 'Профиль' при наведении на нее курсора"""
    header.visit()
    login.full_login("teacher-test@yopmail.com", "5uR94zLhF80r")
    page_url = data["url"]
    page.goto(page_url)
    header.hover_profile_btn_color_check()


@pytest.mark.parametrize(
    "data", site_pages_urls, ids=[u["name"] for u in site_pages_urls]
)
# TC_11.002.01.003 | [Teacher ] Header > "Профиль" button > Redirection check
def test_profile_btn_redirection(header, user_profile, login, data, page: Page):
    """Проверка перенаправления на страницу профиля пользователя после нажатия кнопки 'Профиль'"""
    header.visit()
    login.full_login("teacher-test@yopmail.com", "5uR94zLhF80r")
    page_url = data["url"]
    page.goto(page_url)
    header.click_profile_button()
    user_profile.profile_btn_redirection_check()


# TC_31.003.001.001 | [Student ] Header > My Tutor(button) > Visibility check #326
def test_my_tutor_btn_visibility_as_student(login, header):
    header.visit()
    login.full_login("acc.python.test@gmail.com", "jUvJ5ZSxzdIr")
    header.student_my_tutors_button_is_visible()


# TC_31.003.001.003 | [Student ] Header > My Tutor(button) > Visibility check #326
def test_my_tutor_btn_clickable_redirection_as_student(login, header):
    header.visit()
    login.full_login("acc.python.test@gmail.com", "jUvJ5ZSxzdIr")
    header.student_my_tutors_button_clickable_redirect()


# TC_31.004.001.001 | [Student ] Header > Find Teacher(button) > Visibility check #321
def test_find_tutor_btn_visibility_as_student(login, header):
    header.visit()
    login.full_login("acc.python.test@gmail.com", "jUvJ5ZSxzdIr")
    header.student_find_tutor_button_is_visible()


# TC_31.004.001.003 | [Student ] Header > Find Teacher(button) > Visibility check #321
def test_find_tutor_btn_clickable_redirection_as_student(login, header):
    header.visit()
    login.full_login("acc.python.test@gmail.com", "jUvJ5ZSxzdIr")
    header.student_find_tutor_button_clickable_redirect()
