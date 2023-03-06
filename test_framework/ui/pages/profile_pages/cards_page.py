import allure
import pytest

from test_data.ui.url_data import CARDS_PAGE
from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.locators.profile_pages_loc.cards_page_loc import LocatorsProfileCardsPage
from test_framework.ui.pages.base_pages.base_page import BasePage


class ProfileCardsPage(BasePage):
    def __init__(self, browser, url=None) -> None:
        super().__init__(browser, url)
        self.locators = LocatorsProfileCardsPage
        self.url = CARDS_PAGE

    @allure.step("Клик на кнопку 'Раскрыть/Скрыть'.")
    def click_on_button_expand_hide(self):
        button_expand_hide = self.browser.find_element(*self.locators.button_expand_locator)
        button_expand_hide.click()

    @allure.step("Проверка отображения основных карт")
    def check_displaying_basic_cards(self):
        card_one = self.browser.find_element(*self.locators.card_one_locator)
        card_one.is_displayed()
        card_two = self.browser.find_element(*self.locators.card_two_locator)
        card_two.is_displayed()

    @allure.step("Проверка отображения дополнительных карт.")
    def check_displaying_additional_cards(self):
        card_four = self.browser.find_element(*self.locators.card_four_locator)
        card_four.is_displayed()
        card_five = self.browser.find_element(*self.locators.card_five_locator)
        card_five.is_displayed()

    @allure.step("Проверка отображения только основных карт.")
    def check_not_displaying_additional_cards(self):
        card_four = self.browser.find_elements(*self.locators.card_four_locator)
        card_five = self.browser.find_elements(*self.locators.card_five_locator)
        if not (card_four and card_five):
            return True
        raise pytest.fail("Дополнительные карты отображаются на странице.")

    @allure.step("Клик на изображение карты 'GoR Classic.")
    def click_on_image_card_gor_classic(self):
        image_card_gor_classic = self.browser.find_element(*self.locators.card_gor_classic_image_locator)
        image_card_gor_classic.click()

    @allure.step("Провека отображения вкладки 'Информация'.")
    def check_display_tab_information(self):
        tab_information = self.browser.find_element(*self.locators.tab_information_locator)
        tab_information.is_displayed()

    @allure.step("Провека отображения вкладки 'История'.")
    def check_display_tab_history(self):
        tab_information = self.browser.find_element(*self.locators.tab_history_locator)
        tab_information.is_displayed()

    @allure.step("Провека отображения вкладки 'Управление'.")
    def check_display_tab_control(self):
        tab_information = self.browser.find_element(*self.locators.tab_control_locator)
        tab_information.is_displayed()

    @allure.step("Клик на изображение карты 'GoR Gold'.")
    def click_on_image_card_gor_gold(self):
        image_card_gor_gold = self.browser.find_element(*self.locators.card_gor_gold_image_locator)
        image_card_gor_gold.click()

    @allure.step("Клик на изображение карты 'GoR Smart'.")
    def click_on_image_card_gor_smart(self):
        image_card_gor_gold = self.browser.find_element(*self.locators.card_gor_smart_image_locator)
        image_card_gor_gold.click()

    @allure.step("Клик на вкладку 'История'.")
    def click_on_tab_history(self):
        self.browser.find_element(*self.locators.tab_history_locator).click()

    @allure.step("Проверка наличия элементов на странице.")
    def check_displaying_elements_on_page(self, expected_locator: str) -> None:
        element_on_page = self.is_element_present(getattr(self.locators, expected_locator))
        CommonChecker.check_field_equals(element_on_page, True, assertion_message="Элемента нет на странице")

    @allure.step("Проверка наличия Формы инфо о карте на странице.")
    def check_full_fields_in_form_on_cards_page(self):
        self.browser.find_element(*self.locators.label_status_locator)
        self.browser.find_element(*self.locators.label_currency_locator)
        self.browser.find_element(*self.locators.label_validity_date_locator)
        self.browser.find_element(*self.locators.label_client_locator)
        self.browser.find_element(*self.locators.label_card_number_locator)
        self.browser.find_element(*self.locators.label_account_number_locator)
        self.browser.find_element(*self.locators.field_status_locator)
        self.browser.find_element(*self.locators.field_currency_locator)
        self.browser.find_element(*self.locators.field_validity_date_locator)
        self.browser.find_element(*self.locators.field_client_locator)
        self.browser.find_element(*self.locators.field_card_number_locator)
        self.browser.find_element(*self.locators.field_account_number_locator)
        self.browser.find_element(*self.locators.copy_info_client_locator)
        self.browser.find_element(*self.locators.copy_info_card_number_locator)
        self.browser.find_element(*self.locators.copy_info_account_number_locator)
        self.browser.find_element(*self.locators.form_card_info_locator)
        self.browser.find_element(*self.locators.calendar_locator)
