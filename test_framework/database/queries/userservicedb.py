from typing import Any, Union

from test_framework.database.db.user_service import UserServiceDB
from test_framework.database.orm.base_config_db import BaseDB
from test_framework.database.orm.usersevicedb import Client, Contacts, Verification


class QueriesUserService:
    def __init__(self, db: BaseDB = None):
        self.db = db or UserServiceDB()

    def select_all_data_from_table_client(self) -> Union[Client, Any]:
        with self.db.create_session() as session:
            return session.query(Client.id).first()

    def select_verification_code(self, ver_code) -> Union[Verification, Any]:
        with self.db.create_session() as session:
            return session.query(Verification.sms_verification_code).filter(
                Verification.sms_verification_code.ilike(ver_code)
            )

    def select_email_subscription_from_table_contacts_by_client_id(self, client_id) -> Union[Client, Any]:
        with self.db.create_session() as session:
            return session.query(Contacts.email_subscription).filter(Contacts.id_client == client_id)
