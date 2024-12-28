import allure
from playwright.sync_api import Page, expect
from core.settings import base_url


class Homepage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открываем главную страницу")
    def visit(self):
        self.page.goto(base_url)

    @allure.step("check_info_main_page")
    def check_info_main_page(self):
        self.page.get_by_role("main").text_content().split()

    @allure.step("check_info_main_page_before_and_after_reload")
    def reload(self):
        self.page.reload()

    @allure.step('Check info in the "Добро пожаловать" container')
    def check_info_welcome_container(self):
        welcome_container = self.page.locator("section").filter(has_text="Добро пожаловать в Мыслеплав! "
                                                                         "Откройте новые горизонты обучения с "
                                                                         "нашей платформ")
        welcome_container.wait_for(state="visible", timeout=10000)

        expected_section_text = """
        Добро пожаловать в Мыслеплав!
            Откройте новые горизонты обучения с нашей платформой!
            
                Найти репетитора
                Стать репетитором
        """

        assert (
                welcome_container.text_content().split() == expected_section_text.split()
        ), (
            f"Expected text does not match actual text. \n"
            f"Expected: {expected_section_text.split()} \n"
            f"Actual: {welcome_container.text_content().split()}"
        )

    @allure.step('Click on "Стать репетитором" button')
    def click_become_tutor_btn(self):
        self.page.locator(
            "div[class*='d-sm-flex'] a:text('Стать репетитором')"
        ).first.click()

    @allure.step('Check "Преимущества для учеников" title')
    def check_preferences_for_students_title(self):
        preferences_for_students_loc = self.page.get_by_role("heading", name="Преимущества для учеников")
        preferences_for_students_loc.wait_for(state="visible", timeout=10000)
        expect(preferences_for_students_loc).to_be_visible()
        expected_title = "Преимущества для учеников"
        actual_title = preferences_for_students_loc.text_content()
        assert actual_title == expected_title, (
            f"Expected text does not match actual text. \n"
            f"Expected: {expected_title} \n"
            f"Actual: {actual_title}"
        )

    @allure.step('Check "Удобный поиск репетитора" card is visible')
    def check_comfortable_finding_of_tutor_card_visible(self):
        comfortable_finding_of_tutor_card = self.page.get_by_text(
            "Удобный поиск репетитора Изучайте профили репетиторов без рекламы и необходимост"
        )
        expect(comfortable_finding_of_tutor_card).to_be_visible()
        expected_card_text = """
               Удобный поиск репетитора
                        Изучайте профили репетиторов без рекламы и необходимости регистрации.
               """
        assert (
                comfortable_finding_of_tutor_card.text_content().split() == expected_card_text.split()
        ), (
            f"Expected text does not match actual text. \n"
            f"Expected: {expected_card_text.split()} \n"
            f"Actual: {comfortable_finding_of_tutor_card.text_content().split()}"
        )

    @allure.step(
        'Check "Гарантия качества" card is visible'
    )
    def check_guarantee_of_quality_card_visible(self):
        guarantee_of_quality_card = self.page.get_by_text(
            "Гарантия качества Если занятие по объективным причинам не устроит, вы сможете ве")

        expect(guarantee_of_quality_card).to_be_visible()
        expected_card_text = """
                   Гарантия качества
                        Если занятие по объективным причинам не устроит, вы сможете вернуть свои деньги.
                   """
        assert (
                guarantee_of_quality_card.text_content().split()
                == expected_card_text.split()
        ), (
            f"Expected text does not match actual text. \n"
            f"Expected: {expected_card_text.split()} \n"
            f"Actual: {guarantee_of_quality_card.text_content().split()}"
        )

    @allure.step('Check "Организация обучения" card is visible')
    def check_organizing_the_studying_card_visible(self):
        organizing_the_studying_card = self.page.get_by_text(
            "Организация обучения Просматривайте информацию о занятиях, времени проведения, о"
        )
        expect(organizing_the_studying_card).to_be_visible()
        expected_card_text = """
                       Организация обучения
                        Просматривайте информацию о занятиях, времени проведения, оплатах и дополнительных материалах 
                        в одном месте.
                       """
        assert (
                organizing_the_studying_card.text_content().split() == expected_card_text.split()
        ), (
            f"Expected text does not match actual text. \n"
            f"Expected: {expected_card_text.split()} \n"
            f"Actual: {organizing_the_studying_card.text_content().split()}"
        )

    @allure.step('Check "Домашние задания" card is visible')
    def check_homework_card_visible(self):
        homework_card = self.page.get_by_text(
            "Домашние задания Выполняйте домашние задания с помощью эффективных инструментов ")
        expect(homework_card).to_be_visible()
        expected_card_text = """
                           Домашние задания
                        Выполняйте домашние задания с помощью эффективных инструментов на платформе.
                          """
        assert (
                homework_card.text_content().split() == expected_card_text.split()
        ), (
            f"Expected text does not match actual text. \n"
            f"Expected: {expected_card_text.split()} \n"
            f"Actual: {homework_card.text_content().split()}"
        )

    @allure.step(
        'Check "Управление уроками и домашними заданиями" card is visible'
    )
    def check_lessons_and_homeworks_management_card_visible(self):
        lessons_and_homeworks_management_card = self.page.get_by_text(
            "Управление уроками и домашними заданиями Фиксируйте информацию о занятиях, созда"
        )
        expect(lessons_and_homeworks_management_card).to_be_visible()
        expected_card_text = """
                       Управление уроками и домашними заданиями
                        Фиксируйте информацию о занятиях, создавайте и проверяйте домашние задания.
                       """
        assert (
                lessons_and_homeworks_management_card.text_content().split()
                == expected_card_text.split()
        ), (
            f"Expected text does not match actual text. \n"
            f"Expected: {expected_card_text.split()} \n"
            f"Actual: {lessons_and_homeworks_management_card.text_content().split()}"
        )

    @allure.step(
        'Check "Статистика и аналитика" card is visible'
    )
    def check_statistics_and_analytics_card_visible(self):
        statistics_and_analytics_card = self.page.get_by_text(
            "Статистика и аналитика Отслеживайте просмотры объявлений и общую статистику, что"
        )
        expect(statistics_and_analytics_card).to_be_visible()
        expected_card_text = """
                           Статистика и аналитика
                        Отслеживайте просмотры объявлений и общую статистику, чтобы следить за 
                        эффективностью продвижения.
                           """
        assert (
                statistics_and_analytics_card.text_content().split()
                == expected_card_text.split()
        ), (
            f"Expected text does not match actual text. \n"
            f"Expected: {expected_card_text.split()} \n"
            f"Actual: {statistics_and_analytics_card.text_content().split()}"
        )

    @allure.step(
        'Check "Управление отзывами" card is visible'
    )
    def check_review_management_card_visible(self):
        review_management_card = self.page.get_by_text(
            "Управление отзывами Только ученики, занимавшиеся с вами, могут оставлять отзывы"
        )
        expect(review_management_card).to_be_visible()
        expected_card_text = """
                              Управление отзывами
                        Только ученики, занимавшиеся с вами, могут оставлять отзывы.
                              """
        assert (
                review_management_card.text_content().split()
                == expected_card_text.split()
        ), (
            f"Expected text does not match actual text. \n"
            f"Expected: {expected_card_text.split()} \n"
            f"Actual: {review_management_card.text_content().split()}"
        )

    @allure.step(
        'Check "Поддержка и продвижение" card is visible'
    )
    def check_support_and_promotion_card_visible(self):
        support_and_promotion_card = self.page.get_by_text(
            "Поддержка и продвижение Получайте помощь от менеджеров платформы и рекламируйте "
        )
        expect(support_and_promotion_card).to_be_visible()
        expected_card_text = """
                            Поддержка и продвижение
                        Получайте помощь от менеджеров платформы и рекламируйте себя в социальных сетях.
                                  """
        assert (
                support_and_promotion_card.text_content().split()
                == expected_card_text.split()
        ), (
            f"Expected text does not match actual text. \n"
            f"Expected: {expected_card_text.split()} \n"
            f"Actual: {support_and_promotion_card.text_content().split()}"
        )

    @allure.step(
        'Check "Мощное сообщество" card is visible'
    )
    def check_powerful_community_card_visible(self):
        powerful_community_card = self.page.get_by_text(
            "Мощное сообщество Общайтесь с другими репетиторами и участвуйте в жизни сообщест"
        )
        expect(powerful_community_card).to_be_visible()
        expected_card_text = """
                            Мощное сообщество
                        Общайтесь с другими репетиторами и участвуйте в жизни сообщества.
                                     """
        assert (
                powerful_community_card.text_content().split()
                == expected_card_text.split()
        ), (
            f"Expected text does not match actual text. \n"
            f"Expected: {expected_card_text.split()} \n"
            f"Actual: {powerful_community_card.text_content().split()}"
        )

    @allure.step('Check info in the "Присоединяйтесь сейчас!" container')
    def check_join_now_container(self):
        join_now_container = self.page.locator("section").filter(has_text="Присоединяйтесь сейчас! Откройте новые "
                                                                          "горизонты обучения с нашей платформой! На")
        join_now_container.wait_for(state="visible", timeout=10000)
        expected_section_text = """
            Присоединяйтесь сейчас!
            Откройте новые горизонты обучения с нашей платформой!
            
                Найти репетитора
                Стать репетитором
           """

        assert (
                join_now_container.text_content().split() == expected_section_text.split()
        ), (
            f"Expected text does not match actual text. \n"
            f"Expected: {expected_section_text.split()} \n"
            f"Actual: {join_now_container.text_content().split()}"
        )

    @allure.step('Check "Преимущества для репетиторов" title')
    def check_preferences_for_tutors_title(self):
        preference_for_tutors_loc = self.page.get_by_role(
            "heading", name="Преимущества для репетиторов"
        )
        expect(preference_for_tutors_loc).to_be_visible()
        expected_title = "Преимущества для репетиторов"
        actual_title = preference_for_tutors_loc.text_content()
        assert actual_title == expected_title, (
            f"Expected text does not match actual text. \n"
            f"Expected:{expected_title} \n"
            f"Actual: {actual_title}"
        )

    @allure.step('Check "Продающие объявления и безопасность расчетов" card is visible')
    def check_selling_ads_and_security_paymen_card_visible(self):
        selling_ads_and_security_payment_card = self.page.get_by_text(
            "Продающие объявления и безопасность расчетов Размещайте эффективные объявления и"
        )
        expect(selling_ads_and_security_payment_card).to_be_visible()
        expected_card_text = """
                           Продающие объявления и безопасность расчетов
                        Размещайте эффективные объявления и будьте уверены в получении оплаты после каждого урока.
                           """
        assert (
                selling_ads_and_security_payment_card.text_content().split()
                == expected_card_text.split()
        ), (
            f"Expected text does not match actual text. \n"
            f"Expected: {expected_card_text.split()} \n"
            f"Actual: {selling_ads_and_security_payment_card.text_content().split()}"
        )

    @allure.step("Нажимаем на кнопку More at the top")
    def click_more_button_at_the_top(self):
        self.page.get_by_role("link", name="Подробнее").first.click()

    @allure.step("Нажимаем на кнопку More at the bottom")
    def click_more_button_at_the_bottom(self):
        self.page.get_by_role("link", name="Подробнее").last.click()

    @allure.step("Проверка видимости первой кнопки 'Стать репетитором'")
    def first_btn_become_a_tutor_is_visible(self):
        button = self.page.get_by_role("link", name="Стать репетитором").first
        assert button.is_visible()

    @allure.step("Кликаем на кнопку 'Регистрация'")
    def click_registration_button(self):
        self.page.get_by_test_id("signup").click()

    @allure.step("Проверка доступности первой кнопки стать репетиром")
    def find_first_btn_become_tutor(self):
        become_tutor_btn = self.page.button = self.page.get_by_role("link", name="Стать репетитором").first
        assert become_tutor_btn.is_enabled()

    @allure.step("Проверка редиректа кнопок 'Найти репетитора'")
    def check_find_tutor_btn_redirection(self):
        button_2 = self.page.get_by_role("link", name="Найти репетитора").first
        button_2.click()
        find_tutor_btn_redirection = self.page.url
        return find_tutor_btn_redirection

    def check_find_tutor_btn_2_redirection(self):
        button_3 = self.page.locator("role=link[name='Найти репетитора']").last
        button_3.wait_for(state="visible")
        button_3.click()
        find_tutor_btn_2_redirection = self.page.url
        return find_tutor_btn_2_redirection

    @allure.step("Проверка видипости кнопки 'Найти репетитора'")
    def find_tutor_button_should_be_visible(self):
        button = self.page.locator(
            "body > main > div > div > section:nth-child(1) > div.d-none.d-sm-flex.justify-content-center.mt-4 > a.btn.btn-light.me-2.rounded.btn-lg"
        )
        assert button.is_visible()
