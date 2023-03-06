import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@allure.id("C5993285")
@allure.title("C5993285. Появление предупреждающего сообщения о включенном CapsLock при вводе пароля")
def test_ui_c5993285_displaying_warning_message_on_turned_capslock(browser):
    # Открытие главной страницы
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Нажать на поле ввода "Пароль"
    main_page.click_on_the_password_input_field()

    # Нажатие клавиши CapsLock
    main_page.turn_on_capslock()

    # Проверка появления сообщения "Включен CapsLock"
    main_page.check_message_about_on_turned_capslock()

    # Нажатие клавиши CapsLock
    main_page.turn_on_capslock()

    # Проверка не отображения сообщения "Включен CapsLock"
    main_page.check_no_message_about_on_turned_capslock()
