import allure

from test_framework.api.data.client.client_id import client_id
from test_framework.api.steps.steps_api import ApiSteps


@allure.id("C6034340")
@allure.title("C6034340. Изменение статуса email-рассылки без авторизации существующего пользователя")
def test_api_c6034340_update_subscription_status_to_active_no_authorization() -> None:
    # Отправка запроса на изменение статуса рассылки
    ApiSteps().update_subscription_status_email_with_check_status_400(client_id, status_email=True)
