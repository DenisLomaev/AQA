import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import valid_password_universal, valid_phone_number_universal_for_UI
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6174388")
@allure.title("C6174388 Проверка появления формы регистрации после выхода из профиля")
def test_ui_c6174388_open_main_page_registration_form_after_logout(browser):
    # Открытие браузера
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()
    # Авторизаци пользователя
    main_page.authorization(phone_number=valid_phone_number_universal_for_UI, password=valid_password_universal)
    # Выход пользователя
    profile_page = ProfileMainPage(browser)
    profile_page.click_button_logout()
    # Проверка появления формы регистрации
    main_page.check_main_page_after_reload()
