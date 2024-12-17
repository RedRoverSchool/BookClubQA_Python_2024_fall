import allure


@allure.title("TC_05.001.006.001")
@allure.link("https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall/issues/173")
def test_min_price_filed_is_presented_on_page(find_tutor):
    find_tutor.open_find_tutor_page
    find_tutor.check_min_price_field_is_visible


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

