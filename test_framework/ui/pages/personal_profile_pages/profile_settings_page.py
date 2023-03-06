import allure
from selenium.webdriver.common.keys import Keys

from test_data.ui.url_data import SETTINGS_PAGE_URL
from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.data.data_field import DataField
from test_framework.ui.data.data_messages import DataMessages
from test_framework.ui.data.data_tabs import DataTabs
from test_framework.ui.locators.personal_profile_pages_loc.profile_settings_page_loc import LocatorsProfileSettingsPage
from test_framework.ui.pages.base_pages.base_page import BasePage


class ProfileSettingsPage(BasePage):
    def __init__(self, browser, url=None) -> None:
        super().__init__(browser, url)
        self.locators = LocatorsProfileSettingsPage
        self.tab = DataTabs()
        self.field = DataField()
        self.error = DataMessages
        self.url = SETTINGS_PAGE_URL

    @allure.step("Клик на вкладку 'Настройки'.")
    def open_profile_options_page(self) -> None:
        profile_settings_page = self.browser.find_element(*self.locators.profile_settings_page_locator)
        profile_settings_page.click()

    @allure.step("Клик на кнопку 'карандаш' Изменить Email.")
    def click_on_button_change_email(self) -> None:
        button_change_email = self.browser.find_element(*self.locators.button_change_email_locator)
        button_change_email.click()

    @allure.step("Клик на кнопку 'карандаш' Изменить Номер телефона.")
    def click_on_button_change_phone_number(self) -> None:
        button_change_email = self.browser.find_element(*self.locators.button_change_phone_number_locator)
        button_change_email.click()

    @allure.step("Сравнить Email в поле с Email пользователя.")
    def check_user_email_in_email_field_equals(self, expected_email: str) -> None:
        field_email_text = self.browser.find_element(*self.locators.field_email_locator).get_attribute("value")
        CommonChecker.check_field_equals(field_email_text, expected_email)

    @allure.step("Сравить Номер телефона в поле с номером телефона пользователя.")
    def check_user_phone_number_in_phone_number_field_equals(self, expected_phone_number: str) -> None:
        field_phone_number_text = (
            self.browser.find_element(*self.locators.field_phone_number_locator).get_attribute("value").replace(" ", "")
        )
        CommonChecker.check_field_equals(field_phone_number_text, expected_phone_number)

    @allure.step("Ввод данных в поле Email.")
    def enter_new_email_to_email_field(self, new_email: str) -> None:
        email_field = self.browser.find_element(*self.locators.field_email_locator)
        email_field.send_keys(Keys.CONTROL + "a")
        email_field.send_keys(Keys.DELETE)
        email_field.send_keys(new_email)

    @allure.step("Ввод данных в поле Номер телефона.")
    def enter_new_phone_number_to_phone_number_field(self, new_phone_number: str) -> None:
        phone_number_field = self.browser.find_element(*self.locators.field_phone_number_locator)
        phone_number_field.send_keys(Keys.CONTROL + "a")
        phone_number_field.send_keys(Keys.DELETE)
        phone_number_field.send_keys(new_phone_number)

    @allure.step("Ввод данных в поле Номер телефона без очистки поля.")
    def enter_new_phone_number_to_phone_number_field_with_no_clear(self, new_phone_number: str) -> None:
        phone_number_field = self.browser.find_element(*self.locators.field_phone_number_locator)
        phone_number_field.send_keys(new_phone_number)

    @allure.step("Проверка активноси кнопки 'Сохранить изменения'.")
    def check_button_save_changes_is_disable(self) -> None:
        button_save_change = self.browser.find_element(*self.locators.button_save_changes_locator)
        button_save_change.is_enabled()

    @allure.step("Клик на кнопку 'Сохранить изменения'")
    def click_on_save_changes_button(self) -> None:
        button_save_change = self.browser.find_element(*self.locators.button_save_changes_locator)
        button_save_change.click()

    @allure.step("Клик на кнопку 'Сбросить изменения'")
    def click_on_dismiss_changes_button(self) -> None:
        button_save_change = self.browser.find_element(*self.locators.button_skip_changes_locator)
        button_save_change.click()

    @allure.step("Проверка отображения сообщения о успешном изменении email.")
    def check_message_success_change_email(self) -> None:
        text_message_success_change = self.browser.find_element(*self.locators.message_email_success_changed).text
        CommonChecker.check_field_equals(
            text_message_success_change,
            self.error.message_access_email_change,
            assertion_message="Ошибка отображения уведомления об изменения email",
        )

    @allure.step("Проверка отображения сообщения об ошибке изменения email.")
    def check_message_not_change_email(self) -> None:
        text_message_not_change = self.browser.find_element(*self.locators.message_email_not_changed).text
        CommonChecker.check_field_equals(
            text_message_not_change, self.error.message_not_change_email, assertion_message="Email изменен"
        )

    @allure.step("Проверка отсутствия элементов на странице.")
    def check_not_displaying_elements_in_page(self, expected_locator: str) -> None:
        element_on_page = self.is_element_present(getattr(self.locators, expected_locator))
        CommonChecker.check_field_equals(element_on_page, False, assertion_message="Элемент есть на странице")

    @allure.step("Проверка наличия элементов на странице.")
    def check_displaying_elements_on_page(self, expected_locator: str) -> None:
        element_on_page = self.browser.find_element(getattr(self.locators, expected_locator))
        element_on_page.is_displayed()

    @allure.step("Проверка отображения сообщения об успешном изменении поля.")
    def check_message_success_change_field(self, locator: str, expected_error: str) -> None:
        text_message_success_change = self.browser.find_element(*getattr(self.locators, locator)).text
        CommonChecker.check_field_equals(
            text_message_success_change,
            getattr(self.error, expected_error),
            assertion_message="Ошибка отображения уведомления об изменения поля",
        )

    @allure.step("Проверка отображения сообщения об ошибке изменения поля.")
    def check_message_not_change_field(self, locator: str, expected_error: str) -> None:
        text_message_not_change = self.browser.find_element(*getattr(self.locators, locator)).text
        CommonChecker.check_field_equals(
            text_message_not_change, getattr(self.error, expected_error), assertion_message="Значение поля изменено"
        )

    @allure.step("Клик на кнопку 'карандаш' Изменить Номер телефона.")
    def click_on_link(self, link) -> None:
        excepted_link = self.browser.find_element(*getattr(self.locators, link))
        excepted_link.click()

    @allure.step("Проверка отображения страницы.")
    def check_page_after_link_click(self, excepted_url):
        current_page_url = self.browser.current_url
        CommonChecker.check_field_equals(
            current_page_url, excepted_url, assertion_message="Ошибка отображения страницы"
        )
