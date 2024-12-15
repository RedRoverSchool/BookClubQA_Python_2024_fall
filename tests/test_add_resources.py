from operator import itemgetter
from faker import Faker

fake = Faker()


def test_add_resources(
        homepage,
        header,
        login,
        register,
        create_announcement_page,
        my_students_page,
        teacher_profile_page,
        workspace,
        add_edit_resources_page
):
    homepage.visit()
    header.click_on_registration_button()
    tutor_email, tutor_password = itemgetter('email', 'password')(register.registration_new_user('tutor'))
    header.click_create_announcement_button()
    create_announcement_page.fill_new_announcement_form()
    header.click_my_students_button()
    my_students_page.click_generate_invite_button()
    # invite_link = my_students_page.get_invite_link()
    header.click_on_profile_button()
    teacher_profile_page.click_teacher_logout_button()
    header.click_on_registration_button()
    student_name, student_password = itemgetter('name', 'password')(register.registration_new_user('student'))
    # workspace.navigate_to_invite_link(invite_link)
    header.click_logout_button()
    header.click_on_login_button()
    login.full_login(tutor_email, tutor_password)
    header.click_my_students_button()
    my_students_page.navigate_to_student_dashboard(student_name)
    workspace.navigate_to_add_resources()
    resource_text = add_edit_resources_page.add_resources()
    workspace.verify_resource_text(resource_text)


def test_intercept(homepage, header, login, create_announcement_page, my_students_page):
    homepage.visit()
    header.click_on_login_button()
    login.enter_username('wwwwwwwwwwww')
    login.enter_password('dsadsadsa')
    login.click_login_button()
    header.click_my_students_button()
    # create_announcement_page.intercept()
    my_students_page.click_generate_invite_button()

