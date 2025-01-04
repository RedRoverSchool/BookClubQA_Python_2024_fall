import allure


@allure.title("TC_01.001.001.005")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/54")
def test_presence_of_the_privacy_policy(footer):
    footer.open_main_page()
    footer.scroll_down_to_the_footer()
    footer.privacy_policy_url_should_be_visible()


@allure.title("TC_01.001.001.006")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/53")
def test_enabled_privacy_policy_url(footer):
    footer.open_main_page()
    footer.scroll_down_to_the_footer()
    footer.privacy_policy_url_should_be_enabled()


@allure.title("TC_01.001.001.007")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/52")
def test_redirect_privacy_policy_page(footer):
    footer.open_main_page()
    footer.scroll_down_to_the_footer()
    footer.click_privacy_policy_url()
    footer.wait_for_navigation()
    footer.verify_privacy_policy_page()


@allure.title("TC_01.001.001.008")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/51")
def test_availability_of_the_privacy_policy_link_on_find_tutor_page(footer):
    footer.open_find_tutor_page()
    footer.scroll_down_to_the_footer()
    footer.privacy_policy_url_should_be_visible()
    footer.privacy_policy_url_should_be_enabled()


@allure.title("TC_01.001.001.008")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/51")
def test_availability_of_the_privacy_policy_link_on_signup_page(footer):
    footer.open_signup_page()
    footer.scroll_down_to_the_footer()
    footer.privacy_policy_url_should_be_visible()
    footer.privacy_policy_url_should_be_enabled()


@allure.title("TC_01.001.001.008")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/51")
def test_availability_of_the_privacy_policy_link_on_login_page(footer):
    footer.open_login_page()
    footer.scroll_down_to_the_footer()
    footer.privacy_policy_url_should_be_visible()
    footer.privacy_policy_url_should_be_enabled()
