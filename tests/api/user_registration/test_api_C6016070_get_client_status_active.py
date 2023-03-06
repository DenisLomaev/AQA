import allure

from test_framework.api.data.client.client_status import statuses_client
from test_framework.api.steps.steps_api import ApiSteps
from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.data.user_data import valid_phone_number_universal


@allure.id("C6016070")
@allure.title("C6016070. Проверка регистрации пользователя (статус ACTIVE)")
def test_api_c6016070_get_client_status_active() -> None:
    # Попытка получения активного статуса клиента
    response_json = ApiSteps().get_all_information_client_by_phone(phone=valid_phone_number_universal).json()

    # Проверка статуса клиента
    CommonChecker.check_field_equals(
        response_json["clientStatus"], statuses_client["active"], assertion_message="Статус не совпадает"
    )
