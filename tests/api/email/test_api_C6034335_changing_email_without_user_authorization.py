import allure

from test_framework.api.data.client.client_id import client_id
from test_framework.api.steps.steps_api import ApiSteps


@allure.id("C6034335")
@allure.title("C6034335. Изменение email существующего пользователя без авторизации")
def test_api_c6034335_get_mail_changed_with_valid_data_with_no_authorization() -> None:
    # Отправка запроса на изменение почты
    ApiSteps().get_email_changed_no_authorization(client_id=client_id)
