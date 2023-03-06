import allure

from test_framework.api.data.client.client_id import wrong_client_id
from test_framework.api.steps.steps_api import ApiSteps
from test_framework.ui.data.user_data import valid_password_universal, valid_phone_number_universal


@allure.id("C6034341")
@allure.title("C6034341. Изменение статуса email-рассылки с незарегистрированным в системе clientId")
def test_api_c6034341_update_subscription_status_to_active_with_wrong_clientId(authorization_by_phone) -> None:
    # Авторизация
    authorization_by_phone(phone_number=valid_phone_number_universal, password=valid_password_universal)

    # Отправка запроса на изменение статуса рассылки
    ApiSteps().update_subscription_status_email_with_check_status_400(client_id=wrong_client_id, status_email=True)
