import pytest

def test_homepage_info_is_same_after_reload(homepage, register):
    homepage.visit()
    main_page_info_before_reload = homepage.check_info_main_page()
    homepage.reload()
    main_page_info_after_reload = homepage.check_info_main_page()
    assert main_page_info_after_reload == main_page_info_before_reload


def test_homepage_info(homepage, register):
    homepage.visit()
    homepage.check_info_welcome_container()
    homepage.check_2_find_tutor_btns()
    homepage.check_2_become_tutor_btns()
    homepage.check_why_students_choose_us_title()
    homepage.check_find_tutor_card_visible()
    homepage.check_regular_funds_in_ad_for_new_tutors_card_visible()
    homepage.check_professional_tools_for_finding_card_visible()
    homepage.check_2_more_btns()
    homepage.check_why_tutors_choose_us_title()
    homepage.check_not_take_interest_for_lesson_card_visible()
    homepage.check_regular_funds_in_ad_for_new_students_card_visible()
    homepage.check_professional_tools_for_collaboration_card_visible()


@pytest.mark.skip(
    reason="не прошёл CI после изменений 16.12.2024. Ругается на teardown теста"
)
def test_more_btn_redirects_telegram_page_for_students(homepage, telegram_page):
    homepage.visit()
    homepage.click_more_button_at_the_top()
    telegram_page.students_info_should_be_opened()
    telegram_page.check_telegram_channel_should_have_title_for_students()


# @pytest.mark.skip(reason="не прошёл CI после изменений 16.12.2024. ")
def test_more_btn_redirects_telegram_page_for_tutors(homepage, telegram_page):
    # """
    # CI Ругается на ERROR tests/test_homepage.py::test_more_btn_redirects_telegram_page_for_tutors[chromium] -
    # playwright._impl._errors.TimeoutError: Page.screenshot: Timeout 30000ms exceeded.
    #
    # """
    homepage.visit()
    homepage.click_more_button_at_the_bottom()
    telegram_page.tutors_info_should_be_opened()
    telegram_page.check_telegram_channel_should_have_title_for_tutors()


def test_first_btn_become_a_tutor_is_visible(homepage):
    homepage.visit()
    homepage.first_btn_become_a_tutor_is_visible()


def test_first_btn_become_tutor_is_enabled(homepage):
    homepage.visit()
    homepage.find_first_btn_become_tutor()


def test_find_tutor_btn_redirection(homepage):
    homepage.visit()
    url = homepage.check_find_tutor_btn_redirection()
    assert (
        url
        == "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/listings/list/"
    )


def test_find_tutor_btn_2_redirection(homepage):
    homepage.visit()
    url = homepage.check_find_tutor_btn_2_redirection()
    assert (
        url
        == "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/listings/list/"
    )

def test_find_tutor_button_visibility_as_student(homepage, header, register, login):
    homepage.visit()
    header.click_registration_button()
    register.registration_new_user('student')
    homepage.visit()
    homepage.find_tutor_button_should_be_visible()
