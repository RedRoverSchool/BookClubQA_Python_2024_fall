import requests
from faker import Faker
from requests.auth import HTTPBasicAuth
from models.user_model import RegisterRequest
from Data.constants import BASE_URL, AUTH_CREDENTIALS

USERS_URL = f"{BASE_URL}/api/users/"


def create_user(user_data: RegisterRequest) -> dict:
    """
    Создает пользователя через API.

    :param user_data: RegisterRequest, данные пользователя для регистрации.
    :return: dict, информация о созданном пользователе.
    """
    response = requests.post(
        USERS_URL,
        json=user_data.dict(exclude_none=True),  # Преобразуем модель в словарь
        auth=HTTPBasicAuth(*AUTH_CREDENTIALS)
    )
    response.raise_for_status()
    return response.json()


def delete_user(email: str):
    """
    Удаляет пользователя через API.

    :param email: str, email пользователя.
    :return: None.
    """
    delete_url = f"{USERS_URL}{email}/"
    response = requests.delete(
        delete_url,
        auth=HTTPBasicAuth(*AUTH_CREDENTIALS)
    )
    response.raise_for_status()


def create_fake_user_with_role(role: str) -> dict:
    """
    Создает фейкового пользователя с указанной ролью.

    :param role: str, роль пользователя ('teacher' или 'student').
    :return: dict, данные созданного пользователя.
    """
    fake = Faker()
    password = fake.password()
    user_data = RegisterRequest(
        first_name=fake.name(),
        email=fake.email(),
        password=password,
        is_tutor=role == "teacher",
        is_premium=role == "teacher",
        is_standart=role == "student",
        is_writer=role == "teacher",
        end_subscription="2024-12-20"
    )
    created_user = create_user(user_data)
    return {"email": created_user["email"], "password": password, "role": role}



def delete_fake_user(email: str):
    """
    Удаляет фейкового пользователя по email.

    :param email: str, email пользователя.
    :return: None.
    """
    delete_user(email)