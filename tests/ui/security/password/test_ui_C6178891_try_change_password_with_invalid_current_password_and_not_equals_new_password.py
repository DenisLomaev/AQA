import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import (
    password,
    valid_password_autofirstnametest,
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
@allure.id("C6178891")
@allure.title(
    "C6178891. "
    "Изменение пароля: данные поля 'Подтвердите новый пароль' не совпадают с данными поля 'Задайте новый пароль'."
)
def test_ui_C6178891_try_change_password_with_invalid_current_password_and_not_equals_new_password(browser):
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

    # Ввод одного символа во все поля
    profile_security_page.enter_current_password(valid_password_autofirstnametest)
    profile_security_page.enter_new_password(password)
    profile_security_page.enter_confirm_new_password(valid_password_autofirstnametest)

    # Клик на пусток поле
    profile_security_page.click_field_current_password()

    # Проверка появления сообщения "Пароли не совподают"
    profile_security_page.check_message_mismatch_password()
