import allure

from test_framework.api.data.id_client.id_client import invalid_client_id
from test_framework.api.data.phones_cleint.all_phones import (
    valid_password_for_change_password,
    valid_phone_number_for_change_password,
)
from test_framework.api.steps.steps_api import ApiSteps


@allure.id("C5996223")
@allure.title("C5996223. Получение информации о настройке с незарегистрированным в системе clientId")
def test_api_C5996223_get_info_notifications_with_not_registred_cliend_id(authorization_by_phone) -> None:
    # Авторизация юзера, для получения акссес токена в хедерс
    authorization_by_phone(
        phone_number=valid_phone_number_for_change_password, password=valid_password_for_change_password
    )

    # Попытка получения cтатуса уведомлений по id клиента незарегистрированного в системе
    ApiSteps().get_status_notification_by_invalid_id(id_client=invalid_client_id)
