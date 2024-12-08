from playwright.sync_api import Page, expect
from components.header_student import HeaderStudentPage
from components.header import Header
from components.find_tutor import FindTutor


def login_as_student(page: Page):
    """Авторизация под Student."""
    page.goto("http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/login/")
    page.locator('(//a[@class="btn btn-outline-light mb-2 me-2 ms-3"])[1]').click()
    page.fill("input[name='username']", "Yuliya")
    page.fill("input[name='password']", "sdjflsfdjlksdjflksdjf")
    page.click("button[type='submit']")
    expect(page.locator('text="Выйти"')).to_be_visible()


def test_my_teachers_btn_exists(header, page: Page):
    """Проверка наличия кнопки 'Мои репетиторы'."""
    login_as_student(page)  # Выполняем авторизацию
    my_teachers_button = HeaderStudentPage(page)
    header.visit()
    my_teachers_button.check_my_teachers_btn_exists()


def test_my_teachers_btn_click(header, page: Page):
    """Проверка клика на кнопку 'Мои репетиторы'."""
    login_as_student(page)
    my_teachers_button = HeaderStudentPage(page)
    header.visit()
    my_teachers_button.click_my_teachers_btn()
    my_teachers_button.verify_page_my_teachers_opened()

