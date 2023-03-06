import allure

from test_framework.api.data.phones_cleint.all_phones import valid_phone_number_for_change_password
from test_framework.api.steps.steps_api import ApiSteps
from test_framework.database.steps.userservicedb import StepsUserService
from test_framework.helpers.main_checkers import CommonChecker


@allure.id("C6039358")
@allure.title("C6039358. Верификация пользователя при вводе верного кода верификации")
def test_api_c6039358_verification_user_by_valid_verification_code() -> None:
    # Получение кода верификации
    ver_code = ApiSteps().get_verification_code_by_phone_wait_it_in_response(
        phone=valid_phone_number_for_change_password
    )

    # Получение кода верификации с бд
    ver_code_from_bd = StepsUserService().get_verification_code(ver_code=ver_code)[0][0]

    #  Проверка на соответвие кода верификации
    CommonChecker().check_field_equals(ver_code, ver_code_from_bd)

    # Верификация юзера с валидным кодом верификации
    ApiSteps().verification_user_with_check_status_code_ok(
        phone_number=valid_phone_number_for_change_password, ver_code=ver_code
    )
