from typing import Any

import app_data.api.base_requests
from test_data.api.data_url import MainURL

main_headers = {"Fingerprint": "Aaa"}


class RequestsForTestSait:
    def __init__(self) -> None:
        self.request = app_data.api.base_requests.BaseRequests()
        self.base_url = MainURL().get_url_from_dict("base_url")
        self.headers = main_headers

    def get_all_information_from_sait(self, valid_phone_number_no_client: str) -> Any:
        return self.request.get(url=f"{self.base_url}/api/v1/registration?mobilePhone={valid_phone_number_no_client}")

    def reg_no_client(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}/api/v1/registration/user-profile/new/", json=payload)

    def reg_client(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}/api/v1/registration/user-profile/", json=payload)

    def get_phone_number_by_passport(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}/api/v1/security/session", json=payload)

    def get_verification_code_by_phone(self, phone: str) -> Any:
        return self.request.get(url=f"{self.base_url}/api/v1/security/session?receiver={phone}", headers=self.headers)

    def get_authorization_token(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}/api/v1/login/", headers=self.headers, json=payload)

    def update_email(self, client_id: str, payload: dict) -> Any:
        return self.request.patch(
            url=f"{self.base_url}/api/v1/user/settings/email?clientId={client_id}", headers=self.headers, json=payload
        )

    def update_subscription_status(self, client_id: str, payload: dict) -> Any:
        return self.request.patch(
            url=f"{self.base_url}/api/v1/user/settings/notifications/email?clientId={client_id}",
            headers=self.headers,
            json=payload,
        )

    def changing_email_with_wrong_address(self, client_id: str, payload: dict, headers) -> Any:
        return self.request.patch(
            url=f"{self.base_url}/api/v1/user/settings/email?clientId={client_id}", headers=headers, json=payload
        )

    def get_set_new_password_by_phone(self, phone_number: str, payload: dict) -> Any:
        return self.request.patch(
            url=f"{self.base_url}/api/v1/login/password?mobilePhone={phone_number}", headers=self.headers, json=payload
        )

    def get_info_about_notification_by_id(self, id_client: str) -> Any:
        return self.request.get(
            url=f"{self.base_url}/api/v1/user/settings/notifications/all?clientId={id_client}", headers=self.headers
        )

    def get_info_about_notification_by_invalid_id(self, id_client: str) -> Any:
        return self.request.get(
            url=f"{self.base_url}/api/v1/user/settings/notifications/all?clientId={id_client}", headers=self.headers
        )

    def logout_user_token(self) -> Any:
        return self.request.get(url=f"{self.base_url}/api/v1/logout", headers=self.headers)

    def update_client_status_in_active(self, status: str) -> Any:
        return self.request.patch(
            url=f"{self.base_url}/api/v1/test/change-client-status/?status={status}", headers=self.headers
        )

    def get_all_information_from_sait_by_token(self) -> Any:
        return self.request.get(url=f"{self.base_url}/api/v1/user/info", headers=self.headers)

    def logout_user_token_without_headers(self) -> Any:
        return self.request.get(url=f"{self.base_url}/api/v1/logout")

    def get_info_about_client(self) -> Any:
        return self.request.get(url=f"{self.base_url}/api/v1/user/info", headers=self.headers)

    def verification_user_with_valid_ver_code(self, payload: dict) -> Any:
        return self.request.post(
            url=f"{self.base_url}/api/v1/security/session/verification/", headers=self.headers, json=payload
        )

    def change_security_question(self, payload: dict) -> Any:
        return self.request.patch(
            url=f"{self.base_url}/api/v1/user/settings/controls", headers=self.headers, json=payload
        )

    def change_password_with_access_token(self, payload: dict) -> Any:
        return self.request.patch(
            url=f"{self.base_url}/api/v1/user/settings/password", headers=self.headers, json=payload
        )
