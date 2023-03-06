import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.for_tests.data_C6181473_c6181482 import new_phone_number
from test_framework.ui.data.user_data import valid_password_ui_python, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_settings_page import ProfileSettingsPage


@pytest.mark.ui
@allure.id("C6181473")
@allure.title("C6181473. Проверка изменения номера телефона с валидными данными .")
def test_ui_c6181473_success_change_phone_number_with_valid_data(browser_change_phone_number_after_test):
    # Открытие браузера
    main_page = MainPage(browser_change_phone_number_after_test, MAIN_PAGE_URL)
    main_page.open()
    # Авторизация пользователя
    main_page.authorization(phone_number=valid_phone_number_ui_python, password=valid_password_ui_python)
    # Вход в личный кабинет
    main_page.click_button_account()
    # Переход во вкладку "Настройки"
    profile_setting_page = ProfileSettingsPage(browser_change_phone_number_after_test)
    profile_setting_page.open_profile_options_page()
    main_page.wait_logo_is_clickable()
    # Проверка активности кнопки Сохранить изменеия
    profile_setting_page.check_button_save_changes_is_disable()
    # Нажать на иконку "карандаш"
    profile_setting_page.click_on_button_change_phone_number()
    # Ввести новый номер телефона
    profile_setting_page.enter_new_phone_number_to_phone_number_field(new_phone_number)
    # Нажать на кнопку "Сохранить изменения"
    profile_setting_page.click_on_save_changes_button()
    """На фронте временно отключили данный функционал
           из-за некорректной работы отображения сообщений об изменении поля"""
    # Проверка появления сообщения Номер подтверждён
    profile_setting_page.check_message_success_change_field(
        "message_phone_number_success_changed_locator", "message_success_phone_number_change"
    )
