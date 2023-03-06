import allure

from test_framework.api.data.phones_cleint.all_phones import wrong_phone_number
from test_framework.api.steps.steps_api import ApiSteps


@allure.id("C5982187 ")
@allure.title("C5982187 . Получения кода ошибки 400 при попытке верификации")
def test_api_c5982187_get_verification_code_by_wrong_phone_number() -> None:
    # Попытка получения кода верификации по номеру телефона
    ApiSteps().get_verification_code_by_invalid_phone(phone=wrong_phone_number)
