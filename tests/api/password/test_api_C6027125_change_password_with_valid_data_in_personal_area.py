import allure
import pytest

from test_framework.api.data.phones_cleint.all_phones import (
    valid_password_for_change_password,
    valid_phone_number_for_change_password,
)
from test_framework.api.steps.steps_api import ApiSteps


@pytest.mark.skip(reason="нет возможности удалить accesstoken")
@allure.id("C6027125")
@allure.title("C6027125. Изменение пароля на валидный пароль в личном кабинете.")
def test_api_c6027125_change_password_with_valid_data_in_personal_area() -> None:
    # Авторизация пользователя

    ApiSteps().authorization_by_phone_and_password(
        phone_number=valid_phone_number_for_change_password, password=valid_password_for_change_password
    )

    # Смена пароля запросом pathc
    ApiSteps().change_password_with_auth_user_and_valid_password(password="Aa1234", new_password="Aa1234")

    # Логаут юзера
    ApiSteps().logout_user()

    # Повторная авторизация и логаут
    ApiSteps().authorization_by_phone_and_password(
        phone_number=valid_phone_number_for_change_password, password=valid_password_for_change_password
    )
    ApiSteps().logout_user()
