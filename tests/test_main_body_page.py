

def test_main_page_info_is_same_after_reload(header, main_body, register):
    header.visit()
    main_page_info_before_reload = main_body.check_info_main_page()
    main_body.reload()
    main_page_info_after_reload = main_body.check_info_main_page()
    assert main_page_info_after_reload == main_page_info_before_reload

    
def test_main_body_page(header, main_body, register):
    header.visit()
    main_body.check_info_welcome_container()
    main_body.check_2_find_tutor_btns()
    main_body.check_2_become_tutor_btns()
    main_body.check_why_students_choose_us_title()
    main_body.check_find_tutor_card_visible()
    main_body.check_regular_funds_in_ad_for_new_tutors_card_visible()
    main_body.check_professional_tools_for_finding_card_visible()
    main_body.check_2_more_btns()
    main_body.check_why_tutors_choose_us_title()
    main_body.check_not_take_interest_for_lesson_card_visible()
    main_body.check_regular_funds_in_ad_for_new_students_card_visible()
    main_body.check_professional_tools_for_collaboration_card_visible()

