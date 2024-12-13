from playwright.sync_api import Page
import pytest
from core.settings import site_pages_urls


@pytest.mark.parametrize(
    "data", site_pages_urls, ids=[u["name"] for u in site_pages_urls]
)
def test_profile_btn_visibility(user_profile, login, data, page: Page):
    """Проверка видимости кнопки 'Профиль'
    TC_11.002.01.001 | [Teacher ] Header > "Профиль" button > Visibility check"""
    login.open_login_page()
    login.full_login("teacher_test", "a.9QA{!@HDB;en2")
    page_url = data["url"]
    page.goto(page_url)
    user_profile.visibility_profile_btn_check()


@pytest.mark.parametrize(
    "data", site_pages_urls, ids=[u["name"] for u in site_pages_urls]
)
def test_profile_btn_hover(user_profile, login, data, page: Page):
    """Проверка смены цвета кнопки 'Профиль' при наведении на нее курсора
    TC_11.002.01.002 | [Teacher ] Header > "Профиль" button > Hover support check"""
    login.open_login_page()
    login.full_login("teacher_test", "a.9QA{!@HDB;en2")
    page_url = data["url"]
    page.goto(page_url)
    user_profile.hover_profile_btn_color_check()


@pytest.mark.parametrize(
    "data", site_pages_urls, ids=[u["name"] for u in site_pages_urls]
)
def test_profile_btn_redirection(user_profile, login, data, page: Page):
    """Проверка перенаправления на страницу профиля пользователя после нажатия кнопки 'Профиль'
    TC_11.002.01.003 | [Teacher ] Header > "Профиль" button > Redirection check"""
    login.open_login_page()
    login.full_login("teacher_test", "a.9QA{!@HDB;en2")
    page_url = data["url"]
    page.goto(page_url)
    user_profile.click_profile_btn()
    user_profile.profile_btn_redirection_check()
