from core.settings import list_url


def test_homepage_info_is_same_after_reload(homepage, register):
    homepage.visit()
    main_page_info_before_reload = homepage.check_info_main_page()
    homepage.reload()
    main_page_info_after_reload = homepage.check_info_main_page()
    assert main_page_info_after_reload == main_page_info_before_reload


def test_welcome_and_join_now_containers_info_are_visible(homepage):
    homepage.visit()
    homepage.check_info_welcome_container()
    homepage.check_join_now_container()


def test_checking_preferences_for_students_section_info_is_visible(homepage):
    homepage.visit()
    homepage.check_preferences_for_students_title()
    homepage.check_comfortable_finding_of_tutor_card_visible()
    homepage.check_guarantee_of_quality_card_visible()
    homepage.check_organizing_the_studying_card_visible()
    homepage.check_homework_card_visible()


def test_checking_preferences_for_tutors_section_info_is_visible(homepage):
    homepage.visit()
    homepage.check_preferences_for_tutors_title()
    homepage.check_selling_ads_and_security_paymen_card_visible()
    homepage.check_lessons_and_homeworks_management_card_visible()
    homepage.check_statistics_and_analytics_card_visible()
    homepage.check_review_management_card_visible()
    homepage.check_support_and_promotion_card_visible()
    homepage.check_powerful_community_card_visible()


def test_more_btn_redirects_telegram_page_for_students(homepage, telegram_page):
    homepage.visit()
    homepage.click_more_button_at_the_top()
    telegram_page.students_info_should_be_opened()
    telegram_page.check_telegram_channel_should_have_title_for_students()


def test_more_btn_redirects_telegram_page_for_tutors(homepage, telegram_page):
    homepage.visit()
    homepage.click_more_button_at_the_bottom()
    telegram_page.tutors_info_should_be_opened()
    telegram_page.check_telegram_channel_should_have_title_for_tutors()


# TC_00.002.002.001 | Main page (body) - All users > Become a Teacher >
# Verify button "Стать репетитором" is visible below "Добро пожаловать в "Мыслеплав"!" heading #77
def test_first_btn_become_a_tutor_is_visible(homepage):
    homepage.visit()
    homepage.first_btn_become_a_tutor_is_visible()


def test_first_btn_become_tutor_is_enabled(homepage):
    homepage.visit()
    homepage.find_first_btn_become_tutor()


def test_find_tutor_btn_redirection(homepage):
    homepage.visit()
    url = homepage.check_find_tutor_btn_redirection()
    assert url == list_url


def test_find_tutor_btn_2_redirection(homepage):
    homepage.visit()
    url = homepage.check_find_tutor_btn_2_redirection()
    assert url == list_url


def test_find_tutor_button_visibility_as_student(homepage, header, register, login):
    homepage.visit()
    header.click_registration_button()
    register.registration_new_user("student")
    homepage.visit()
    homepage.find_tutor_button_should_be_visible()
