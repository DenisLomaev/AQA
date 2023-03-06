import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL, link_location_page
from test_framework.ui.data.user_data import valid_password_ui_python, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_settings_page import ProfileSettingsPage


@pytest.mark.ui
@allure.id("C6181560")
@allure.title("C6181560. Проверка ссылок на странице Настройки.")
def test_ui_c6181560_check_links_in_settings_page(browser):
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
    # Проверка работоспособности ссылки в блоке мой аккаунт
    profile_setting_page.click_on_link("link_how_deactivate_account_locator")
    profile_setting_page.check_page_after_link_click(link_location_page)
    # Возврат на страницу настроек
    main_page.click_button_account()
    profile_setting_page.open_profile_options_page()
    main_page.wait_logo_is_clickable()
    # Проверка работоспособности ссылки в блоке сменить имя
    profile_setting_page.click_on_link("link_in_change_fio_block_locator")
    # Возврат на страницу настроек
    main_page.click_button_account()
    profile_setting_page.open_profile_options_page()
    main_page.wait_logo_is_clickable()
    # Проверка работоспособности ссылки в блоке смена ФИО по иным причинам
    profile_setting_page.click_on_link("link_other_way_to_change_fio_block_locator")
