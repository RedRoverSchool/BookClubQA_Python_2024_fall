

def test_my_students_btn_visibility(login, teacher_profile):
    login.open_login_page()
    login.full_login("teacher@yopmail.com", "iamateacher123")
    assert teacher_profile.is_my_students_button_visible, "The 'Мои студенты' button is not found"




