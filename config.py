from sys import platform

# Окружение для запуска тестов
env = platform

# Адрес подключения к БД
url_db = "postgresql+psycopg2://{}:{}@{}:5432/{}"

# Частота опроса
default_interval = 2
verification_interval = 4

# Таймаут
default_timeout = 120
verification_timeout = 80
