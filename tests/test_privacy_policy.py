def test_presence_of_the_privacy_policy(footer):
    footer.open_main_page()
    footer.scroll_down_to_the_footer()
    footer.privacy_policy_url_should_be_visible()


# TC_01.001.001.006
def test_enabled_privacy_policy_url(footer):
    footer.open_main_page()
    footer.scroll_down_to_the_footer()
    footer.privacy_policy_url_should_be_enabled()


# TC_01.001.001.007
def test_redirect_privacy_policy_page(footer):
    footer.open_main_page()
    footer.scroll_down_to_the_footer()
    footer.click_privacy_policy_url()
    footer.wait_for_navigation()
    footer.privacy_policy_page_should_contain_text()


# TC_01.001.001.008
def test_availability_of_the_privacy_policy_link_on_find_tutor_page(footer):
    footer.open_find_tutor_page()
    footer.scroll_down_to_the_footer()
    footer.privacy_policy_url_should_be_visible()
    footer.privacy_policy_url_should_be_enabled()


def test_availability_of_the_privacy_policy_link_on_signup_page(footer):
    footer.open_signup_page()
    footer.scroll_down_to_the_footer()
    footer.privacy_policy_url_should_be_visible()
    footer.privacy_policy_url_should_be_enabled()


def test_availability_of_the_privacy_policy_link_on_login_page(footer):
    footer.open_login_page()
    footer.scroll_down_to_the_footer()
    footer.privacy_policy_url_should_be_visible()
    footer.privacy_policy_url_should_be_enabled()
