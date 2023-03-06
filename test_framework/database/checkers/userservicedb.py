from typing import Any

from test_framework.helpers.main_checkers import CommonChecker


class CheckerUserService:
    @staticmethod
    def check_id_in_db(response: Any, expected_id: str) -> None:
        CommonChecker.check_field_equals(
            response, expected_id, assertion_message="id полученный из БД не совпадает с ожидаемым"
        )
