import allure
import pytest


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_visible_cookie_banner(cookie_banner):
    cookie_banner.open_main_page()
    cookie_banner.cookie_banner_should_be_visible()


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_visible_button_accept(cookie_banner):
    cookie_banner.open_main_page()
    cookie_banner.cookie_button_should_be_visible()


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_enable_button_accept(cookie_banner):
    cookie_banner.open_main_page()
    cookie_banner.cookie_button_should_be_enable()


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_cookie_text_matches(cookie_banner):
    cookie_banner.open_main_page()
    cookie_banner.cookie_text_matches()


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_cookie_banner_disappeared(cookie_banner):
    cookie_banner.open_main_page()
    cookie_banner.click_accept_button()
    cookie_banner.cookie_banner_is_missing()


@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_cookie_banner_does_not_appear_when_reopening(cookie_banner):
    cookie_banner.open_main_page()
    cookie_banner.click_accept_button()
    cookie_banner.banner_does_not_reappear()


@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/422")
@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_the_functionality_of_the_reject_cookie(cookie_banner):
    cookie_banner.open_main_page()
    cookie_banner.wait_for_reject_cookie_button()
    cookie_banner.click_reject_cookie_button()
    cookie_banner.verify_ym_cookies_are_missing()
