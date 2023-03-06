from typing import Any

import allure

from test_framework.database.checkers.userservicedb import CheckerUserService
from test_framework.database.queries.userservicedb import QueriesUserService
from test_framework.helpers.main_checkers import CommonChecker


class StepsUserService:
    def __init__(self):
        self.queries = QueriesUserService()
        self.db_checker = CheckerUserService()

    def get_verification_code(self, ver_code) -> Any:
        return self.queries.select_verification_code(ver_code)

    @allure.step("Получение verification_code из БД и проверка его значения на равенство")
    def get_verification_code_with_check_it_equals_value(self, ver_code: str) -> Any:
        ver_code_db = StepsUserService().get_verification_code(ver_code)[0][0]
        CommonChecker().check_field_equals(ver_code_db, ver_code)
        return ver_code_db

    def get_user_info_from_client_table(self) -> Any:
        return self.queries.select_all_data_from_table_client()

    def get_info_from_contacts_table_by_id(self, client_id) -> Any:
        request = self.queries.select_email_subscription_from_table_contacts_by_client_id(client_id=client_id)
        return request
