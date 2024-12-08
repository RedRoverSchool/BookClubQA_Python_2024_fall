from playwright.sync_api import Page, expect
import allure


class MainBodyPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("check_info_main_page")
    def check_info_main_page(self):
        self.page.get_by_role("main").text_content().split()

    @allure.step("check_info_main_page_before_and_after_reload")
    def reload(self):
        self.page.reload()
        
    @allure.step("Check info in the \"Добро пожаловать\" container")
    def check_info_welcome_container(self):
        welcome_container = self.page.get_by_text("Добро пожаловать в \"Мыслеплав\"! Платформа, соединяющая учеников и "
                                                  "репетиторов, о")
        expect(welcome_container).to_be_visible()
        expected_section_text = """
        Добро пожаловать в "Мыслеплав"!
        Платформа, соединяющая учеников и репетиторов, открывает новые горизонты для обучения.
        
            Найти репетитора
            Найти репетитора
            Стать репетитором
            Стать репетитором
        """
        assert welcome_container.text_content().split() == expected_section_text.split(), \
            (f"Expected text does not match actual text. \n"
             f"Expected: {expected_section_text.split()} \n"
             f"Actual: {welcome_container.text_content().split()}")

    @allure.step("Check 2 \"Найти репетитора\" btns")
    def check_2_find_tutor_btns(self):
        find_tutor_btns = self.page.locator('a.d-none:text("Найти репетитора")').filter().count()
        assert find_tutor_btns == 2

    @allure.step("Check 2 \"Стать репетитором\" btns")
    def check_2_become_tutor_btns(self):
        become_tutor_btns = self.page.locator('a.d-none:text("Стать репетитором")').filter().count()
        assert become_tutor_btns == 2

    @allure.step("Check \"Почему ученики выбирают нас?\" title")
    def check_why_students_choose_us_title(self):
        why_students_choose_us_loc = self.page.get_by_role("heading", name="Почему ученики выбирают нас?")
        expect(why_students_choose_us_loc).to_be_visible()
        expected_title = "Почему ученики выбирают нас?"
        actual_title = why_students_choose_us_loc.text_content()
        assert actual_title == expected_title, \
            (f"Expected text does not match actual text. \n"
             f"Expected: {expected_title} \n"
             f"Actual: {actual_title}")

    @allure.step("Check \"Бесплатный поиск репетиторов\" card is visible")
    def check_find_tutor_card_visible(self):
        free_find_tutor_card = self.page.get_by_text(
            "Бесплатный поиск репетиторов Находим лучших репетиторов без лишних затрат")
        expect(free_find_tutor_card).to_be_visible()
        expected_card_text = """
               Бесплатный поиск репетиторов
                               Находим лучших репетиторов без лишних затрат.
               """
        assert free_find_tutor_card.text_content().split() == expected_card_text.split(), \
            (f"Expected text does not match actual text. \n"
             f"Expected: {expected_card_text.split()} \n"
             f"Actual: {free_find_tutor_card.text_content().split()}")

    @allure.step("Check \"Регулярные вложения в рекламу Привлекаем новых репетиторов\" card is visible")
    def check_regular_funds_in_ad_for_new_tutors_card_visible(self):
        regular_funds_in_ad_card = self.page.get_by_text(
            "Регулярные вложения в рекламу Привлекаем новых репетиторов для вас")
        expect(regular_funds_in_ad_card).to_be_visible()
        expected_card_text = """
                   Регулярные вложения в рекламу Привлекаем новых репетиторов для вас.
                   """
        assert regular_funds_in_ad_card.text_content().split() == expected_card_text.split(), \
            (f"Expected text does not match actual text. \n"
             f"Expected: {expected_card_text.split()} \n"
             f"Actual: {regular_funds_in_ad_card.text_content().split()}")

    @allure.step("Check \"Профессиональные инструменты для поиска\" card is visible")
    def check_professional_tools_for_finding_card_visible(self):
        professional_tools_card = self.page.get_by_text(
            "Профессиональные инструменты для поиска Эффективный поиск подходящего репетитора")
        expect(professional_tools_card).to_be_visible()
        expected_card_text = """
                       Профессиональные инструменты для поиска Эффективный поиск подходящего репетитора.
                       """
        assert professional_tools_card.text_content().split() == expected_card_text.split(), \
            (f"Expected text does not match actual text. \n"
             f"Expected: {expected_card_text.split()} \n"
             f"Actual: {professional_tools_card.text_content().split()}")

    @allure.step("Check \"Регулярные вложения в рекламу Привлекаем новых учеников\" card is visible")
    def check_regular_funds_in_ad_for_new_students_card_visible(self):
        regular_funds_in_ad_for_new_student_card = self.page.get_by_text(
            "Регулярные вложения в рекламу Привлекаем новых учеников для вас")
        expect(regular_funds_in_ad_for_new_student_card).to_be_visible()
        expected_card_text = """
                       Регулярные вложения в рекламу Привлекаем новых учеников для вас.
                       """
        assert regular_funds_in_ad_for_new_student_card.text_content().split() == expected_card_text.split(), \
            (f"Expected text does not match actual text. \n"
             f"Expected: {expected_card_text.split()} \n"
             f"Actual: {regular_funds_in_ad_for_new_student_card.text_content().split()}")

    @allure.step("Check \"Профессиональные инструменты для взаимодействия\" card is visible")
    def check_professional_tools_for_collaboration_card_visible(self):
        professional_tools_for_collaboration_card = self.page.get_by_text(
            "Профессиональные инструменты для взаимодействия Возможность создавать уроки, доб")
        expect(professional_tools_for_collaboration_card).to_be_visible()
        expected_card_text = """
                           Профессиональные инструменты для взаимодействия Возможность создавать уроки, 
                           добавлять домашки и оплаты для ученика.
                           """
        assert professional_tools_for_collaboration_card.text_content().split() == expected_card_text.split(), \
            (f"Expected text does not match actual text. \n"
             f"Expected: {expected_card_text.split()} \n"
             f"Actual: {professional_tools_for_collaboration_card.text_content().split()}")

    @allure.step("Check 2 \"Подробнее\" btns")
    def check_2_more_btns(self):
        more_btn = self.page.get_by_role("link", name="Подробнее").filter().count()
        assert more_btn == 2

    @allure.step("Check \"Почему репетиторы выбирают нас?\" title")
    def check_why_tutors_choose_us_title(self):
        why_tutors_choose_us_loc = self.page.get_by_role("heading", name="Почему репетиторы выбирают нас?")
        expect(why_tutors_choose_us_loc).to_be_visible()
        expected_title = "Почему репетиторы выбирают нас?"
        actual_title = why_tutors_choose_us_loc.text_content()
        assert actual_title == expected_title, \
            (f"Expected text does not match actual text. \n"
             f"Expected:{expected_title} \n"
             f"Actual: {actual_title}")

    @allure.step("Check \"Не берем процент с Ваших занятий\" card is visible")
    def check_not_take_interest_for_lesson_card_visible(self):
        not_take_interest_for_lesson_card = self.page.get_by_text(
            "Не берем процент с Ваших занятий Вы можете бесплатно размещать свои обьявления")
        expect(not_take_interest_for_lesson_card).to_be_visible()
        expected_card_text = """
                           Не берем процент с Ваших занятий Вы можете бесплатно размещать свои обьявления
                           """
        assert not_take_interest_for_lesson_card.text_content().split() == expected_card_text.split(), \
            (f"Expected text does not match actual text. \n"
             f"Expected: {expected_card_text.split()} \n"
             f"Actual: {not_take_interest_for_lesson_card.text_content().split()}")

