import allure

from test_framework.api.steps.steps_api import ApiSteps
from test_framework.database.steps.userservicedb import StepsUserService
from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.data.user_data import valid_password_universal, valid_phone_number_universal


@allure.id("C6034337")
@allure.title("C6034337. Активация рассылки для пользователя с валидными данными")
def test_api_c6034337_update_subscription_status_to_active(authorization_by_phone) -> None:
    # Авторизация
    authorization_by_phone(phone_number=valid_phone_number_universal, password=valid_password_universal)

    # Получаем клиент ID
    client_id = ApiSteps().get_all_info_about_user_by_access_token().json()["clientId"]

    # Отправка запроса на изменение статуса рассылки
    ApiSteps().update_subscription_status_to_active_with_check_status_ok(client_id, status_email=True)

    # Получаем информацию из БД о статусе email подписки
    user_info = StepsUserService().get_info_from_contacts_table_by_id(client_id)

    # проверка актуального статуса с ожидаемым
    CommonChecker.check_field_equals(str(*user_info[0]), "True", assertion_message="Статус не совпадает")
