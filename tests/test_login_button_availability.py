import allure
import pytest


def test_login_button_present_and_enabled_when_not_logged_in(homepage):
       """
       Verify that the "Войти" button is present and enabled in the header when a user is not logged in.
       """
       homepage.visit()
       # Use the new method from homepage.py
       homepage.check_login_button()