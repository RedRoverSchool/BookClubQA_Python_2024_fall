import allure
from faker import Faker

fake = Faker()


@allure.title("TC_05.001.006.002")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/243")
def test_redirect_to_tutors_page_with_0_min_price(find_tutor):
    find_tutor.open_find_tutor_page()
    find_tutor.open_filter_widget()
    find_tutor.enter_min_price(0)
    find_tutor.check_filter_btn_is_visible()
    find_tutor.click_filter_button()
    find_tutor.check_prices_over_min_price(0)


@allure.title("TC_05.001.006.004")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/287")
def test_verify_tutors_with_random_min_price_by_keyboard(find_tutor):
    """
    Проверка, что после ввода в поле фильтра "Минимальная цена (от)" рандомного значения с клавиатуры, в списке
    репетиторов отображаются только репетиторы со стоимостью занятия >= установленной минимальной цены
    """
    min_price = find_tutor.set_random_min_price(fake, min_value=1, max_value=5000)

    find_tutor.open_find_tutor_page()
    find_tutor.open_filter_widget()
    find_tutor.enter_min_price(min_price)
    find_tutor.click_filter_button()
    find_tutor.check_prices_over_min_price(min_price)


@allure.title("TC_05.001.005.001")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/251")
def test_verify_tutors_after_entered_min_experience(find_tutor):
    """
    Проверка, что после ввода значения в поле "Минимальный опыт преподавания"
    отображаются только репетиторы с опытом преподавания >= указанного значения.
    """
    min_experience = 5

    find_tutor.open_find_tutor_page()
    find_tutor.open_filter_widget()
    find_tutor.enter_min_experience(min_experience)
    find_tutor.click_filter_button()
    find_tutor.check_experience_over_min_value(min_experience)


@allure.title("TC_34.001.001.002")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/11")
# TC_34.001.001.002 [Student] Find a teacher > Verify button "Подробнее" in a tutor profile is visible
def test_btn_more_find_tutor_is_visible(login, header, find_tutor):
    header.visit()
    login.full_login("acc.python.test@gmail.com", "jUvJ5ZSxzdIr")
    find_tutor.check_btn_more_is_visible()


@allure.title("TC_34.001.001.003")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/11")
# TC_34.001.001.003 [Student] Find a teacher > Verify button "Подробнее" in a tutor profile clickable and redirectible
def test_btn_more_find_tutor_is_clickable(login, header, find_tutor):
    header.visit()
    login.full_login("acc.python.test@gmail.com", "jUvJ5ZSxzdIr")
    find_tutor.check_btn_more_is_clickable()


@allure.title("TC_34.001.001.004")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/11")
# TC_34.001.001.004 [Student] Find a teacher > Verify button "Подробнее" has each tutor profile
def test_btn_more_find_tutor_has_each_profile(login, header, find_tutor):
    header.visit()
    login.full_login("acc.python.test@gmail.com", "jUvJ5ZSxzdIr")
    find_tutor.check_btn_more_has_each_profile()

@allure.title("TC_37.001.001.001")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/416")
# TC_37.001.001.001 [Student ] Find a teacher > More > Verify tutor profile contains full details
def test_tutor_profile_has_require_details(login, header, find_tutor):
    header.visit()
    login.full_login("acc.python.test@gmail.com", "jUvJ5ZSxzdIr")
    find_tutor.check_btn_more_is_clickable()
    find_tutor.check_tutor_profile_has_require_details()

@allure.title("TC_37.001.001.002")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/416")
# TC_37.001.001.002 [Student ] Find a teacher > More > Verify the tutor profile has the button "Хочу заниматься!"
def test_tutor_profile_has_btn_request_lesson(login, header, find_tutor):
    header.visit()
    login.full_login("acc.python.test@gmail.com", "jUvJ5ZSxzdIr")
    find_tutor.check_btn_more_is_clickable()
    find_tutor.check_tutor_profile_has_btn_request_lesson()

@allure.title("TC_37.001.001.003")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/416")
# TC_37.001.001.003 [Student ] Find a teacher > More > Verify the button "Хочу заниматься!" is clickable and redirectable
def test_tutor_profile_btn_request_lesson_clickable_redirect(login, header, find_tutor):
    header.visit()
    login.full_login("acc.python.test@gmail.com", "jUvJ5ZSxzdIr")
    find_tutor.check_btn_more_is_clickable()
    find_tutor.check_tutor_profile_btn_request_lesson_clickable_redirect()
