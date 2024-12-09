from playwright.sync_api import Page
from components.login import Login
from components.my_teachers import MyTeachersPage

#TC_32.001.001.001 | Student > My teachers> Viewing My Teachers List > Navigate to the "My Teachers" Page

def test_my_teachers_btn_exists(header, page: Page):
    """Проверка наличия кнопки 'Мои репетиторы'."""
    header.visit()
    header.click_on_login_button()
    login_page = Login(page)
    login_page.full_login("Yuliya", "sdjflsfdjlksdjflksdjf")   #пока так логинюсь
    my_teachers_button = MyTeachersPage(page)
    my_teachers_button.check_my_teachers_btn_exists()


def test_my_teachers_btn_click(header, page: Page):
    """Проверка клика на кнопку 'Мои репетиторы'."""
    header.visit()
    header.click_on_login_button()
    login_page = Login(page)
    login_page.full_login("Yuliya", "sdjflsfdjlksdjflksdjf")
    my_teachers_button = MyTeachersPage(page)
    my_teachers_button.click_my_teachers_btn()
    my_teachers_button.verify_page_my_teachers_opened()
    my_teachers_button.check_teachers_list()

