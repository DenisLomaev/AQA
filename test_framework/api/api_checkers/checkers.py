from typing import Any, Union

from test_framework.helpers.main_checkers import CommonChecker


class CheckersApi:
    @staticmethod
    def checker_response(api_response: Any) -> None:
        CommonChecker.check_field_equals(api_response["page"], 2, assertion_message="Некорректное значение page")

    @staticmethod
    def checker_key_in_collection(key: str, collection: Union[dict, list]) -> None:
        CommonChecker.check_key_in_collection(
            key, collection, assertion_message=f"отсутствует ключ {key} в {collection}"
        )

    @staticmethod
    def checker_satus_notifications(response_json: dict) -> None:
        # Проверка статуса sms-уведомлений
        CommonChecker.check_field_equals(
            response_json["SMSNotification"], True, assertion_message="Статус не совпадает"
        )
        # Проверка статуса push-уведомлений
        CommonChecker.check_field_equals(
            response_json["PushNotification"], True, assertion_message="Статус не совпадает"
        )
        # Проверка статуса подписки по email
        CommonChecker.check_field_equals(
            response_json["EmailSubscription"], False, assertion_message="Статус не совпадает"
        )

    @staticmethod
    def check_availability_acces_token(response: dict) -> None:
        CommonChecker.check_key_in_collection(
            "accessToken", response, assertion_message="Отсутвует поле acces token в ответе"
        )
        CommonChecker.check_not_empty_response(response["accessToken"], assertion_message="Access token = None")
