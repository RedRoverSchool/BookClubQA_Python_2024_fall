from faker import Faker
import pytest

fake = Faker


# TC_01.001.001.005
def test_presence_of_the_privacy_policy(footer):
    footer.open()
    footer.scroll_down_to_the_footer()
    footer.privacy_policy_url_should_be_visible()


# TC_01.001.001.006
def test_enabled_privacy_policy_url(footer):
    footer.open()
    footer.scroll_down_to_the_footer()
    footer.privacy_policy_url_should_be_enabled()


# TC_01.001.001.007
def test_redirect_privacy_policy_page(footer):
    footer.open()
    footer.scroll_down_to_the_footer()
    footer.click_on_privacy_policy_url()
    footer.wait_for_navigation()
    footer.clicking_privacy_policy_url_should_be_redirect_to_policy_page()


# TC_01.001.001.008
def test_availability_of_the_privacy_policy_link_on_different_platform_pages(footer):
    footer.open()
    footer.scroll_down_to_the_footer()
    footer.privacy_policy_url_should_be_visible()
    footer.privacy_policy_url_should_be_enabled()
