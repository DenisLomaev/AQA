import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import valid_password_ui_python, valid_phone_number_universal_for_UI
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.profile_pages.cards_page import ProfileCardsPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6032472")
@allure.title("C6032472. Возможность для пользователя просматривать реквизиты карты 'GoR Smart'")
def test_ui_c6032472_user_can_view_card_smart_details(browser):
    # Открытие главной страницы банка
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Авторизация
    main_page.authorization(phone_number=valid_phone_number_universal_for_UI, password=valid_password_ui_python)

    # Переход в личный кабинет(профиль)
    main_page.click_logo_gor()
    profile_main_page = ProfileMainPage(browser)

    # Открытие вкладки 'Карты'
    profile_main_page.open_profile_cards_page()
    profile_cards_page = ProfileCardsPage(browser)

    # Кликнуть на изображение карты 'GoR Smart'
    profile_cards_page.click_on_image_card_gor_gold()

    # Проверка отображения вкладки 'Информация'
    profile_cards_page.check_display_tab_information()

    # Проверка отображения вкладки 'История'
    profile_cards_page.check_display_tab_history()

    # Проверка отображения вкладки 'Управление'
    profile_cards_page.check_display_tab_control()

    # Поверка отображения формы инфо о карте и ее элементов
    profile_cards_page.check_full_fields_in_form_on_cards_page()

    # Проверка отображения кнопки Детали кредита
    profile_cards_page.check_displaying_elements_on_page("button_credit_detail_locator")

    # Проверка отображения элементов Footer
    profile_main_page.check_displaying_footer_elements()
