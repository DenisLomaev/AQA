import allure
import pytest

from test_framework.api.data.for_tests.data_C5980334 import test_auth
from test_framework.api.steps.steps_api import ApiSteps


@allure.id("C5980334")
@allure.title("C5980334. Авторизация пользователя с не валидными данными")
@pytest.mark.parametrize("data", test_auth)
def test_api_c5980334_authorization_invalid_data(data) -> None:
    # Авторизация. Попытка получение токена доступа по некорректным данным
    ApiSteps().get_authorization_token_by_invalid_data(data)
