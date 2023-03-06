import allure

from test_framework.api.data.phones_cleint.all_phones import (
    valid_password_for_change_password,
    valid_phone_number_for_change_password,
)
from test_framework.api.steps.steps_api import ApiSteps


@allure.id("C5995309")
@allure.title("C5995309. Получение информации о настройке уведомлений")
def test_api_C5995309_get_info_notifications(authorization_by_phone) -> None:

    # Авторизация юзера, для получения акссес токена в хедерс
    authorization_by_phone(
        phone_number=valid_phone_number_for_change_password, password=valid_password_for_change_password
    )

    # Извлечение ID авторизованного пользователя
    client_id = ApiSteps().get_all_information_client_by_phone(phone=valid_phone_number_for_change_password).json()
    client_id = client_id["idCustomer"]

    # Проверка настроек уведовлений
    ApiSteps().get_status_notification_by_id_with_all_check(client_id)
