import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import password, valid_phone_number
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6042527")
@allure.title("C6042527. Просмотр информации о кредитных продуктах")
def test_ui_c6032396_changing_password_in_profile_security(browser):
    # Открытие главной страницы банка
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Авторизация
    main_page.authorization(phone_number=valid_phone_number, password=password)

    # Переход в личный кабинет(профиль)
    main_page.click_logo_gor()

    # Выбираем раздел кредиты в Меню
    profile_main_page = ProfileMainPage(browser, url=browser.current_url)
    profile_main_page.click_on_credits_section()

    # Выбираем раздел кредитные продукты
    profile_main_page.click_on_credits_product()

    # To be continue...когда девопс прикрутит к стенду логику
