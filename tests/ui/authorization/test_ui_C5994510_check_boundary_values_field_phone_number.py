import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.for_tests.data_c5994510 import four_digit, one_digit
from test_framework.ui.data.user_data import valid_password_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@allure.id("C5994510")
@allure.title("C5994510. Проверка граничных значений поля ввода номера телефона")
def test_ui_c5994510_check_boundary_values_field_phone_number(browser):
    # Открытие главной страницы
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Нажать на кнопку "По телефону"
    main_page.click_button_by_phone()

    # Ввести валидный пароль в поле ввода пароля
    main_page.enter_password_in_pass_field(password=valid_password_ui_python)

    # Кнопка "Войти" неактивна
    main_page.check_status_button_login_disabled()

    # Нажать на поле ввода номера телефона
    main_page.click_phone_field()

    # Ввести 1 цифру
    main_page.enter_number_in_phone_field(phone=one_digit)

    # Кнопка "Войти" неактивна
    main_page.check_status_button_login_disabled()

    # Ввести 4 цифры
    main_page.enter_number_in_phone_field(phone=four_digit)

    # Кнопка "Войти" неактивна
    main_page.check_status_button_login_disabled()

    # Ввести 4 цифры
    main_page.enter_number_in_phone_field(phone=four_digit)

    # Кнопка "Войти" неактивна
    main_page.check_status_button_login_disabled()

    # Ввести 1 цифру
    main_page.enter_number_in_phone_field(phone=one_digit)

    # Проверка активности кнопки "Войти"
    main_page.check_active_button_login()

    # Ввести 1 цифру
    main_page.enter_number_in_phone_field(phone=one_digit)

    # Проверка не отображания последней введенной цифры
    main_page.check_entered_digits_phone_field()

    # Нажать на кнопку "Войти"
    main_page.click_button_login()
