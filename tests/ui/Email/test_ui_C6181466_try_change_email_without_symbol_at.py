import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import valid_password_universal, valid_phone_number_universal_for_UI
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_settings_page import ProfileSettingsPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6178891")
@allure.title("C6178891. Проверка статуса 'Адрес не подтвержден' при редактировании email..")
def test_C6181466_try_change_email_without_symbol_at(browser):
    # Переменная без символа "@"
    email_without_at = "asdr1289mail.ru"

    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Авторизация пользователя
    main_page.authorization(phone_number=valid_phone_number_universal_for_UI, password=valid_password_universal)

    # Вход в личный кабинет
    profile_page = ProfileMainPage(browser)
    profile_page.open_profile_general_information_page()

    # Вход во вкладку настройки
    profile_settings_page = ProfileSettingsPage(browser)
    profile_settings_page.open_profile_options_page()

    # Клик на кнопку "Карандаш"
    profile_settings_page.click_on_button_change_email()

    # Очистка поля Еmail и ввод нового Email
    profile_settings_page.enter_new_email_to_email_field(email_without_at)

    # Сохраняем изменения
    profile_settings_page.click_on_save_changes_button()

    """На фронте временно отключили данный функционал
           из-за некорректной работы отображения сообщений об изменении поля"""
    # Проверка сообщения об ошибке
    profile_settings_page.check_message_not_change_email()
