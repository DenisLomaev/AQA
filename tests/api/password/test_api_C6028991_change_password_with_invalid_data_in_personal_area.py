import allure
import pytest

from test_framework.api.data.phones_cleint.all_phones import (
    valid_password_for_change_password,
    valid_phone_number_for_change_password,
)
from test_framework.api.steps.steps_api import ApiSteps


@allure.id("C6028991")
@allure.title("C6028991. Изменение пароля в личном кабинете при несовпадении старого пароля")
def test_api_C6028991_change_password_with_invalid_data_in_personal_area(authorization_by_phone) -> None:
    # Авторизация пользователя

    authorization_by_phone(
        phone_number=valid_phone_number_for_change_password, password=valid_password_for_change_password
    )

    # Смена пароля запросом pathc
    ApiSteps().change_password_with_auth_user_and_invalid_password(password="Aa123423", new_password="Aa1234")
