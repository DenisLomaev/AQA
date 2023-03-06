import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import valid_password_ui_python, valid_phone_number_universal_for_UI
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage
from test_framework.ui.pages.profile_pages.transfer_via_cards_page import TransferCardsProfilePage


@pytest.mark.ui
@allure.id("C6066975")
@allure.title("C6066975. Пользователь может выбрать перевод на другую карту")
def test_ui_c6066975_user_can_choose_transfer_another_card(browser):
    # Открытие главной страницы банка
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Авторизация
    main_page.authorization(phone_number=valid_phone_number_universal_for_UI, password=valid_password_ui_python)

    # Переход в личный кабинет(профиль)
    main_page.click_logo_gor()
    profile_main_page = ProfileMainPage(browser)

    # Переход на страницу "Переводы"
    profile_main_page.open_profile_transfer_via_cards_page()
    profile_transfer_via_cards_page = TransferCardsProfilePage(browser, url=browser.current_url)

    # В разделе "Переводы" выбрать таб "По карте"
    profile_transfer_via_cards_page.click_button_by_card()

    # Проверка отображения формы для переводов по карте
    profile_transfer_via_cards_page.check_displaying_elements_on_page("form_card_to_card_money_transfer_locator")
