import allure

from test_framework.ui.data.user_data import valid_passport_number_universal, valid_password_universal


@allure.id("C5980156")
@allure.title("C5980156. Авторизация пользователя с валидными данными по номеру паспорта")
def test_api_c5980156_authorization_by_passport_number(authorization_by_passport) -> None:
    # Авторизация. Получение токена доступа по номеру паспорта
    authorization_by_passport(passport_number=valid_passport_number_universal, password=valid_password_universal)
