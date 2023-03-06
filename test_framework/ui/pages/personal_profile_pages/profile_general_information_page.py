import allure

from test_data.ui.url_data import PROFILE_GENERAL_INFORMATION_PAGE_URL
from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.data.data_field import DataField
from test_framework.ui.data.data_tabs import DataTabs
from test_framework.ui.locators.personal_profile_pages_loc.profile_general_information_page_loc import (
    LocatorsProfileGeneralInformationPage,
)
from test_framework.ui.pages.base_pages.base_page import BasePage


class ProfileGeneralInformationPage(BasePage):
    def __init__(self, browser, url=None) -> None:
        super().__init__(browser, url)
        self.locators_by = LocatorsProfileGeneralInformationPage
        self.tab = DataTabs()
        self.field = DataField()
        self.url = PROFILE_GENERAL_INFORMATION_PAGE_URL

    @allure.step("Клик на вкладку 'Безопасность'.")
    def open_profile_security_page(self):
        profile_security_page = self.browser.find_element(*self.locators_by.profile_security_page_locator)
        profile_security_page.click()

    @allure.step("Проверка отображения вкладки 'Общая информация'")
    def check_displaying_tab_general_information(self):
        tab_general_information_text = self.browser.find_element(*self.locators_by.tab_general_information_locator).text
        CommonChecker.check_field_equals(
            tab_general_information_text,
            self.tab.general_information,
            assertion_message="Ошибка отображения вкладки 'Общая информация'",
        )

    @allure.step("Проверка отображения вкладки 'Безопасность'")
    def check_displaying_tab_security(self):
        tab_security_text = self.browser.find_element(*self.locators_by.tab_security_locator).text
        CommonChecker.check_field_equals(
            tab_security_text, self.tab.security, assertion_message="Ошибка отображения вкладки 'Безопасность'"
        )

    @allure.step("Проверка отображения вкладки 'Уведомления'")
    def check_displaying_tab_notifications(self):
        tab_notifications_text = self.browser.find_element(*self.locators_by.tab_notifications_locator).text
        CommonChecker.check_field_equals(
            tab_notifications_text, self.tab.notifications, assertion_message="Ошибка отображения вкладки 'Уведомления'"
        )

    @allure.step("Проверка отображения вкладки 'Настройки'")
    def check_displaying_tab_settings(self):
        tab_settings_text = self.browser.find_element(*self.locators_by.tab_settings_locator).text
        CommonChecker.check_field_equals(
            tab_settings_text, self.tab.settings, assertion_message="Ошибка отображения вкладки 'Настройки'"
        )

    @allure.step("Проверка отображения поля 'Имя'")
    def check_displaying_field_first_name(self):
        field_first_name_text = self.browser.find_element(*self.locators_by.label_first_name_locator).text
        CommonChecker.check_field_equals(
            field_first_name_text, self.field.first_name, assertion_message="Ошибка отображения поля 'Имя'"
        )

    @allure.step("Проверка отображения поля 'Фамилия'")
    def check_displaying_field_last_name(self):
        field_last_name_text = self.browser.find_element(*self.locators_by.label_last_name_locator).text
        CommonChecker.check_field_equals(
            field_last_name_text, self.field.last_name, assertion_message="Ошибка отображения поля 'Фамилия'"
        )

    @allure.step("Проверка отображения поля 'ID'")
    def check_displaying_field_id(self):
        field_id_text = self.browser.find_element(*self.locators_by.field_id_locator).text
        CommonChecker.check_field_equals(field_id_text, self.field.id, assertion_message="Ошибка отображения поля 'ID'")

    @allure.step("Проверка отображения поля 'Телефон'")
    def check_displaying_field_telephone(self):
        field_telephone_text = self.browser.find_element(*self.locators_by.field_telephone_locator).text
        CommonChecker.check_field_equals(
            field_telephone_text, self.field.telephone, assertion_message="Ошибка отображения поля 'Телефон'"
        )

    @allure.step("Проверка отображения поля 'Электронная почта'")
    def check_displaying_field_email(self):
        field_email_text = self.browser.find_element(*self.locators_by.field_email_locator).text
        CommonChecker.check_field_equals(
            field_email_text, self.field.email, assertion_message="Ошибка отображения поля 'Электронная почта'"
        )

    @allure.step("Проверка отображения радиобаттона 'Резидент РФ/Нерезидент РФ'")
    def check_displaying_radiobutton_resident_or_no_resident(self):
        radio_button_resident_text = self.browser.find_element(*self.locators_by.radio_button_resident_locator).text
        CommonChecker.check_field_equals(
            radio_button_resident_text,
            self.field.resident,
            assertion_message="Ошибка отображения радиобаттона 'Резидент РФ'",
        )

        radio_button_no_resident_text = self.browser.find_element(
            *self.locators_by.radio_button_no_resident_locator
        ).text
        CommonChecker.check_field_equals(
            radio_button_no_resident_text,
            self.field.no_resident,
            assertion_message="Ошибка отображения радиобаттона 'Нерезидент РФ'",
        )

    @allure.step("Проверка наличия элементов на странице.")
    def check_displaying_elements_on_page(self, locator: str) -> None:
        element_on_page = self.browser.find_element(*getattr(self.locators_by, locator))
        element_on_page.is_displayed()
