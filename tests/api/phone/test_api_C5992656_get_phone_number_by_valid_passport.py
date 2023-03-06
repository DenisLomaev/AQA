import allure

from test_framework.api.steps.steps_api import ApiSteps
from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.data.user_data import valid_passport_number_universal, valid_phone_number_universal


@allure.id("C5992656")
@allure.title("C5992656. Получение номера телефона по существующему номеру паспорта.")
def test_api_c5992656_get_phone_number_by_valid_passport() -> None:
    # Получение номера телефона по номеру паспорта
    phone_number = ApiSteps().get_phone_number_by_passport(passport_number=valid_passport_number_universal).json()

    # Проверка валидности номера телефона
    CommonChecker.check_field_equals(
        phone_number, valid_phone_number_universal, assertion_message="Получен неверный номер телефона"
    )
