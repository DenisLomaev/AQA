import allure

from test_framework.api.data.phones_cleint.all_phones import (
    valid_password_for_change_password,
    valid_phone_number_for_change_password,
)


@allure.id("C5979935")
@allure.title("C5979935. Авторизация пользователя с валидными данными по номеру телефону")
def test_api_c5979935_authorization_by_phone_number(authorization_by_phone) -> None:
    # Авторизация. Получение токена доступа по номеру телефона
    authorization_by_phone(
        phone_number=valid_phone_number_for_change_password, password=valid_password_for_change_password
    )
