import allure
import pytest
from Data.data import EMAIL_TUTOR_KM, PASSWORD_TUTOR_KM, EMAIL_TUTOR_WA_KM, PASSWORD_TUTOR_WA_KM, EMAIL_TUTOR_MV, PASSWORD_TUTOR_MV


# TC_12.002.001| [Teacher] Create announcement > Create teacher announcement.
# Verify the announcement is created after filling in all form fields with valid data#163
@pytest.mark.skip(
    reason="Тест был признан неактуальным из-за обновления процесса регистрации, внедренного 09.01.2025."
)
def test_create_announcement(header, announcement, login):
    header.visit()
    login.full_login(EMAIL_TUTOR_KM, PASSWORD_TUTOR_KM)
    header.click_create_announcement_btn()
    announcement.create_announcement()
    announcement.verify_announcements_page_endpoint()


@allure.label(
    "TC_12.003.002|[Teacher] Verify the announcement is not created when the empty form is submitted"
)
def test_teacher_announcement_blank_form_same_endpoint(
    header, login, create_announcement_page, announcement
):
    header.visit()
    login.full_login(EMAIL_TUTOR_WA_KM, PASSWORD_TUTOR_WA_KM)
    header.click_create_announcement_button()
    create_announcement_page.click_finalize_announcement_button()
    announcement.verify_required_fields_are_not_filled()
    create_announcement_page.verify_create_announcement_page_endpoint()


# TC_12.001.005 | [Teacher] Create announcement > Create teacher announcement >
# Verify the number of announcements remains zero when an empty form is submitted
def test_teacher_announcement_blank_form(
    header, login, create_announcement_page, announcement
):
    header.visit()
    login.full_login("zpak7760@gmail.com", "q4fLncSv9Lgx")
    header.click_create_announcement_button()
    create_announcement_page.click_finalize_announcement_button()
    announcement.navigate_to_users_announcement_list()
    announcement.verify_number_of_announcements_is_zero()


# TC_13.001.005 | [Teacher]My_announcement > Verify the ability to hide the ad from students
def test_teacher_hiding_announcement(header, login, announcement, footer):
    header.visit()
    header.click_login_button()
    login.full_login(EMAIL_TUTOR_MV, PASSWORD_TUTOR_MV)
    announcement.click_my_announcement_button()
    announcement.click_make_announcement_invisible()
    announcement.verify_announcement_hiding(footer, header, announcement)
    header.click_my_announcement_button()
    announcement.click_make_announcement_visible()


# TC_15.001.002 | Header-Teacher > My announcements ("Мои объявления") when User has an announcement >
# Verify the teacher's name in the announcement
@pytest.mark.skip(reason="не прошёл CI после изменений 26.12.2024")
def test_teacher_announcement_name(
    header, register, my_teachers, create_announcement_page, announcement
):
    header.visit()
    header.click_registration_button()
    register.registration_new_user("tutor")
    header.click_create_announcement_button()
    announcement_detail = create_announcement_page.fill_submit_new_announcement_form()
    tutor_name = announcement_detail["fio_value"]
    header.click_my_announcement_button()
    announcement.verify_announcement_tutor_name(tutor_name)


# TC_13.001.001 | [Teacher]My_announcement > "Просмотреть" button redirection check
def test_view_announcement_btn_redirection(header, announcement, login):
    header.visit()
    login.full_login(EMAIL_TUTOR_MV, PASSWORD_TUTOR_MV)
    announcement.click_my_announcement_button()
    announcement.click_view_announcement_button()
    announcement.check_announcement_url_by_template()


# TC_13.001.003 | [Teacher]My_announcement > "Редактировать" button redirection check
def test_edit_announcement_btn_redirection(header, announcement, login):
    header.visit()
    login.full_login(EMAIL_TUTOR_MV, PASSWORD_TUTOR_MV)
    announcement.click_my_announcement_button()
    announcement.click_edit_announcement_button()
    announcement.check_edit_announcement_page_url()


# TC_13.001.004 | [Teacher]My_announcement > Verify the ability to see detailed ad statistics
def test_announcement_detailed_info(header, announcement, login):
    header.visit()
    login.full_login(EMAIL_TUTOR_MV, PASSWORD_TUTOR_MV)
    announcement.click_my_announcement_button()
    announcement.check_view_counter_visible()


# TC_13.005.002 | [Teacher] My announcements > Hiding announcement >
# Verify the teacher is able  to the page "Мое объявление"#299"
def test_redirection_to_my_announcement_page(header, announcement, login):
    header.visit()
    login.full_login("zayatest55@gmail.com", "RM7tAgSYSh7X")
    announcement.click_my_announcement_button()


# TC_12.002.003 | [Teacher] Create announcement > Create teacher announcement >
# Verify the announcement is created after filling in required form fields with valid data #313
@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")
def test_create_announcement_with_only_required_fields(header, announcement, register):
    # email, password = user_registration_cleanup
    header.visit()
    header.click_registration_button()
    register.registration_new_user("tutor")
    header.click_create_announcement_btn()
    announcement.create_announcement_with_only_required_fields()
    announcement.verify_announcements_page_endpoint()


# TC_13.002.001| [Teacher] My announcement > Edit announcement > Mandatory fields are marked with "*"
def test_mandatory_field_marks_on_edit_announcement_page(header, login, announcement):
    header.visit()
    login.full_login(EMAIL_TUTOR_MV, PASSWORD_TUTOR_MV)
    announcement.click_my_announcement_button()
    announcement.click_edit_announcement_button()
    announcement.verify_mandatory_fields_are_marked()


# TC_13.007.002| [Teacher] My announcement > Edit announcement > Mandatory fields are required to be filled
def test_mandatory_fields_on_edit_announcement_page(header, login, announcement):
    header.visit()
    login.full_login(EMAIL_TUTOR_MV, PASSWORD_TUTOR_MV)
    announcement.click_my_announcement_button()
    announcement.click_edit_announcement_button()
    announcement.clear_mandatory_fields()
    announcement.verify_mandatory_field_error_messages()
