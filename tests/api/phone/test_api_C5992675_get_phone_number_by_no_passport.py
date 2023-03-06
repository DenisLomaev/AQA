import allure

from test_framework.api.steps.steps_api import ApiSteps
from test_framework.helpers.main_checkers import CommonChecker


@allure.id("C5992675")
@allure.title("C5992675. Получение номера телефона по несуществующему номеру паспорта")
def test_api_c5992675_get_phone_number_no_passport() -> None:
    # Получение номера телефона по номеру паспорта
    phone_number = ApiSteps().get_phone_number_by_passport_without_check(passport_number="")

    # Проверка статус кода 400
    CommonChecker.check_status_code_400(phone_number)

    # Проверка сообщения об ошибке
    CommonChecker.check_not_empty_response(
        phone_number.json()["message"], assertion_message="Сообщение не было получено"
    )
