import allure

from test_framework.api.steps.steps_api import ApiSteps
from test_framework.helpers.data_generation import get_custom_email
from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.data.user_data import valid_password_universal, valid_phone_number_universal


@allure.id("C5998149")
@allure.title("C5998149. Изменение email с валидными данными ")
def test_api_c5998149_get_mail_changed_with_valid_data(authorization_by_phone):

    # Получение случайного емайла
    random_email = get_custom_email()

    # Авторизация
    authorization_by_phone(phone_number=valid_phone_number_universal, password=valid_password_universal)

    client_id = ApiSteps().get_all_info_about_user_by_access_token().json()["clientId"]

    # Отправка запроса на изменение почты
    ApiSteps().get_random_email_changed_with_valid_data(client_id=client_id, random_email=random_email)

    # Получен   ие информации о клиенте
    response_json = ApiSteps().get_all_info_about_user_by_access_token().json()

    # Проверка изменения Email в таблице БД.
    CommonChecker.check_field_equals(response_json["email"], random_email, assertion_message="Email не совпадает")
