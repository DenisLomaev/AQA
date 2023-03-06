import allure

from test_data.ui.url_data import SETTINGS_PAGE_URL
from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.data.data_field import DataField
from test_framework.ui.data.data_tabs import DataTabs
from test_framework.ui.locators.personal_profile_pages_loc.profile_notifications_page_loc import (
    LocatorsProfileNotificationPage,
)
from test_framework.ui.pages.base_pages.base_page import BasePage


class ProfileNotificationPage(BasePage):
    def __init__(self, browser, url=None) -> None:
        super().__init__(browser, url)
        self.locators = LocatorsProfileNotificationPage
        self.tab = DataTabs()
        self.field = DataField()
        self.url = SETTINGS_PAGE_URL

    @allure.step("Клик на вкладку 'Настройки'.")
    def open_profile_options_page(self):
        profile_notification_page = self.browser.find_element(*self.locators.profile_notification_page_locator)
        profile_notification_page.click()

    @allure.step("Клик на чекбокс 'Email рассылка'")
    def click_checkbox_email_notification(self):
        profile_notification_page = self.browser.find_element(*self.locators.checkbox_email_notification_locator)
        profile_notification_page.click()

    @allure.step("Клик на чекбокс 'SMS рассылка'")
    def click_checkbox_sms_notification(self):
        profile_notification_page = self.browser.find_element(*self.locators.checkbox_sms_notification_locator)
        profile_notification_page.click()

    @allure.step("Клик на чекбокс 'PUSH рассылка'")
    def click_checkbox_push_notification(self):
        profile_notification_page = self.browser.find_element(*self.locators.checkbox_push_notification_locator)
        profile_notification_page.click()

    @allure.step("Проверка переключения чекбокса")
    def check_notification_checkbox_switch(self, locator, label):
        notification_checkbox = self.browser.find_element(*getattr(self.locators, locator)).text
        CommonChecker.check_field_equals(
            notification_checkbox, label, assertion_message="Не удалось переключить чекбокс"
        )
