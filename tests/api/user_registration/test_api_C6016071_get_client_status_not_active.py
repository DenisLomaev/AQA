import allure

from test_framework.api.data.client.client_status import statuses_client
from test_framework.api.data.phones_cleint.all_phones import valid_phone_number_not_active
from test_framework.api.steps.steps_api import ApiSteps
from test_framework.helpers.main_checkers import CommonChecker


@allure.id("C6016071")
@allure.title("C6016071. Проверка регистрации пользователя (статус NOT_ACTIVE) ")
def test_api_c6016071_get_client_status_not_active() -> None:
    # Попытка получения неактивного статуса клиента
    response_json = ApiSteps().get_all_information_client_by_phone(phone=valid_phone_number_not_active).json()

    # Проверка статуса клиента
    CommonChecker.check_field_equals(
        response_json["clientStatus"], statuses_client["not active"], assertion_message="Статус не совпадает"
    )
