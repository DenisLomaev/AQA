import time

import allure
import pytest
from selenium.webdriver.common.keys import Keys

from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.data.data_main_page import DataMainPage
from test_framework.ui.data.data_messages import DataMessages
from test_framework.ui.data.for_tests.data_c5993625 import full_password
from test_framework.ui.data.for_tests.data_c5994510 import full_phone_number
from test_framework.ui.locators.main_page_loc import LocatorsMainPage
from test_framework.ui.pages.base_pages.base_page import BasePage


class MainPage(BasePage):
    locators_by = LocatorsMainPage
    data = DataMainPage()
    error = DataMessages()

    @allure.step('Клик на кнопку "Зарегистрироваться".')
    def open_registration_page(self):
        registration_page = self.browser.find_element(*self.locators_by.button_registration_locator)
        registration_page.click()

    @allure.step('Клик на кнопку "По телефону".')
    def click_button_by_phone(self):
        phone_button = self.browser.find_element(*self.locators_by.button_by_phone_locator)
        phone_button.click()

    @allure.step('Клик на кнопку "По паспорту".')
    def click_button_by_passport(self):
        button_passport = self.browser.find_element(*self.locators_by.button_by_passport_number_locator)
        button_passport.click()

    @allure.step('Нажать на поле "Номер паспорта".')
    def click_on_the_passport_number_entry_field(self):
        passport_field = self.browser.find_element(*LocatorsMainPage.field_passport_number_locator)
        passport_field.click()

    @allure.step('Проверяем что Лейбл "Паспорт" отображается над полем ввода номера паспорта.')
    def check_the_passport_text_above_the_input_field(self):
        passport_text_field = self.browser.find_element(*LocatorsMainPage.text_above_the_passport_field)
        passport_text = passport_text_field.text
        CommonChecker.check_field_equals(
            passport_text,
            self.data.text_passport,
            assertion_message="Произошла ошибка отсутствует текст над Полем ввода паспорта",
        )

    @allure.step("Ввести номер паспорта в поле 'Номер паспорта'.")
    def enter_on_the_passport_number_entry_field(self, passport_number: str):
        passport_field = self.browser.find_element(*LocatorsMainPage.field_passport_number_locator)
        passport_field.send_keys(passport_number)

    @allure.step("Нажать на поле 'Телефон'.")
    def click_phone_field(self):
        phone_field = self.browser.find_element(*self.locators_by.field_phone_locator)
        phone_field.click()

    @allure.step('Проверяем что Лейбл "Пароль" отображается над полем ввода пароля')
    def check_the_password_text_above_the_input_field(self):
        password_text_field = self.browser.find_element(*LocatorsMainPage.text_above_the_password_field)
        password_text = password_text_field.text
        CommonChecker.check_field_equals(
            password_text,
            self.data.text_password,
            assertion_message="Произошла ошибка отсутствует текст над Полем ввода пароля",
        )

    @allure.step("Клик на поле 'Паспорт'.")
    def click_passport_field(self):
        passport_field = self.browser.find_element(*self.locators_by.field_passport_number_locator)
        passport_field.click()

    @allure.step("Ввод валидного номера телефона в поле ввода.")
    def enter_number_in_phone_field(self, phone):
        phone_field = self.browser.find_element(*self.locators_by.field_phone_locator)
        phone_field.send_keys(phone)

    @allure.step("Проверка отображения сообщения 'Недостаточно символов'.")
    def check_message_not_enough_characters(self):
        message_not_enough_characters = self.browser.find_element(
            *self.locators_by.text_not_enough_characters_locator
        ).text
        CommonChecker.check_field_equals(
            message_not_enough_characters,
            self.data.message_not_enough_characters,
            assertion_message="Некорректное отображение сообщения",
        )

    @allure.step('Нажать на поле ввода "Пароль".')
    def click_on_the_password_input_field(self):
        enter_field_password = self.browser.find_element(*self.locators_by.field_password_locator)
        enter_field_password.click()

    @allure.step('Ввод валидного пароля в поле "Пароль".')
    def enter_password_in_pass_field(self, password):
        enter_field_password = self.browser.find_element(*self.locators_by.field_password_locator)
        enter_field_password.send_keys(password)

    @allure.step("Нажать на кнопку отображения пароля.")
    def click_on_password_display_button(self):
        click_display_button = self.browser.find_element(*self.locators_by.button_hidden_password_locator)
        click_display_button.click()

    @allure.step('Нажать на кнопку "Войти".')
    def click_button_login(self):
        button = self.browser.find_element(*self.locators_by.button_login_locator)
        self.browser.execute_script("arguments[0].click();", button)

    @allure.step('Клик на кнопку-логотип "GOR"(переход в личный кабинет)')
    def click_logo_gor(self):
        click_logo = self.browser.find_element(*self.locators_by.logo_locator)
        click_logo.click()

    @allure.step("Авторизация пользователя.")
    def authorization(self, phone_number: str, password: str):
        time.sleep(2)
        self.click_button_by_phone()
        self.click_phone_field()
        self.enter_number_in_phone_field(phone=phone_number)
        self.enter_password_in_pass_field(password=password)
        self.click_on_password_display_button()
        self.click_button_login()

    @allure.step("Проверка отображения главной страницы.")
    def check_main_page_after_reload(self):
        main_page_url = self.browser.current_url
        CommonChecker.check_field_equals(
            main_page_url, self.data.main_page_after_reload, assertion_message="Ошибка отображения главной страницы"
        )

    @allure.step("Проверка отображения сообщения 'Включен CapsLock'.")
    def check_message_about_on_turned_capslock(self):
        message_on_turned_capslock = self.browser.find_element(
            *self.locators_by.text_about_on_turned_capslock_locator
        ).text
        CommonChecker.check_field_equals(
            message_on_turned_capslock,
            self.data.message_include_capslock,
            assertion_message="Ошибка отображения уведомления о включенном CapsLock",
        )

    @allure.step("Проверка не отображения сообщения 'Включен CapsLock'.")
    def check_no_message_about_on_turned_capslock(self):
        message_on_turned_capslock = self.browser.find_elements(*self.locators_by.text_about_on_turned_capslock_locator)
        if not message_on_turned_capslock:
            return True
        raise pytest.fail("Сообщение о включенном CapsLock отображается на странице.")

    @allure.step("Проверка неактивности кнопки 'Войти'.")
    def check_status_button_login_disabled(self):
        button_login_disabled = self.browser.find_element(*self.locators_by.button_login_status_disabled)
        button_login_disabled.is_enabled()

    @allure.step("Очистка поля ввода номера телефона")
    def clear_field_phone_number(self):
        field_phone_number = self.browser.find_element(*self.locators_by.field_phone_locator)
        field_phone_number.send_keys(Keys.CONTROL + "a")
        field_phone_number.send_keys(Keys.DELETE)

    @allure.step("Проверка не отображания введеных букв и спец.символов в поле ввода номера паспорта.")
    def check_no_entered_letters_and_special_characters_in_passport_field(self):
        text_passport_field = self.browser.find_element(*self.locators_by.field_passport_number_locator).text
        CommonChecker.check_field_equals(
            text_passport_field, self.data.empty_field, assertion_message="Ошибка при проверке введенных символов"
        )

    @allure.step(
        'Проверка отображения сообщения "Пароль должен содержать не менее 6 знаков,'
        'строчные или заглавные буквы латинского алфавита A-z, цифры от 0 до 9"'
    )
    def check_message_validation_password(self):
        text_message_validation_password = self.browser.find_element(
            *self.locators_by.text_validation_password_locator
        ).text
        CommonChecker.check_field_equals(
            text_message_validation_password,
            self.error.message_validation_password,
            assertion_message="Ошибка отображения уведомления о валидации пароля",
        )

    @allure.step("Очистка поля ввода номера паспорта")
    def clear_field_passport_number(self) -> None:
        field_passport_number = self.browser.find_element(*self.locators_by.field_passport_number_locator)
        field_passport_number.send_keys(Keys.CONTROL + "a")
        field_passport_number.send_keys(Keys.DELETE)

    @allure.step("Проверка не отображания введеных букв и спец.символов в поле ввода номера телефона.")
    def check_no_entered_letters_and_special_characters_in_phone_field(self):
        text_passport_field = self.browser.find_element(*self.locators_by.field_phone_locator).text
        CommonChecker.check_field_equals(
            text_passport_field, self.data.empty_field, assertion_message="Ошибка при проверке введенных символов"
        )

    @allure.step("Проверка не отображания введенных спец.символов в поле ввода номера пароля.")
    def check_no_entered_special_characters_in_password_field(self):
        text_password_field = self.browser.find_element(*self.locators_by.field_password_locator).text
        CommonChecker.check_field_equals(
            text_password_field, self.data.empty_field, assertion_message="Ошибка при проверке введенных символов"
        )

    @allure.step("Проверка активности кнопки 'Войти'.")
    def check_active_button_login(self):
        return self.browser.find_element(*self.locators_by.button_login_status_enabled)

    @allure.step("Проверка отображения введенных символов в поле 'Пароль'.")
    def check_entered_symbols_in_password_field(self):
        text_password_field = self.browser.find_element(*self.locators_by.field_password_locator).get_property("value")
        CommonChecker.check_field_equals(
            text_password_field, full_password, assertion_message="Ошибка при проверке введенных символов"
        )

    @allure.step("Проверка введенных цифр в поле 'Телефон'.")
    def check_entered_digits_phone_field(self):
        text_field_phone_number = self.browser.find_element(*self.locators_by.field_phone_locator).get_attribute(
            "value"
        )
        CommonChecker.check_field_equals(
            text_field_phone_number.replace(" ", ""),
            full_phone_number,
            assertion_message="Ошибка при проверке номера телефона",
        )

    @allure.step('Клик на кнопку-логотип "Аккаунт+имя"(переход в личный кабинет)')
    def click_button_account(self):
        click_button = self.browser.find_element(*self.locators_by.button_account_locator)
        click_button.click()

    @allure.step("Ожидание кликабельности элемента ЛОГО")
    def wait_logo_is_clickable(self):
        self.browser.find_element(*self.locators_by.logo_locator)

    @allure.step("Проверка наличия элементов на странице.")
    def check_displaying_elements_on_page(self, locator):
        element_on_page = self.browser.find_element(*locator)
        element_on_page.is_displayed()
