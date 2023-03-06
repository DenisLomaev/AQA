import allure
import pytest

from test_framework.api.data.for_tests.data_c5994271 import new_valid_password
from test_framework.api.data.phones_cleint.all_phones import valid_phone_number_for_change_password


@allure.id("C5994271")
@allure.title("C5994271. Установление нового пароля с валидными данными в строке 'newPassword'")
@pytest.mark.parametrize("expected_password", new_valid_password)
def test_api_c5994271_set_new_password_with_valid_data(
    authorization_by_phone_for_change_password, expected_password
) -> None:

    # Смена пароля и логаут
    authorization_by_phone_for_change_password.success_change_user_password(
        valid_phone_number_for_change_password, expected_password
    )
    authorization_by_phone_for_change_password.logout_user()

    # Проверка входа в систему с измененным паролем и логаут
    authorization_by_phone_for_change_password.authorization_by_phone_and_password(
        phone_number=valid_phone_number_for_change_password, password=expected_password
    )
