import time

import allure

from test_data.ui.url_data import PROFILE_PAGE_URL
from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.locators.profile_main_page_loc import LocatorsProfileMainPage
from test_framework.ui.pages.base_pages.base_page import BasePage


class ProfileMainPage(BasePage):
    def __init__(self, browser, url=None) -> None:
        super().__init__(browser, url)
        self.locators = LocatorsProfileMainPage
        self.url = PROFILE_PAGE_URL

    @allure.step("Клик на линк пользователя.")
    def open_profile_general_information_page(self):
        self.wait_element_clickable(*self.locators.profile_general_information_page_locator)
        profile_general_information_page = self.browser.find_element(
            *self.locators.profile_general_information_page_locator
        )
        profile_general_information_page.click()

    @allure.step("Клик на вкладку 'Карты'.")
    def open_profile_cards_page(self):
        profile_cards_page = self.browser.find_element(*self.locators.profile_cards_page_locator)
        profile_cards_page.click()

    @allure.step("Клик на раздел 'Кредиты'")
    def click_on_credits_section(self):
        credit_button = self.browser.find_element(*self.locators.button_credits_section)
        credit_button.click()

    @allure.step("Клик на раздел 'Кредитные продукты'")
    def click_on_credits_product(self):
        credit_product_button = self.browser.find_element(*self.locators.button_credit_product)
        credit_product_button.click()

    @allure.step("Клик на вкладку 'Переводы'.")
    def open_profile_transfer_via_cards_page(self):
        profile_transfer_via_cards_page = self.browser.find_element(*self.locators.profile_transfer_via_cards_locator)
        profile_transfer_via_cards_page.click()

    @allure.step('Нажатие на кнопку "Выход"')
    def click_button_logout(self):
        click_button = self.browser.find_element(*self.locators.button_logout_locator)
        click_button.click()

    @allure.step("Выход из страницы")
    def click_logout(self):
        self.wait_element_clickable(*self.locators.button_logout_locator)
        self.click_button_logout()
        time.sleep(1)

    @allure.step("Проверка наличия элементов на странице.")
    def check_displaying_elements_on_page(self, expected_locator: str) -> None:
        element_on_page = self.is_element_present(getattr(self.locators, expected_locator))
        CommonChecker.check_field_equals(element_on_page, True, assertion_message="Элемента нет на странице")

    @allure.step("Проверка отображения элементов в Footer.")
    def check_displaying_footer_elements(self):
        self.browser.find_element(*self.locators.footer_address)
        self.browser.find_element(*self.locators.footer_consultation_loc)
        self.browser.find_element(*self.locators.footer_for_fiz_client)
        self.browser.find_element(*self.locators.footer_button_link_appstore_locator)
        self.browser.find_element(*self.locators.footer_button_link_play_market_locator)
