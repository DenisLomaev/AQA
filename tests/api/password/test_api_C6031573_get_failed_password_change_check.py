import allure
import pytest

from test_framework.api.data.for_tests.data_c5994271 import verification_code
from test_framework.api.data.phones_cleint.all_phones import valid_phone_number_for_change_password
from test_framework.api.steps.steps_api import ApiSteps
from test_framework.helpers.main_checkers import CommonChecker


@allure.id("C6031573")
@allure.title("C6031573. Ввод не валидных символов в строку newPassword")
@pytest.mark.parametrize("expected_password", verification_code)
# баг исправлен, но еще должен будет поменяться статус код с 500 на 400
def test_api_C6031573_get_failed_password_change_check(
    authorization_by_phone_for_change_password, expected_password
) -> None:

    # Попытка отправить запрос на изменение пароля не валидными данными
    response = (
        ApiSteps()
        .failed_change_user_password(
            valid_phone_number=valid_phone_number_for_change_password, password=expected_password
        )
        .json()
    )

    # Проверка Response body
    CommonChecker.check_not_empty_response(response["message"], assertion_message="invalid password format")
