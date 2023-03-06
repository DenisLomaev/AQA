import allure
import pytest

from test_framework.api.data.for_tests.data_c5994271 import verification_code
from test_framework.api.data.phones_cleint.all_phones import valid_phone_number_for_change_password
from test_framework.api.steps.steps_api import ApiSteps
from test_framework.database.steps.userservicedb import StepsUserService
from test_framework.helpers.main_checkers import CommonChecker


@pytest.mark.skip(reason="нет возможности удалить accesstoken")
@allure.id("C6039405")
@allure.title("C6039405. Верификация пользователя при вводе неверного кода верификации 1 раз")
@pytest.mark.parametrize("expected_verification_code", verification_code)
def test_api_c6039405_verification_user_by_invalid_verification_code_more_3_times(
    generation_ver_code_and_check_him_by_bd, expected_verification_code
) -> None:
    ver_code = generation_ver_code_and_check_him_by_bd
    # Получение кода верификации с бд
    ver_code_from_bd = StepsUserService().get_verification_code(ver_code=ver_code)

    #  Проверка на соответвие кода верификации
    CommonChecker().check_field_equals(ver_code, *ver_code_from_bd[0])

    # Верификация юзера с валидным кодом верификации
    ApiSteps().verification_user_with_check_status_code_406(
        phone_number=valid_phone_number_for_change_password, ver_code=expected_verification_code
    )
