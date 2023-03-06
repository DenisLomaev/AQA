import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@allure.id("C5994515")
@allure.title("C5994515. Появление валидации при введении некорректного пароля")
def test_ui_c5994515_check_password_validation(browser):
    # Открытие главной страницы
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Нажать на поле "Пароль"
    main_page.click_on_the_password_input_field()

    # Проверяем что Лейбл "Пароль" отображается над полем ввода пароля
    main_page.check_the_password_text_above_the_input_field()

    # Ввести невалидный пароль в поле ввода пароля
    main_page.enter_password_in_pass_field(password="1231231")

    # Проверка неактивного статуса кнопки "Войти"
    main_page.check_status_button_login_disabled()

    # Клик на поле ввода телефона
    main_page.click_phone_field()

    # Проверка отображения уведомления о валидации пароля
    main_page.check_message_validation_password()
