import allure
from faker import Faker

fake = Faker()

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

def test_verify_tutors_after_entered_min_price_by_random(find_tutor):
    find_tutor.open_find_tutor_page()
    find_tutor.add_random_min_price(fake)
    find_tutor.click_filter_button()
    find_tutor.check_prices_over_min_price(fake.random_int(min=1, max=1000))

def test_verify_min_experience_field(find_tutor):
    find_tutor.open_find_tutor_page()
    find_tutor.check_min_exp_field_is_visible()