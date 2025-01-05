from faker import Faker

fake = Faker()
fake_name_for_registration = fake.user_name()

# links
base_url = "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru"

signup_url = f"{base_url}/authorization/signup/"
login_url = f"{base_url}/authorization/login/"

policy_url = "https://www.example.com/privacy-policy"
list_url = f"{base_url}/listings/list/"

tutors_list_url = f"{base_url}/listings/list/"

support_url = "https://t.me/misleplav_support_bot"

# tutor's url
my_announcement_url = f"{base_url}/listings/my_listing/"
my_student_url = f"{base_url}/dashboard/my_students/"
teacher_profile_url = f"{base_url}/subscription/profile/"
statistics_url = f"{base_url}/statistics/statistics/"
edit_announcement_url = "http://testing.misleplav.ru/listings/update/"

title = "Example Domain"

site_pages_urls = [
    {
        "name": "Main page",
        "url": "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/",
    },
    {
        "name": "Lists Page",
        "url": "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/listings/my_listing/",
    },
    {
        "name": "Signup Page",
        "url": "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/authorization/signup/",
    },
    {
        "name": "Create list Page",
        "url": "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/listings/create/",
    },
    {
        "name": "User profile Page",
        "url": "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/subscription/profile/",
    },
    {
        "name": "My students Page",
        "url": "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/dashboard/my_students/",
    },
]

pages_urls_for_guest = [base_url, login_url, signup_url, list_url]
