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
