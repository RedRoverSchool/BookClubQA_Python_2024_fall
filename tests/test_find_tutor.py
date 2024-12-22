import allure
from faker import Faker

fake = Faker()


def test_redirect_to_tutors_page_with_0_min_price(find_tutor):
    find_tutor.open_find_tutor_page()
    find_tutor.enter_min_price(0)
    find_tutor.check_filter_btn_is_visible()
    find_tutor.click_filter_button()
    find_tutor.check_prices_over_min_price(0)


@allure.title("TC_05.001.006.002")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/243")
def test_verify_tutors_with_random_min_price_by_keyboard(find_tutor):
    """
    Проверка, что после ввода в поле фильтра "Минимальная цена (от)" рандомного значения с клавиатуры, в списке
    репетиторов отображаются только репетиторы со стоимостью занятия >= установленной минимальной цены
    """
    min_price = find_tutor.set_random_min_price(fake, min_value=1, max_value=1000)

    find_tutor.open_find_tutor_page()
    find_tutor.enter_min_price(min_price)
    find_tutor.click_filter_button()
    find_tutor.check_prices_over_min_price(min_price)

@allure.title("TC_05.001.005.003")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/251")
def test_verify_tutors_after_entered_min_experience(find_tutor):
    """
    Проверка, что после ввода значения в поле "Минимальный опыт преподавания"
    отображаются только репетиторы с опытом преподавания >= указанного значения.
    """
    min_experience = 5

    find_tutor.open_find_tutor_page()
    find_tutor.enter_min_experience(min_experience)
    find_tutor.click_filter_button()
    find_tutor.check_experience_over_min_value(min_experience)


@allure.title("TC_05.001.006.005")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/334")
def test_verify_tutors_not_displayed_with_min_price_more_than_current_tutors_prices(find_tutor):
    """
    Проверка, что после ввода в поле фильтра "Минимальная цена (от)" значения большего, чем текущие цены репетиторов, список
    репетиторов пустой и отображается сообщение "Нет результатов". Учитывается пролистывание списка репетиторов.
    """
    find_tutor.open_find_tutor_page()
    min_price = find_tutor.find_max_tutors_price() + fake.random_int(1, 1000)

    find_tutor.enter_min_price(min_price)
    find_tutor.click_filter_button()
    find_tutor.check_message_no_results_is_visible()
