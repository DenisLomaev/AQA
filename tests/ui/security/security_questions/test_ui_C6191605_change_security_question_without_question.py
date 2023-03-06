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
@allure.id("C6191605")
@allure.title("C6191605. Изменить контрольный вопрос,не выбрав вопрос")
def test_ui_C6191605_change_security_question_without_question(browser):
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

    # Заполнить поле введите ответ на секретный вопрос
    profile_security_page.enter_answer_for_your_security_question("Asdfsd1234A")

    # Проверка, что кнопка подтвердить неактивна
    profile_security_page.check_no_active_submit_button()
