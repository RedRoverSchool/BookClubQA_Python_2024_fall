import allure
from playwright.sync_api import Page


class TeacherProfile:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Собираем все ссылки на объявления")
    def collect_listings_links(self):
        links = self.page.locator('//div[@class="card-body"]/a').evaluate_all(
            "elements => elements.map(el => el.getAttribute('href'))"
        )
        return links

    @allure.step("Кликаем на первую ссылку из списка объявлений")
    def click_first_listing(self):
        links = self.collect_listings_links()
        if len(links) > 0:
            self.page.locator('//div[@class="card-body"]/a').nth(0).click()
        else:
            raise Exception("Ссылки на объявления не найдены")

    @allure.step("Ищем и кликаем по первой доступной ссылке на объявление")
    def click_on_first_available_listing(self) -> object:
        for i in range(1, 11):  # Проверяем до 10 ссылок
            listing_selector = f'//a[@href="/listings/{i}/"]'
            if self.page.locator(listing_selector).count() > 0:
                self.page.locator(listing_selector).click()
                return
        raise Exception("Доступные ссылки на объявления не найдены")
