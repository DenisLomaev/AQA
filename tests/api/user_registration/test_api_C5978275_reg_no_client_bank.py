import allure

from test_framework.api.steps.steps_api import ApiSteps
from test_framework.helpers.data_generation import get_custom_login
from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.data.user_data import password


@allure.id("C5978275")
@allure.title("C5978275. Регистрация не клиента банка в приложении")
def test_api_c5978275_reg_no_client_bank(reg_and_authorization_new_user) -> None:
    # Регистрация не клиента банка
    random_phone = get_custom_login()
    client_id = reg_and_authorization_new_user(phone_number=random_phone, password=password)

    info_about_client = ApiSteps().get_all_information_from_sait_by_access_token().json()

    # Проверка id пользователя
    CommonChecker.check_field_equals(client_id, info_about_client["clientId"], assertion_message="ID не совподает")
