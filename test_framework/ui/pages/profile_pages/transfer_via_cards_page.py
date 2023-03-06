import allure
from selenium import webdriver

from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.locators.profile_pages_loc.transfer_via_cards_page_loc import LocatorsTransferCardsPage
from test_framework.ui.pages.base_pages.base_page import BasePage


class TransferCardsProfilePage(BasePage):
    def __init__(self, browser, url: str):
        super().__init__(browser, url)
        self.locators = LocatorsTransferCardsPage()

    @allure.step("Клик на вкладку 'По карте'.")
    def click_button_by_card(self):
        button_by_card = self.browser.find_element(*self.locators.button_by_card_locator)
        button_by_card.click()

    @allure.step("Проверка наличия элементов на странице.")
    def check_displaying_elements_on_page(self, expected_locator: str) -> None:
        element_on_page = self.is_element_present(getattr(self.locators, expected_locator))
        CommonChecker.check_field_equals(element_on_page, True, assertion_message="Элемента нет на странице")
