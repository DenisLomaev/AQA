import allure

from test_framework.api.data.phones_cleint.all_phones import (
    valid_password_for_change_password,
    valid_phone_number_for_change_password,
)
from test_framework.api.steps.steps_api import ApiSteps


@allure.id("C6033991")
@allure.title("C6033991. Изменение статуса клиента на Active")
def test_api_с6033991_change_security_question_with_valid_value(authorization_by_phone) -> None:

    # Авторизация для получения акссес токена в хедерс
    authorization_by_phone(
        phone_number=valid_phone_number_for_change_password, password=valid_password_for_change_password
    )

    # Смена секретного вопроса
    ApiSteps().change_security_question_with_valid_value(basic_question="vasika", new_question="vasika")
