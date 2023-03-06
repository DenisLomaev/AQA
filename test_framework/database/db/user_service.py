from test_framework.database.orm.base_config_db import BaseDB


class UserServiceDB(BaseDB):
    user = "huntflow"
    password = "huntflow"
    host = "localhost"
    database = "db_huntflow"
