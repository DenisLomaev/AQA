import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.for_tests.data_c6181469_c6181470 import invalid_email, valid_email
from test_framework.ui.data.user_data import valid_password_ui_python, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_settings_page import ProfileSettingsPage


@pytest.mark.ui
@allure.id("c6181470")
@allure.title("c6181470. Проверка изменения email с невалидными данными граничные значения.")
def test_ui_c6181470_check_email_change_invalid_border_data(browser_change_email_after_test):
    # Открытие браузера
    main_page = MainPage(browser_change_email_after_test, MAIN_PAGE_URL)
    main_page.open()
    # Авторизация пользователя
    main_page.authorization(phone_number=valid_phone_number_ui_python, password=valid_password_ui_python)
    # Вход в личный кабинет
    main_page.click_button_account()
    # Переход во вкладку "Настройки"
    profile_setting_page = ProfileSettingsPage(browser_change_email_after_test)
    profile_setting_page.open_profile_options_page()
    main_page.wait_logo_is_clickable()
    # Нажать на иконку "карандаш"
    profile_setting_page.click_on_button_change_email()
    # Проверка активности кнопки "Сохранить изменения"
    profile_setting_page.check_button_save_changes_is_disable()
    # Отредактировать существующий email валидными данными.
    profile_setting_page.enter_new_email_to_email_field(valid_email)
    # Проверка активности кнопки "Сохранить изменения"
    profile_setting_page.check_button_save_changes_is_disable()
    # Нажать на кнопку "Сохранить изменения".
    profile_setting_page.click_on_save_changes_button()
    # Проверка появления статуса "Адрес подтверждён".
    profile_setting_page.check_message_success_change_email()
    # Нажать на иконку "карандаш"
    profile_setting_page.click_on_button_change_email()
    # Отредактировать существующий email невалидными данными.
    profile_setting_page.enter_new_email_to_email_field(invalid_email)
    # Проверка активности кнопки "Сохранить изменения"
    profile_setting_page.check_button_save_changes_is_disable()
    # Нажать на кнопку "Сохранить изменения".
    profile_setting_page.click_on_save_changes_button()
    """На фронте временно отключили данный функционал
           из-за некорректной работы отображения сообщений об изменении поля"""
    # Проверка сообщения об ошибке
    profile_setting_page.check_message_not_change_email()
