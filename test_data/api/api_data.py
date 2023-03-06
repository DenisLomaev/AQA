import uuid

from test_framework.helpers.data_generation import get_custom_email, get_custom_passport, get_custom_password


class DataClient:
    @staticmethod
    def get_payload_for_no_client(phone_number_no_client: str) -> dict:
        return {
            "mobilePhone": phone_number_no_client,
            "password": "Qwerty5",
            "securityQuestion": "cat name",
            "securityAnswer": "vasika",
            "email": "denis1599@mail.ru",
            "firstName": "Fortestfirsttest",
            "middleName": "Fortestmiddlename",
            "lastName": "Fortestlastname",
            "passportNumber": "SN-121-000-199",
            "countryOfResidence": "RU",
            "ExpiryDate": "2022-09-28",
        }

    @staticmethod
    def get_random_payload_for_no_client(phone_number: str, password: str) -> dict:
        return {
            "mobilePhone": phone_number,
            "password": password,
            "securityQuestion": "cat name",
            "securityAnswer": "vasika",
            "email": get_custom_email(),
            "firstName": "Fortestfirsttest",
            "middleName": "Fortestmiddlename",
            "lastName": "Fortestlastname",
            "passportNumber": get_custom_passport(),
            "countryOfResidence": "RU",
            "issuanceDate": "2012-05-15",
            "birthday": "1998-08-22",
        }

    @staticmethod
    def get_payload_for_client(phone_number: str) -> dict:
        return {
            "mobilePhone": phone_number,
            "id": str(uuid.uuid4()),
            "password": get_custom_password(),
            "securityQuestion": "cat name",
            "securityAnswer": "niki",
            "email": f"{phone_number}@mail.ru",
        }

    @staticmethod
    def get_email_for_change_no_valid(expected_email: str) -> dict:
        return {"newEmail": expected_email}

    @staticmethod
    def get_password_for_change_valid(expected_password: str) -> dict:
        return {"newPassword": expected_password}

    @staticmethod
    def get_random_email_for_change(email: str = None, email_len: int = 8) -> dict:
        if email is None:
            return {"newEmail": get_custom_email(email_len)}
        return {"newEmail": email}

    @staticmethod
    def activate_status(status_email: bool) -> dict:
        return {"notificationStatusEmail": status_email}

    @staticmethod
    def get_data_passport_number(passport_number: str) -> dict:
        return {"passportNumber": passport_number}

    @staticmethod
    def get_payload_for_authorization_with_phone(phone_number: str, password: str) -> dict:
        return {"login": phone_number, "password": password, "type": "PHONE_NUMBER"}

    @staticmethod
    def get_payload_for_authorization_with_passport(passport_number: str, password: str) -> dict:
        return {"login": passport_number, "password": password, "type": "PASSPORT_NUMBER"}

    @staticmethod
    def get_payload_for_authorization_with_invalid_data(data: dict) -> dict:
        return {"login": data["login"], "password": data["password"], "type": data["type"]}

    @staticmethod
    def get_payload_for_authorization_with_password(phone_number: str, password: str) -> dict:
        return {"login": phone_number, "password": password, "type": "PHONE_NUMBER"}

    @staticmethod
    def get_payload_for_change_verification_user_data(receiver: str, ver_code: str) -> dict:
        return {"receiver": receiver, "verificationCode": ver_code}

    @staticmethod
    def get_payload_for_change_password_with_access_token(basic_password: str, new_password: str) -> dict:
        return {"password": basic_password, "newPassword": new_password}
