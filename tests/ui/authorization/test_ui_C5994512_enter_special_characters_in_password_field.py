import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.helpers.data_generation import get_custom_password_punctuation_only
from test_framework.ui.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@allure.id("C5994512")
@allure.title("C5994512. Возможность ввода в поле ввода пароля спец.символов")
def test_ui_c5994512_enter_special_characters_in_password_field(browser):
    # Открытие главной страницы
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Нажать на поле ввода пароля.
    main_page.click_on_the_password_input_field()

    # Ввести все возможные специальные символы, включая пробелы.
    main_page.enter_password_in_pass_field(password=get_custom_password_punctuation_only(10))

    # Проверка не отображания введеных букв и спец.символов в поле ввода номера паспорта
    main_page.check_no_entered_special_characters_in_password_field()
