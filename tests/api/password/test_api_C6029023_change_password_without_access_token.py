import allure

from test_framework.api.steps.steps_api import ApiSteps


@allure.id("C6029023")
@allure.title("C6029023. Изменение пароля на валидный пароль при неуспешной валидации токена")
def test_api_C6029023_change_password_without_access_token() -> None:

    # Смена пароля запросом pathc
    ApiSteps().change_password_with_auth_user_and_invalid_password(password="Aa123423", new_password="Aa1234")
