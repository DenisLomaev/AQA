import allure

from test_framework.api.data.phones_cleint.all_phones import invalid_phone_number
from test_framework.api.steps.steps_api import ApiSteps


@allure.id("C5982205 ")
@allure.title("C5982205 . Получения кода ошибки 404 при попытке верификации")
def test_api_c5982205_get_verification_code_by_wrong_phone_number() -> None:
    # Попытка получения кода верификации по номеру телефона
    ApiSteps().get_verification_code_by_non_existent_phone(phone=invalid_phone_number)
