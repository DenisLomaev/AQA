import allure
import pytest

from test_framework.api.data.client.client_id import wrong_client_id
from test_framework.api.steps.steps_api import ApiSteps


@pytest.mark.xfail(reason="Debugging is ongoing ")
@allure.id("C6015831")
@allure.title("C6015831. Изменение почты клиента с несуществующим ID  без авторизации")
def test_api_c6015831_get_email_changed_with_wrong_id():

    # Отправка запроса на изменение почты
    ApiSteps().get_email_changed_with_invalid_data(client_id=wrong_client_id)
