import allure

from test_framework.api.steps.steps_api import ApiSteps
from test_framework.ui.data.user_data import valid_passport_number_universal, valid_password_universal


@allure.id("C6040989")
@allure.title("C6040989. Выход из системы в случае неправильного запроса")
def test_api_C6040989_logout_user_with_wrong_request(authorization_by_passport) -> None:
    # Авторизация
    authorization_by_passport(passport_number=valid_passport_number_universal, password=valid_password_universal)
    # Выход пользователя с неправильным запросом.
    ApiSteps().logout_user_with_wrong_request()
