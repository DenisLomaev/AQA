import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import valid_password_universal, valid_phone_number_universal_for_UI
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)


@pytest.mark.ui
@allure.id("C6176283")
@allure.title("C6176283 Проверка отображения элементов в личном кабинете")
def test_ui_c6176283_check_info_page_elements_is_present(browser):
    # Открытие главной страницы
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()
    # Авторизация пользователя
    main_page.authorization(phone_number=valid_phone_number_universal_for_UI, password=valid_password_universal)
    # Переход на страницу пользователя
    main_page.click_button_account()
    profile_page = ProfileGeneralInformationPage(browser)
    # Проверка наличия Лейбл "Фамилия" и поле с фамилией пользователя
    profile_page.check_displaying_elements_on_page("label_last_name_locator")
    profile_page.check_displaying_elements_on_page("field_last_name_locator")
    # Проверка наличия Лейбл "Имя" и поле с именем пользователя
    profile_page.check_displaying_elements_on_page("label_first_name_locator")
    profile_page.check_displaying_elements_on_page("field_first_name_locator")
    # Проверка наличия Лейбл "Отчество" и поле с отчеством пользователя
    profile_page.check_displaying_elements_on_page("label_past_name_locator")
    profile_page.check_displaying_elements_on_page("field_past_name_locator")
    # Проверка наличия Лейбл "Телефон" и поле с номером телефона пользователя
    profile_page.check_displaying_elements_on_page("label_telephone_locator")
    profile_page.check_displaying_elements_on_page("field_telephone_locator")
    # Проверка наличия Лейбл "Электронная почта" и поле для ввода данных
    profile_page.check_displaying_elements_on_page("label_email_locator")
    profile_page.check_displaying_elements_on_page("field_email_locator")
    # Проверка наличия Лейбл "Резиденство" и поле со статусом
    profile_page.check_displaying_elements_on_page("label_resident_locator")
    profile_page.check_displaying_elements_on_page("field_resident_locator")
