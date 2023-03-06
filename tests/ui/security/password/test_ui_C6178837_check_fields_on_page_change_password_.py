import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import (
    invalid_data_for_change_password,
    valid_password_universal,
    valid_phone_number_universal_for_UI,
)
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)
from test_framework.ui.pages.personal_profile_pages.profile_security_page import ProfileSecurityPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@pytest.mark.parametrize("expected_password", invalid_data_for_change_password)
@allure.id("C6178837")
@allure.title(
    "C6178837. "
    "Валидные граничные значения полей 'Введите текущий пароль', 'Задайте новый пароль', 'Подтвердите новый пароль'."
)
def test_ui_C6178837_check_fields_on_page_change_password_with_invalid_data(browser, expected_password):
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

    # Ввод паролей
    profile_security_page.enter_current_password(expected_password)
    profile_security_page.enter_new_password(expected_password)
    profile_security_page.enter_confirm_new_password(expected_password)

    # Проверка, что поля заполнены
    profile_security_page.check_fields_value("field_current_password_locator", expected_password)
    profile_security_page.check_fields_value("field_create_new_password_locator", expected_password)
    profile_security_page.check_fields_value("field_confirm_new_password_locator", expected_password)
