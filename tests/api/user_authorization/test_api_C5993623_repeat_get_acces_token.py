from typing import Callable

import allure

from test_framework.api.api_checkers.checkers import CheckersApi
from test_framework.ui.data.user_data import valid_phone_number_universal


@allure.id("C5993623")
@allure.title("C5993623. Авторизация пользователя: Повторное получение acces token")
def test_api_C5993623_repeat_get_acces_token(authorization_by_phone: Callable) -> None:
    # Проверка получение acces токена
    authorization_json = authorization_by_phone(phone_number=valid_phone_number_universal, password="Aa1234")

    # Проверка присутствие access токена
    CheckersApi().check_availability_acces_token(authorization_json)
