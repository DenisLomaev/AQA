import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import password, valid_passport_number
from test_framework.ui.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@allure.id("C5994513")
@allure.title("C5994513. Авторизация по номеру паспорта с валидными данными")
def test_ui_c5994513_authorization_by_passport_valid(browser):
    # Открытие главной страницы
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Нажать на кнопку "По паспорту"
    main_page.click_button_by_passport()

    # Нажать на поле "Номер паспорта"
    main_page.click_on_the_passport_number_entry_field()

    # Проверяем что Лейбл "Паспорт" отображается над полем ввода номера паспорта
    main_page.check_the_passport_text_above_the_input_field()

    # Вводим валидный номер паспорта в поле "Паспорт"
    main_page.enter_on_the_passport_number_entry_field(passport_number=valid_passport_number)

    # Нажать на поле ввода "Пароль"
    main_page.click_on_the_password_input_field()

    # Проверяем что Лейбл "Пароль" отображается над полем ввода пароля
    main_page.check_the_password_text_above_the_input_field()

    # Ввести валидный пароль
    main_page.enter_password_in_pass_field(password=password)

    # Нажать на кнопку "Войти"
    main_page.click_button_login()
