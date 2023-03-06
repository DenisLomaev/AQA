import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.for_tests.data_c6189299 import data_for_security_question
from test_framework.ui.data.user_data import valid_password_universal, valid_phone_number_universal_for_UI
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)
from test_framework.ui.pages.personal_profile_pages.profile_security_page import ProfileSecurityPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@pytest.mark.parametrize("expected_data", data_for_security_question)
@allure.id("C6189299")
@allure.title('C6189299. Валидные значения полей " Напишите ваш контрольный вопрос"')
def test_ui_C6189299_check_field_put_your_question_with_valid_data(browser, expected_data):
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

    # Клик на "Написать свой вопрос" из выпадающего списка
    profile_security_page.click_on_elements_on_drop_list("element_put_your_question_in_drop_list")

    # Ввод Твоего секретного вопроса и ответа
    profile_security_page.enter_your_security_question(expected_data)
    profile_security_page.enter_answer_for_your_security_question(expected_data)

    # Проверка введенного текста
    profile_security_page.check_text_in_field("field_put_your_question", expected_data)
    profile_security_page.check_text_in_field("field_put_your_answer", expected_data)
