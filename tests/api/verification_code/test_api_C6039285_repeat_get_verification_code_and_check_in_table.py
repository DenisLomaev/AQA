import allure
import pytest

from test_framework.api.steps.steps_api import ApiSteps
from test_framework.database.steps.userservicedb import StepsUserService
from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.data.user_data import valid_phone_number_universal


@allure.id("C6039285")
@allure.title("C6039285. Повторное получения кода верификации")
def test_api_c6039285_repeat_get_verification_code_and_check_in_table() -> None:
    # Получение кода верификации
    ver_code = ApiSteps().get_verification_code_by_phone_wait_it_in_response(phone=valid_phone_number_universal)
    # Получение кода верификации с БД и проверка на равенство
    ver_code_from_bd = StepsUserService().get_verification_code_with_check_it_equals_value(ver_code)
    # Повторное получение кода верификации
    second_ver_code = ApiSteps().get_verification_code_by_phone_wait_it_in_response(phone=valid_phone_number_universal)
    # Получение повтороного кода верификации с БД
    second_ver_code_from_bd = StepsUserService().get_verification_code_with_check_it_equals_value(second_ver_code)
    # Проверка на различие первого и второго кода верификации в БД
    CommonChecker().check_field_not_equals(ver_code_from_bd, second_ver_code_from_bd)
