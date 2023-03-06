from test_framework.helpers.data_generation import get_custom_password_digits_only

new_valid_password = ["Aa1234", "Qwerty5", "Aa11Bb22Cc33Dd44Ee55", "Qwerty5", "Aa1234"]

# Параметр для параметризированного теста с невалидными паролями
verification_code = [
    get_custom_password_digits_only(6),
    get_custom_password_digits_only(6),
    get_custom_password_digits_only(6),
    get_custom_password_digits_only(6),
]
