import functools
from typing import Any, Union


class CommonChecker:
    default_message = "Некорректный статус код"

    @staticmethod
    def check_status_code_ok(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 200, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_400(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 400, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_406(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 406, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_500(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 500, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_404(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 404, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_201(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 201, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_401(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 401, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_field_equals(
        field: Any, expected_value: Any, assertion_message: str = "Некорректное значение поля"
    ) -> None:
        assert field == expected_value, assertion_message

    @staticmethod
    def check_key_in_collection(
        key: str, collection: Union[list, dict], assertion_message: str = "ключ отсутствует в коллекции"
    ) -> None:
        assert key in collection, assertion_message

    @staticmethod
    def check_not_empty_response(r: Any, assertion_message: str = default_message) -> None:
        assert r is not None, assertion_message

    @staticmethod
    def check_field_not_equals(
        field: str, expected_value: Union[str, int], assertion_message: str = "Некорректное значение поля"
    ) -> None:
        assert field != expected_value, assertion_message


# Функция взаимодействует с assert и проверяет его на True/False
class WaitException(AssertionError):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


def checker_exception(step: Any) -> Any:

    step_name = step.__name__.split(".")[-1]

    @functools.wraps(step)
    def wrap(*args: Any, **kwargs: Any) -> Any:
        try:
            response = step(*args, **kwargs)
        except AssertionError as err:
            raise WaitException(f"Проверка {step_name}, завершилась неудачно: {str(err)}")

        return response

    return wrap
