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
@allure.id("C6176287")
@allure.title("C6176287. Интерфейс раздела 'Изменить пароль' в табе 'Безопасность' личного кабинета.")
def test_ui_C6176287_check_elements_table_change_password(browser):
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

    # Проверка элементов
    profile_security_page.check_displaying_elements_on_page_change_password("button_back")
    profile_security_page.check_displaying_elements_on_page_change_password("text_header")
    profile_security_page.check_displaying_elements_on_page_change_password("text_header_down")
    profile_security_page.check_displaying_elements_on_page_change_password("field_current_password_locator")
    profile_security_page.check_displaying_elements_on_page_change_password("field_create_new_password_locator")
    profile_security_page.check_displaying_elements_on_page_change_password("field_confirm_new_password_locator")
    profile_security_page.check_displaying_elements_on_page_change_password("button_confirm")
    profile_security_page.check_displaying_elements_on_page_change_password("button_cancel")
