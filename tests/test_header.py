import pytest

def test_login_button_opens_login_page(header, login):
    header.visit()
    header.click_on_login_button()
    login.check_url_login_page("/login")

