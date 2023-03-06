import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import valid_password_universal, valid_phone_number_universal_for_UI
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)
from test_framework.ui.pages.personal_profile_pages.profile_security_page import ProfileSecurityPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6191604")
@allure.title("C6191604. Содержимое дропдауна смены контрольного вопроса и его функциональность.")
def test_ui_C6191604_check_fields_dropdown(browser):
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Авторизация пользователя
    main_page.authorization(phone_number=valid_phone_number_universal_for_UI, password=valid_password_universal)

    # Вход в личный кабинет
    profile_page = ProfileMainPage(browser, url=browser.current_url)
    profile_page.open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    profile_info = ProfileGeneralInformationPage(browser, url=browser.current_url)
    profile_info.open_profile_security_page()

    # Клик на кнопку "Смена контрольного вопроса"
    profile_security_page = ProfileSecurityPage(browser, url=browser.current_url)
    profile_security_page.click_on_button_change_security_question()

    # Клик на кнопку выпадения дроплиста
    profile_security_page.click_on_button_drop_list()

    # Проверка, что элементы дроплиста присутствуют на странице
    profile_security_page.check_displaying_elements_on_page_change_password("element_put_your_question_in_drop_list")
    profile_security_page.check_displaying_elements_on_page_change_password("element_lastname_your_mother_in_drop_list")
    profile_security_page.check_displaying_elements_on_page_change_password("element_name_your_close_friend")
    profile_security_page.check_displaying_elements_on_page_change_password("element_your_favorite_book")
    profile_security_page.check_displaying_elements_on_page_change_password("element_your_favorite_color")
    profile_security_page.check_displaying_elements_on_page_change_password("element_your_favorite_dish")
