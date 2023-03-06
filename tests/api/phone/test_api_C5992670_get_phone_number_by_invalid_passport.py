import allure

from test_framework.api.data.passport_client.passport_client import invalid_passport_number
from test_framework.api.steps.steps_api import ApiSteps
from test_framework.helpers.main_checkers import CommonChecker


@allure.id("C5992670")
@allure.title("C5992670. Получение номера телефона по несуществующему номеру паспорта")
def test_api_c5992670_get_phone_number_invalid_passport() -> None:
    # Получение номера телефона по номеру паспорта
    phone_number = ApiSteps().get_phone_number_by_passport_without_check(passport_number=invalid_passport_number)

    # Проверка статус кода 400
    CommonChecker.check_status_code_400(phone_number)

    # Проверка сообщения об ошибке
    CommonChecker.check_not_empty_response(
        phone_number.json()["message"], assertion_message="Сообщение не было получено"
    )
