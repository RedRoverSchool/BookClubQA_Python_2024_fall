def test_create_announcement(
    login, header, announcement, register, create_announcement_page
):
    header.visit()
    header.click_registration_button()
    register.registration_new_user("tutor")
    header.click_create_announcement_button()
    create_announcement_page.fill_submit_new_announcement_form()
    announcement.verify_announcements_page_endpoint()


# AT_12.001.004 | [Teacher] Create announcement > Create teacher announcement >
# Verify the announcement is not created when the empty form is submitted
def test_teacher_announcement_blank_form_same_endpoint(
    header, register, my_teachers, create_announcement_page
):
    header.visit()
    header.click_registration_button()
    register.registration_new_user("tutor")
    header.click_create_announcement_button()

    create_announcement_page.verify_the_announcement_form_is_blank()
    create_announcement_page.click_finalize_announcement_button()
    create_announcement_page.verify_create_announcement_page_endpoint()


# TC_12.001.005 | [Teacher] Create announcement > Create teacher announcement >
# Verify the number of announcements remains zero when an empty form is submitted
def test_teacher_announcement_blank_form(
    header, register, my_teachers, create_announcement_page, announcement
):
    header.visit()
    header.click_registration_button()
    register.registration_new_user("tutor")
    header.click_create_announcement_button()

    create_announcement_page.verify_the_announcement_form_is_blank()
    create_announcement_page.click_finalize_announcement_button()
    announcement.navigate_to_users_announcement_list()
    announcement.verify_number_of_announcements_is_zero()
