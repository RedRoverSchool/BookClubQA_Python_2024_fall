import allure
import time

@allure.title("TC_05.001.006.003")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/249")
def test_verify_tutors_after_entered_min_price_by_keyboard(find_tutor):
    """
    Проверка, что после ввода в поле фильтра "Минимальная цена (от)" значения с клавиатуры, в списке
    репетиторов отображаются только репетиторы со стоимостью занятия >= установленной минимальной цены
    """
    min_price = 120

    find_tutor.open_find_tutor_page()
    find_tutor.enter_min_price(min_price)
    find_tutor.click_filter_button()
    find_tutor.check_prices_over_min_price(min_price)

def test_redirect_to_tutors_page_with_0_min_price(find_tutor):
    find_tutor.open_find_tutor_page()
    find_tutor.enter_min_price(0)
    find_tutor.check_filter_btn_is_visible()
    find_tutor.click_filter_button()
    find_tutor.check_prices_over_min_price(0)

@allure.title("TC_34.001.001.002")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/11")
# TC_34.001.001.002 [Student] Find a teacher > Verify button "Подробнее" in a tutor profile is visible
def test_btn_more_find_tutor_is_visible(login, header, find_tutor):
    header.visit()
    header.click_login_button()
    login.full_login("acc.python.test@gmail.com", "jUvJ5ZSxzdIr")
    header.click_find_tutor_button()
    find_tutor.check_btn_more_is_visible()

@allure.title("TC_34.001.001.003")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/11")
# TC_34.001.001.003 [Student ] Find a teacher > Verify button "Подробнее" in a tutor profile clickable and redirectible 
def test_btn_more_find_tutor_is_clickable(login, header, find_tutor):
    header.visit()
    header.click_login_button()
    login.full_login("acc.python.test@gmail.com", "jUvJ5ZSxzdIr")
    header.click_find_tutor_button()
    find_tutor.check_btn_more_is_clickable()

@allure.title("TC_34.001.001.004")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/11")
# TC_34.001.001.004 [Student ] Find a teacher > Verify button "Подробнее" has each tutor profile
def test_btn_more_find_tutor_has_each_profile(login, header, find_tutor):
    header.visit()
    header.click_login_button()
    login.full_login("acc.python.test@gmail.com", "jUvJ5ZSxzdIr")
    header.click_find_tutor_button()
    find_tutor.check_btn_more_has_each_profile()
