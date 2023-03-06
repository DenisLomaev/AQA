import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import valid_password_ui_python, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@allure.id("C5992946")
@allure.title("C5992946. Авторизация по номеру телефона с валидными данными")
def test_ui_c5992946_authorization_by_phone_valid(browser):
    # Открытие главной страницы
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Нажать на кнопку "По телефону"
    main_page.click_button_by_phone()

    # Нажать на поле "Телефон"
    main_page.click_phone_field()

    # Ввести валидный номер телефона в поле "Телефон"
    main_page.enter_number_in_phone_field(phone=valid_phone_number_ui_python)

    # Нажать на поле ввода "Пароль"
    main_page.click_on_the_password_input_field()

    # Проверяем что Лейбл "Пароль" отображается над полем ввода пароля
    main_page.check_the_password_text_above_the_input_field()

    # Ввести валидный пароль
    main_page.enter_password_in_pass_field(password=valid_password_ui_python)

    # Нажать на кнопку отображения пароля
    main_page.click_on_password_display_button()

    # Нажать на кнопку "Войти"
    main_page.click_button_login()
