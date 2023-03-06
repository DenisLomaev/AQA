from typing import Any

import allure

from app_data.api.requests_for_api.requests_client import RequestsForTestSait, main_headers
from config import verification_interval, verification_timeout
from test_data.api.api_data import DataClient
from test_framework.api.api_checkers.checkers import CheckersApi
from test_framework.helpers.main_checkers import CommonChecker, checker_exception
from test_framework.helpers.waiter import step_waiter


class ApiSteps:
    def __init__(self) -> None:
        self.request = RequestsForTestSait()
        self.checker = CheckersApi()
        self.data = DataClient()

    @allure.step("Получение всей информации по id")
    def get_all_information_from_sait_by_access_token(self):
        request = self.request.get_info_about_client()
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось получить информацию о клиенте")
        return request

    @allure.step("Получение информации")
    def get_all_information_client_by_phone(self, phone: str) -> Any:
        response = self.request.get_all_information_from_sait(phone)
        CommonChecker.check_status_code_ok(response)
        return response

    @allure.step("Получение ID не киента банка")
    def add_new_user_no_client_with_check_status_code(self, phone: str) -> Any:
        payload = self.data.get_payload_for_no_client(phone)
        response = self.request.reg_no_client(payload)
        CommonChecker.check_status_code_201(response)
        return response

    @allure.step("Получение ID не киента банка")
    def add_new_client_with_check_status_code(self, phone: str) -> Any:
        payload = self.data.get_payload_for_client(phone)
        response = self.request.reg_client(payload)
        CommonChecker.check_status_code_201(response, assertion_message="Не удалось зарегистрировать клиента клиента")
        return response

    @allure.step("Получение ID не киента банка")
    def add_new_client_with_random_value_and_check_status_code(self, phone_number: str, password: str) -> Any:
        payload = self.data.get_random_payload_for_no_client(phone_number, password)
        response = self.request.reg_no_client(payload)
        CommonChecker.check_status_code_201(response, assertion_message="Не удалось зарегистрировать клиента клиента")
        return response

    @allure.step("Получение номера телефона по номеру паспорта")
    def get_phone_number_by_passport_without_check(self, passport_number: str, payload: dict = None) -> Any:
        if payload is None:
            payload = self.data.get_data_passport_number(passport_number)
        return self.request.get_phone_number_by_passport(payload)

    @allure.step("Получение номера телефона по номеру паспорта")
    def get_phone_number_by_passport(self, passport_number: str, payload: dict = None) -> Any:
        request = self.get_phone_number_by_passport_without_check(passport_number, payload)
        CommonChecker.check_status_code_ok(
            request, assertion_message="Не удалось получить номер телефона по номеру паспорта"
        )
        return request

    @allure.step("Получение кода верификации по номеру телефона")
    def get_verification_code_by_phone(self, phone: str) -> Any:
        request = self.request.get_verification_code_by_phone(phone)
        CommonChecker.check_status_code_ok(
            request, assertion_message="Не удалось получить код верификации по номеру телефона"
        )
        return request

    @allure.step("Получение кода верификации по номеру телефона и проверки с ожиданием")
    @step_waiter(verification_timeout, verification_interval)
    @checker_exception
    def get_verification_code_by_phone_wait_it_in_response(self, phone: str) -> str:
        request_json = self.get_verification_code_by_phone(phone).json()
        CommonChecker.check_key_in_collection("code", request_json)
        return request_json["code"]

    @allure.step("Получения кода ошибки при попытке верификации по номеру телефона")
    def get_verification_code_by_invalid_phone(self, phone: str) -> Any:
        request = self.request.get_verification_code_by_phone(phone)
        CommonChecker.check_status_code_400(
            request, assertion_message="Удалось получить код верификации по неправильному номеру телефона"
        )

    @allure.step("Получения кода ошибки при попытке верификации по номеру телефона")
    def get_verification_code_by_non_existent_phone(self, phone: str) -> Any:
        request = self.request.get_verification_code_by_phone(phone)
        CommonChecker.check_status_code_400(
            request, assertion_message="Удалось получить код верификации по неправильному номеру телефона"
        )

    @allure.step("Верификация юзера")
    def verification_user(self, phone_number: str, ver_code: str) -> Any:
        payload = self.data.get_payload_for_change_verification_user_data(phone_number, ver_code)
        request = self.request.verification_user_with_valid_ver_code(payload)
        return request

    @allure.step("Верификация юзера с проверкой статус кода 200")
    def verification_user_with_check_status_code_ok(self, phone_number: str, ver_code: str) -> None:
        response = self.verification_user(phone_number, ver_code)
        CommonChecker.check_status_code_ok(response, assertion_message="Не удалось верифицировать пользователя")

    @allure.step("Верификация юзера, с невалидным кодом верификации")
    def verification_user_with_check_status_code_406(self, phone_number: str, ver_code: str) -> Any:
        response = self.verification_user(phone_number, ver_code)
        CommonChecker.check_status_code_406(response, assertion_message="Удалось авторизовать пользователя")

    @allure.step("Получение токена авторизации")
    def get_authorization_token_by_phone(self, phone_number: str, password: str) -> Any:
        payload = self.data.get_payload_for_authorization_with_phone(phone_number, password)
        request = self.request.get_authorization_token(payload)
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось получить токен авторизации")
        return request

    @allure.step("Авторизация по номеру телефона и паролю")
    def authorization_by_phone_and_password(self, phone_number, password: str) -> str:
        request_json = self.get_authorization_token_by_phone(phone_number, password).json()
        CommonChecker.check_key_in_collection(
            "accessToken", request_json, assertion_message="Отсутствует поле 'accessToken'"
        )
        access_token: str = request_json["accessToken"]
        self.request.headers["authorization"] = "Bearer " + access_token
        return request_json

    @allure.step("Получение токена авторизации")
    def get_authorization_token_by_passport(self, passport_number: str, password: str) -> Any:
        payload = self.data.get_payload_for_authorization_with_passport(passport_number, password)
        request = self.request.get_authorization_token(payload)
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось получить токен авторизации")
        return request

    @allure.step("Авторизация по номеру паспорта")
    def authorization_by_passport(self, passport_number, password) -> str:
        request_json = self.get_authorization_token_by_passport(passport_number, password).json()
        CommonChecker.check_key_in_collection(
            "accessToken", request_json, assertion_message="Отсутствует поле 'accessToken'"
        )
        access_token: str = request_json["accessToken"]
        self.request.headers["authorization"] = "Bearer " + access_token
        return access_token

    @allure.step("Попытка получение токена авторизации")
    def get_authorization_token_by_invalid_data(self, data: dict) -> Any:
        payload = self.data.get_payload_for_authorization_with_invalid_data(data)
        request = self.request.get_authorization_token(payload)
        CommonChecker.check_status_code_400(
            request, assertion_message="Удалось получить токен с невалидными значениями"
        )

    @allure.step("Изменение почты клиента на невалидное значение с валидным токеном")
    def get_email_changed_with_no_valid_data(self, client_id, expected_email) -> Any:
        payload = self.data.get_email_for_change_no_valid(expected_email)
        request = self.request.update_email(client_id, payload)
        CommonChecker.check_status_code_400(request, assertion_message="Удалось обновить email невалидным значением")
        return request

    @allure.step("Изменение почты клиента не авторизованным пользователем")
    @step_waiter(20, 2)
    @checker_exception
    def get_email_changed_no_authorization(self, client_id, email: str = "unknow123@mail.ru") -> Any:
        payload = self.data.get_random_email_for_change(email)
        request = self.request.update_email(client_id, payload)

        CommonChecker.check_status_code_400(request, assertion_message="Удалось обновить email не авторизованным")

    @allure.step("Изменение почты на рандомную почту клиента с валидным токеном")
    def get_random_email_changed_with_valid_data(self, client_id: str, random_email: str = None) -> Any:
        payload = self.data.get_random_email_for_change(random_email)
        request = self.request.update_email(client_id, payload)
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось обновить email пользователя")

    @allure.step("Изменение почты клиента с валидным токеном")
    def get_email_changed_with_invalid_data(self, client_id, email=None, email_len=8) -> Any:
        payload = self.data.get_random_email_for_change(email, email_len)
        request = self.request.update_email(client_id, payload)
        CommonChecker.check_status_code_400(request, assertion_message="Удалось обновить email пользователя")

    @allure.step("Изменение пароля клиента")
    def change_user_password(self, phone_number: str, password: str) -> Any:
        payload = self.data.get_password_for_change_valid(password)
        request = self.request.get_set_new_password_by_phone(phone_number, payload)
        return request

    @allure.step("Изменение пароля с валидными данными по номеру телефона")
    def success_change_user_password(self, valid_phone_number: str, password: str) -> Any:
        response = self.change_user_password(valid_phone_number, password)
        CommonChecker.check_status_code_ok(response, assertion_message="Не удалось изменить пароль по номеру телефона")
        return response

    @allure.step("Изменение пароля с невалидными данными по номеру телефона")
    def failed_change_user_password(self, valid_phone_number, password: str) -> Any:
        response = self.change_user_password(valid_phone_number, password)
        CommonChecker.check_status_code_400(response, assertion_message="Удалось изменить пароль по номеру телефона")
        return response

    @allure.step("Изменение пароля с авторизованным пользователем")
    def change_password_with_authorization_user(self, password: str, new_password: str) -> Any:
        payload = self.data.get_payload_for_change_password_with_access_token(password, new_password)
        request = self.request.change_password_with_access_token(payload)
        return request

    @allure.step("Изменение пароля по акксес токену с правильным паролем")
    def change_password_with_auth_user_and_valid_password(self, password: str, new_password: str) -> Any:
        response = self.change_password_with_authorization_user(password, new_password)
        CommonChecker.check_status_code_ok(response, assertion_message="Не удалось изменить пароль")
        return response

    @allure.step("Изменение пароля по акксес токену с неправильным паролем")
    def change_password_with_auth_user_and_invalid_password(self, password: str, new_password: str) -> Any:
        response = self.change_password_with_authorization_user(password, new_password)
        CommonChecker.check_status_code_400(response, assertion_message="Удалось изменить пароль")
        return response

    @allure.step("Получение статусов уведомлений по id клиента")
    def get_status_notification_by_id(self, id_client: str) -> Any:
        request = self.request.get_info_about_notification_by_id(id_client)
        CommonChecker.check_status_code_ok(
            request, assertion_message="Не удалось получить информацию о статусах уведомлений"
        )
        return request

    @allure.step("Получение статусов уведомлений по id клиента с полной проверкой ответа")
    def get_status_notification_by_id_with_all_check(self, id_client: str) -> Any:
        response_json = self.get_status_notification_by_id(id_client).json()
        self.checker.checker_satus_notifications(response_json)
        return response_json

    @allure.step("Получение статусов уведомлений по id клиента без авторизации")
    def get_status_notification_by_id_without_authorization(self, id_client: str) -> Any:
        request = self.request.get_info_about_notification_by_id(id_client)
        CommonChecker.check_status_code_400(request, assertion_message="Неверный статус ответа")

    @allure.step("Получение статусов уведомлений по id клиента")
    def get_status_notification_by_invalid_id(self, id_client: str) -> Any:
        request = self.request.get_info_about_notification_by_invalid_id(id_client)
        CommonChecker.check_status_code_400(
            request, assertion_message="Не удалось получить информацию о статусах уведомлений"
        )
        return request

    @allure.step("Удаление токена, logout пользователя")
    def logout_user(self) -> Any:
        request = self.request.logout_user_token()
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось удалить токен авторизации")
        del main_headers["authorization"]
        return request

    @allure.step("Изменение статуса пользователя на Active")
    def changing_client_status(self, status: str):
        request = self.request.update_client_status_in_active(status)
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось изменить статус")
        return request

    @allure.step("Получение информации о клиенте")
    def get_all_info_about_user_by_access_token(self) -> Any:
        request = self.request.get_all_information_from_sait_by_token()
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось получить информацию об email клиента")
        return request

    @allure.step("Изменение статуса рассылки на {status_email}")
    def update_subscription_status_email(self, client_id: str, status_email: bool) -> Any:
        payload = self.data.activate_status(status_email)
        request = self.request.update_subscription_status(client_id, payload)
        return request

    @allure.step("Изменение статуса рассылки на {status_email} с проверкой 200 статус кода")
    def update_subscription_status_to_active_with_check_status_ok(self, client_id: str, status_email: bool) -> Any:
        request = self.update_subscription_status_email(client_id, status_email)
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось обновить статус пользователя")

    @allure.step("Изменение статуса рассылки на {status_email} с проверкой 400 статус кода")
    def update_subscription_status_email_with_check_status_400(self, client_id, status_email: bool) -> Any:
        request = self.update_subscription_status_email(client_id, status_email)
        CommonChecker.check_status_code_400(request, assertion_message="Удалось обновить статус пользователя")

    @allure.step("Удаление токена, logout пользователя без headers")
    def logout_user_with_wrong_request(self) -> Any:
        request = self.request.logout_user_token_without_headers()
        CommonChecker.check_status_code_400(request, assertion_message="Удалось удалить токен авторизации")
        return request

    @allure.step("Изменение секретного вопроса")
    def change_security_question_with_valid_value(self, basic_question: str, new_question: str):
        payload = self.data.get_payload_for_change_verification_user_data(basic_question, new_question)
        request = self.request.change_security_question(payload)
        CommonChecker.check_status_code_ok(request, assertion_message="Секретный вопрос не изменен")
