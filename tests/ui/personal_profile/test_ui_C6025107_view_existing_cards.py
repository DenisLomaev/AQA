import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import valid_password_ui_python, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.profile_pages.cards_page import ProfileCardsPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6025107")
@allure.title("C6025107. Просмотр имеющихся у клиента карт")
def test_ui_c6025107_view_existing_cards(browser):
    # Открытие главной страницы банка
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Авторизация
    main_page.authorization(phone_number=valid_phone_number_ui_python, password=valid_password_ui_python)

    # Переход в личный кабинет(профиль)
    main_page.click_logo_gor()
    profile_main_page = ProfileMainPage(browser)

    # Открытие вкладки 'Карты'
    profile_main_page.open_profile_cards_page()
    profile_cards_page = ProfileCardsPage(browser)

    # Проверка отображения основных карт
    profile_cards_page.check_displaying_basic_cards()

    # Клик на кнопку 'Раскрыть'
    profile_cards_page.click_on_button_expand_hide()

    # Проверка отображения основных и дополнительных карт
    profile_cards_page.check_displaying_additional_cards()
