import pytest

from test_framework.api.data.phones_cleint.all_phones import (
    valid_password_for_change_password,
    valid_phone_number_for_change_password,
)
from test_framework.api.steps.steps_api import ApiSteps


@pytest.fixture(scope="function")
def authorization_by_phone():
    def authorization(phone_number: str, password: str):
        # Авторизация пользователя
        authorization_json = ApiSteps().authorization_by_phone_and_password(phone_number, password)
        return authorization_json

    yield authorization
    ApiSteps().logout_user()


@pytest.fixture(scope="function")
def authorization_by_passport():
    def authorization(passport_number: str, password: str):
        # Авторизация пользователя
        authorization_json = ApiSteps().authorization_by_passport(passport_number, password)
        return authorization_json

    yield authorization
    ApiSteps().logout_user()


@pytest.fixture(scope="function")
def reg_and_authorization_new_user():
    def reg_and_auth_new_user(phone_number: str, password: str):
        # Авторизация пользователя
        cliend_id = ApiSteps().add_new_client_with_random_value_and_check_status_code(phone_number, password).json()

        ApiSteps().authorization_by_phone_and_password(phone_number, password)
        return cliend_id

    yield reg_and_auth_new_user
    ApiSteps().logout_user()


@pytest.fixture(scope="session")
def authorization_by_phone_for_change_password():
    # Авторизация пользователя
    auth_by_phone = ApiSteps()
    auth_by_phone.authorization_by_phone_and_password(
        phone_number=valid_phone_number_for_change_password, password=valid_password_for_change_password
    )

    yield auth_by_phone
    ApiSteps().logout_user()


@pytest.fixture(scope="session")
def generation_ver_code_and_check_him_by_bd():
    # Получение кода верификации
    ver_code = ApiSteps().get_verification_code_by_phone_wait_it_in_response(
        phone=valid_phone_number_for_change_password
    )
    return ver_code
