import string
import random

valid_password = "Potter1$"
valid_login = "Garry"

invalid_login = "q"
invalid_password = "p"


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
