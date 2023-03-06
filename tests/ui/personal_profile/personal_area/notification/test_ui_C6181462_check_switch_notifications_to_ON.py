import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import valid_password_universal, valid_phone_number_universal_for_UI
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)
from test_framework.ui.pages.personal_profile_pages.profile_notifications_page import ProfileNotificationPage


@pytest.mark.xfail
@pytest.mark.ui
@allure.id("C6181462")
@allure.title("C6181462 Проверка переключения switcher-ов на ON")
def test_ui_c6181462_check_switch_notifications_to_off(browser):
    # Открытие главной страницы
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()
    # Авторизаци пользователя
    main_page.authorization(phone_number=valid_phone_number_universal_for_UI, password=valid_password_universal)
    # Переход в личный кабинет
    main_page.click_button_account()
    # Переход во вкладку "Настройки"
    profile_notification_page = ProfileNotificationPage(browser)
    profile_notification_page.open_profile_options_page()
    main_page.wait_logo_is_clickable()
    # Переключить чекбокс Email Рассылка на ON
    profile_notification_page.click_checkbox_email_notification()
    # Проверка переключение чекбокса Email на ON
    profile_notification_page.check_notification_checkbox_switch("label_email_notification_locator", "ON")
    # Переключить чекбокс SMS Рассылка на ON
    profile_notification_page.click_checkbox_sms_notification()
    # Проверка переключение чекбокса SMS на ON
    profile_notification_page.check_notification_checkbox_switch("label_sms_notification_locator", "ON")
    # Переключить чекбокс Push Рассылка на ON
    profile_notification_page.click_checkbox_push_notification()
    # Проверка переключение чекбокса Push на ON
    profile_notification_page.check_notification_checkbox_switch("label_push_notification_locator", "ON")
    # Переместиться на вкладку Безопасность
    profile_page = ProfileGeneralInformationPage(browser)
    profile_page.open_profile_security_page()
    # Переместиться на вкладку Настройки
    profile_notification_page.open_profile_options_page()
    # Убедиться что переключатели на ON
    profile_notification_page.check_notification_checkbox_switch("label_email_notification_locator", "ON")
    profile_notification_page.check_notification_checkbox_switch("label_sms_notification_locator", "ON")
    profile_notification_page.check_notification_checkbox_switch("label_push_notification_locator", "ON")
