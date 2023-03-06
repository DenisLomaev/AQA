import allure

from test_framework.api.data.id_client.id_client import valid_client_id
from test_framework.api.steps.steps_api import ApiSteps


@allure.id("C5995382")
@allure.title("C5995382. Получение информации о настройке уведомлений без авторизации")
def test_api_C5995382_get_info_notifications_without_authorization() -> None:
    # Получение информации о настройках уведомления по id клиента
    ApiSteps().get_status_notification_by_id_without_authorization(id_client=valid_client_id)
