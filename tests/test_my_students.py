import allure


@allure.title("TC_16.001.001.001")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/446")
# TC_16.001.001 | Header - Teacher > "Мои студенты" - verify block should empty, when any students
def test_check_blank_message_my_students(header, my_students, login):
    header.visit()
    login.full_login("af4d2bd02d@emailawb.pro", "wlA16ukwpB0E")
    # Используется логин преподавателя не имеющего студентов
    my_students.visit()
    my_students.check_no_students_message()
