import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import valid_password_universal, valid_phone_number_universal_for_UI
from test_framework.ui.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@allure.id("C6176275")
@allure.title("C6176275 Авторизация по номеру телефона и переход в личный кабинет")
def test_ui_c6176275_authorization_and_switch_to_personal_profile(browser):
    # Открытие главной страницы
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()
    # Нажать на кнопку "по телефону"
    main_page.click_button_by_phone()
    # Нажать на поле "Телефон"
    main_page.click_phone_field()
    # Ввести валидный номер телефона в поле "Телефон"
    main_page.enter_number_in_phone_field(phone=valid_phone_number_universal_for_UI)
    # Нажать на поле "Пароль"
    main_page.click_on_the_password_input_field()
    # Ввести валидный пароль
    main_page.enter_password_in_pass_field(password=valid_password_universal)
    # Нажать на кнопку отображение пароля
    main_page.click_on_password_display_button()
    # Нажать на кнопку "Войти"
    main_page.click_button_login()
    # Нажать на кнопку "Аккаунт+имя"
    main_page.click_button_account()
