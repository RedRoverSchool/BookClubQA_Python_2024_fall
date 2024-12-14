from faker import Faker

fake = Faker()


def test_create_announcement(login, header, announcement, register):
    register.registration_as_tutor(header, register)
    header.click_on_create_announcement_btn()
    announcement.fill_out_fullname()
    announcement.fill_out_descripption()
    announcement.upload_photo()
    announcement.pick_category()
    announcement.fill_out_experience()
    announcement.checkbox_degree()
    announcement.checkbox_free_first_lesson()
    announcement.fill_out_price()
    announcement.fill_out_class_duration()
    announcement.add_contact_info()
    announcement.click_create_announcement_btn()

# AT_12.001.004 | [Teacher] Create announcement > Create teacher announcement > Verify the announcement is not created when the empty form is submitted
def test_teacher_announcement_blank_form_same_endpoint(header, register, my_teachers, create_announcement_page):
    header.visit()
    header.click_on_registration_button()

    register.fill_nick(fake.user_name())
    register.generate_valid_password()
    register.click_on_become_a_teacher_button()
    register.fill_password(register.password)
    register.fill_confirm_password(register.password)
    register.click_on_registration_button()

    header.click_create_announcement_button()

    create_announcement_page.verify_the_announcement_form_is_blank()
    create_announcement_page.click_finalize_announcement_button()
    create_announcement_page.verify_create_announcement_page_endpoint()

# TC_12.001.005 | [Teacher] Create announcement > Create teacher announcement > Verify the number of announcements remains zero when an empty form is submitted
def test_teacher_announcement_blank_form(header, register, my_teachers, create_announcement_page, announcement):
    header.visit()
    header.click_on_registration_button()

    register.fill_nick(fake.user_name())
    register.generate_valid_password()
    register.click_on_become_a_teacher_button()
    register.fill_password(register.password)
    register.fill_confirm_password(register.password)
    register.click_on_registration_button()

    header.click_create_announcement_button()

    create_announcement_page.verify_the_announcement_form_is_blank()
    create_announcement_page.click_finalize_announcement_button()
    announcement.navigate_to_users_announcement_list()
    announcement.verify_number_of_announcements_is_zero()
