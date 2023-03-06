import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import valid_password_universal, valid_phone_number_universal_for_UI
from test_framework.ui.locators.profile_main_page_loc import LocatorsProfileMainPage
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6174394")
@allure.title("C6174394 Проверка отображения на главной странице элементов курсов валют")
def test_ui_c6174394_check_exchange_form_elements_is_present(browser):
    # Открытие главной страницы
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()
    # Авторизация пользователя
    main_page.authorization(phone_number=valid_phone_number_universal_for_UI, password=valid_password_universal)
    # Переход на главную страницу
    profile_page = ProfileMainPage(browser)
    # Проверка наличия названия столбца "Валюта"
    profile_page.check_displaying_elements_on_page("exchange_table_currency_column_name")
    # Проверка наличия названия столбца "Покупка"
    profile_page.check_displaying_elements_on_page("exchange_table_purchase_column_name")
    # Проверка наличия названия столбца "Продажа"
    profile_page.check_displaying_elements_on_page("exchange_table_sale_column_name")
    # Проверка наличия флага страны
    profile_page.check_displaying_elements_on_page("exchange_table_flag_image")
    # Проверка наличия кода страны
    profile_page.check_displaying_elements_on_page("exchange_table_country_code")
    # Проверка наличия названия страны
    profile_page.check_displaying_elements_on_page("exchange_table_currency_country_name")
    # Проверка наличия курса покупки валюты
    profile_page.check_displaying_elements_on_page("exchange_table_bye_currency")
    # Проверка наличия курса продажи валюты
    profile_page.check_displaying_elements_on_page("exchange_table_sell_currency")
