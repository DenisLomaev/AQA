import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.for_tests.data_C6181467_C6181496 import new_phone_number, valid_email
from test_framework.ui.data.user_data import (
    valid_email_ui_python,
    valid_password_ui_python,
    valid_phone_number_ui_python,
)
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_settings_page import ProfileSettingsPage


@pytest.mark.ui
@allure.id("C6181496")
@allure.title("C6181496. Отмена изменений в поле email и Номер телефона.")
def test_ui_c6181496_cancel_change_email_and_phone_number(browser):
    # Открытие браузера
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()
    # Авторизация пользователя
    main_page.authorization(phone_number=valid_phone_number_ui_python, password=valid_password_ui_python)
    # Вход в личный кабинет
    main_page.click_button_account()
    # Переход во вкладку "Настройки"
    profile_setting_page = ProfileSettingsPage(browser)
    profile_setting_page.open_profile_options_page()
    main_page.wait_logo_is_clickable()
    # Нажать на иконку "карандаш"
    profile_setting_page.click_on_button_change_email()
    # Отредактировать существующий email валидными данными.
    profile_setting_page.enter_new_email_to_email_field(valid_email)
    # Нажать на кнопку сбросить изменения
    profile_setting_page.click_on_dismiss_changes_button()
    # Проверка отмены изменений в поле Email
    profile_setting_page.check_user_email_in_email_field_equals(valid_email_ui_python)
    # Нажать на иконку "карандаш"
    profile_setting_page.click_on_button_change_phone_number()
    # Отредактировать существующий номер телефона валидными данными.
    profile_setting_page.enter_new_phone_number_to_phone_number_field(new_phone_number)
    # Нажать на кнопку сбросить изменения
    profile_setting_page.click_on_dismiss_changes_button()
    # Проверка отмены изменений в поле Номер телефона
    profile_setting_page.check_user_phone_number_in_phone_number_field_equals("+7" + valid_phone_number_ui_python)
