import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import valid_password_universal, valid_phone_number_universal_for_UI
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)
from test_framework.ui.pages.personal_profile_pages.profile_security_page import ProfileSecurityPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6178841")
@allure.title(
    "C6178841. "
    "Невалидные граничные значения полей 'Введите текущий пароль', 'Задайте новый пароль', 'Подтвердите новый пароль'."
)
def test_ui_C6178841_check_message_after_put_password_on_page_change_password(browser):

    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Авторизация пользователя
    main_page.authorization(phone_number=valid_phone_number_universal_for_UI, password=valid_password_universal)

    # Вход в личный кабинет
    profile_page = ProfileMainPage(browser, url=browser.current_url)
    profile_page.open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    profile_info = ProfileGeneralInformationPage(browser, url=browser.current_url)
    profile_info.open_profile_security_page()

    # Клик на кнопку "Изменить пароль"
    profile_security_page = ProfileSecurityPage(browser, url=browser.current_url)
    profile_security_page.click_on_button_change_password()

    # Проверка с 5 символами
    # Ввод пароля и проверка сообщения в поле Введите текущий пароль
    profile_security_page.enter_current_password("Aa123")
    profile_security_page.click_field_new_password()
    profile_security_page.check_message_validation_password("text_validation_password_locator")

    # Ввод пароля и проверка сообщения в поле Введите новый пароль
    profile_security_page.enter_new_password("Aa123")
    profile_security_page.click_field_current_password()
    profile_security_page.check_message_validation_password("text_validation_password_locator_under_new_password")

    # Ввод пароля и проверка сообщения в поле Подтвердите введенный пароль
    profile_security_page.enter_confirm_new_password("Aa123")
    profile_security_page.click_field_current_password()
    profile_security_page.check_message_validation_password("text_message_missmatch_passwords_locator")

    # Клик на кнопку "Отменить"
    profile_security_page.click_button_cancel_data_on_page_change_password()

    # Проверка с 21 символами
    # Ввод паролей
    profile_security_page.enter_current_password("12As4jasRt12345)/asd1")
    profile_security_page.enter_new_password("12As4jasRt12345)/asd1")
    profile_security_page.enter_confirm_new_password("12As4jasRt12345)/asd1")

    # Проверка полей, на несоответсвие введенному значению
    profile_security_page.check_fields_on_page_change_password_not_equals(
        "field_current_password_locator", "12As4jasRt12345)/asd1"
    )
    profile_security_page.check_fields_on_page_change_password_not_equals(
        "field_create_new_password_locator", "12As4jasRt12345)/asd1"
    )
    profile_security_page.check_fields_on_page_change_password_not_equals(
        "field_confirm_new_password_locator", "12As4jasRt12345)/asd1"
    )
