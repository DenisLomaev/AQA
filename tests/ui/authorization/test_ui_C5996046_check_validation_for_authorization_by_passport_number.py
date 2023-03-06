import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.for_tests.data_c5996046 import invalid_passport_number_9_digits as test_data
from test_framework.ui.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@allure.id("C5996046")
@allure.title("C5996046. Проверка валидации при вводе номера паспорта")
def test_ui_c5996046_check_validation_for_authorization_by_passport_number(browser):
    # Открытие главной страницы
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Клик на кнопку "По паспорту"
    main_page.click_button_by_passport()

    # Клик на поле 'Паспорт'
    main_page.click_passport_field()

    # Ввести в поле ввода номера паспорта цифры в количестве меньше 10 цифр
    main_page.enter_on_the_passport_number_entry_field(passport_number=test_data)

    # Клик на поле ввода пароля
    main_page.click_on_the_password_input_field()

    # Проверка отображения сообщения "Недостаточно символов"
    main_page.check_message_not_enough_characters()
