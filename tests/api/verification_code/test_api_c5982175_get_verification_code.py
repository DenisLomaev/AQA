import allure

from test_framework.api.steps.steps_api import ApiSteps
from test_framework.ui.data.user_data import valid_phone_number_universal


@allure.id("C5982175 ")
@allure.title("C5982175 . Получения кода верификации")
def test_api_c5982175_get_verification_code() -> None:
    # Попытка получения кода верификации по номеру телефона
    ApiSteps().get_verification_code_by_phone(phone=valid_phone_number_universal)
