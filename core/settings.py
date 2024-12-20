from faker import Faker

# from pydantic_settings import BaseSettings, SettingsConfigDict

fake = Faker()

base_url = "http://tester:dslfjsdfblkhew@122b1klbfw@testing.misleplav.ru"
fake_name_for_registration = fake.user_name()

policy_url = "https://www.example.com/privacy-policy"
list_url = "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/listings/list/"
tutors_list_url = "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/listings/list/"
list_url = "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/list/"
tutors_list_url = "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/listings/list/"
signup_url = "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/authorization/signup/"
login_url = "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/authorization/login/"
title = "Example Domain"

site_pages_urls = [
    {
        "name": "Main page",
        "url": "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/",
    },
    {
        "name": "Lists Page",
        "url": "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/list/",
    },
    {
        "name": "Signup Page",
        "url": "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/signup/",
    },
    {
        "name": "Create list Page",
        "url": "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/create/",
    },
    {
        "name": "User profile Page",
        "url": "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/profile/",
    },
    {
        "name": "Statistics Page",
        "url": "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/statistics/",
    },
]

site_pages_urls_for_guest = [base_url, login_url, signup_url, list_url]