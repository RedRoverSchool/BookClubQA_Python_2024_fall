import allure


def test_visible_cookie_banner(cookie_banner):
    cookie_banner.open_main_page()
    cookie_banner.cookie_banner_should_be_visible()


def test_visible_button_accept(cookie_banner):
    cookie_banner.open_main_page()
    cookie_banner.cookie_button_should_be_visible()


def test_enable_button_accept(cookie_banner):
    cookie_banner.open_main_page()
    cookie_banner.cookie_button_should_be_enable()


def test_cookie_text_matches(cookie_banner):
    cookie_banner.open_main_page()
    cookie_banner.cookie_text_matches()


def test_cookie_banner_disappeared(cookie_banner):
    cookie_banner.open_main_page()
    cookie_banner.click_accept_button()
    cookie_banner.cookie_banner_is_missing()


def test_cookie_banner_does_not_appear_when_reopening(cookie_banner):
    cookie_banner.open_main_page()
    cookie_banner.click_accept_button()
    cookie_banner.banner_does_not_reappear()


@allure.title("TC_51.001.002.001")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/422")
def test_the_functionality_of_the_reject_cookie(cookie_banner):
    cookie_banner.open_main_page()
    cookie_banner.wait_for_reject_cookie_button()
    cookie_banner.click_reject_cookie_button()
    cookie_banner.verify_ym_cookies_are_missing()
