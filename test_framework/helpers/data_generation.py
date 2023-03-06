import secrets
import string

from test_framework.ui.data.data_cyrillic_letters import cyrillic_letters_lowercase


def get_custom_login(login: int = 11) -> str:
    # Генерация случайного логина
    return "".join(secrets.choice(string.digits) for _ in range(login))


def get_custom_passport(passport_len_firt: int = 4, passport_len_second: int = 6) -> str:
    """Генерация случайного логина"""
    return (
        str("".join(secrets.choice(string.digits) for _ in range(passport_len_firt)))
        + " "
        + str("".join(secrets.choice(string.digits) for _ in range(passport_len_second)))
    )


def get_custom_email(email_len: int = 8) -> str:
    latin_letters_email = string.ascii_letters + string.digits
    return str("".join(secrets.choice(latin_letters_email) for _ in range(email_len))) + "@mail.ru"


def get_custom_password_letters_only(password_len: int = 10) -> str:
    return "".join(secrets.choice(string.ascii_letters) for _ in range(password_len))


def get_custom_password_cyrillic_only(password_len: int = 5) -> str:
    cyrillic_letters = cyrillic_letters_lowercase + cyrillic_letters_lowercase.upper()
    return "".join(secrets.choice(cyrillic_letters) for _ in range(password_len))


def get_custom_password_digits_only(password_len: int = 5) -> str:
    return "".join(secrets.choice(string.digits) for _ in range(password_len))


def get_custom_password_punctuation_only(password_len: int = 5) -> str:
    return "".join(secrets.choice(string.punctuation) for _ in range(password_len))


def get_custom_password(password_len: int = 10) -> str:
    """Функция генерации случайного пароля длиной password_len"""
    return "".join(secrets.choice(string.ascii_letters + string.digits) for i in range(password_len))
