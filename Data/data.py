import string
import random
from models.user_model import RegisterRequest
from faker import Faker
from playwright.sync_api import Page

fake = Faker()

valid_password = "Potter1$"
valid_login = "Garry"

invalid_login = "q-"
invalid_password = "p==="

# with announcement
EMAIL_TUTOR_KM = "tutor_testing@bk.ru"
PASSWORD_TUTOR_KM = "I165TVAzghk8"

EMAIL_TUTOR_MV = "teacher-test@yopmail.com"
PASSWORD_TUTOR_MV = "5uR94zLhF80r"

# without announcement
EMAIL_TUTOR_WA_KM = "tutor_test_misliplav@mail.ru"
PASSWORD_TUTOR_WA_KM = "iZ52toubKacm"

EMAIL_STUDENT_KM = "student-test-misliplav@mail.ru"
PASSWORD_STUDENT_KM = "JXvNebAMsWb7"

EMAIL_TUTOR_ZU = "zayatest55@gmail.com"
PASSWORD_TUTOR_ZU = "RM7tAgSYSh7X"

EMAIL_STUDENT_ZU = "zarinatest4@gmail.com"
PASSWORD_STUDENT_ZU = "q2e6hXVgsy0W"


def generate_valid_password():
    # Определим минимальную длину пароля
    min_length = 8
    # Определим набор символов для генерации
    letters = string.ascii_letters  # буквы
    digits = string.digits  # цифры
    chars = string.punctuation  # специальные символы
    # Генерируем пароль
    password = (
        random.choice(letters) + random.choice(digits) + random.choice(chars)
    )  # гарантируем наличие каждой категории
    password += "".join(
        random.choices(letters + digits + chars, k=min_length - len(password))
    )  # добавляем оставшиеся символы

    # Перемешиваем пароль, чтобы случайно распределить символы
    password = "".join(random.sample(password, len(password)))
    return password


class UserFactory:
    def __init__(self, page: Page):
        self.page = page

    @staticmethod
    def generate_user(role: str = "student", **kwargs) -> RegisterRequest:
        """Генерирует данные для регистрации пользователя."""
        user_data = {
            "first_name": fake.first_name(),
            "email": fake.email(),
            "password": fake.password(
                length=12,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ),
            "is_tutor": kwargs.get("is_tutor", role == "teacher"),
            "is_premium": kwargs.get("is_premium", role == "teacher"),
            "is_standart": kwargs.get("is_standart", role == "student"),
            "is_writer": kwargs.get("is_writer", role == "teacher"),
            "end_subscription": kwargs.get("end_subscription", "2024-12-24"),
        }
        return RegisterRequest(**user_data)
