import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import valid_password_universal, valid_phone_number_universal_for_UI
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6174395")
@allure.title("C6174395 Проверка отображения на главной странице элементов популярных услуг")
def test_ui_c6174395_popular_services_for_elements_is_displayed(browser):
    # Открытие главной страницы
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()
    # Авторизация пользователя
    main_page.authorization(phone_number=valid_phone_number_universal_for_UI, password=valid_password_universal)
    # Переход на главную страницу
    profile_page = ProfileMainPage(browser)
    # Проверка наличия иконки услуги Оплаты связи
    profile_page.check_displaying_elements_on_page("popular_services_phone_pay_locator")
    # Проверка наличия названия услуги Оплаты связи
    profile_page.check_displaying_elements_on_page("popular_services_phone_pay_label_locator")
    # Проверка наличия иконки услуги Перевод на карту
    profile_page.check_displaying_elements_on_page("popular_services_money_transfer_locator")
    # Проверка наличия названия услуги Перевод на карту
    profile_page.check_displaying_elements_on_page("popular_services_money_transfer_label_locator")
    # Проверка наличия иконки услуги Утилиты
    profile_page.check_displaying_elements_on_page("popular_services_utilities_locator")
    # Проверка наличия названия услуги Утилиты
    profile_page.check_displaying_elements_on_page("popular_services_utilities_label_locator")
    # Проверка наличия иконки услуги Обмен валюты
    profile_page.check_displaying_elements_on_page("popular_services_exchange_locator")
    # Проверка наличия названия услуги Обмен валюты
    profile_page.check_displaying_elements_on_page("popular_services_exchange_label_locator")
    # Проверка наличия иконки Добавить
    profile_page.check_displaying_elements_on_page("popular_services_add_new_service_locator")
    # Проверка наличия названия иконки Добавить
    profile_page.check_displaying_elements_on_page("popular_services_add_new_service_label_locator")
