import allure

from test_data.ui.url_data import MAIN_PAGE_URL, PRIVACY_POLICY
from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.locators.registration_page_loc import LocatorsRegistrationPage
from test_framework.ui.pages.base_pages.base_page import BasePage


class RegistrationPage(BasePage):
    locators_by = LocatorsRegistrationPage

    @allure.step("Клик на поле ввода номера телефона.")
    def check_hint_enter_number_after_click_on_phone_field(self):
        phone_field = self.browser.find_element(*self.locators_by.field_phone_locator)
        phone_field.click()

        text_enter_number = self.browser.find_element(*self.locators_by.text_enter_number_locator).text
        CommonChecker.check_field_equals(
            text_enter_number, "Введите номер телефона", assertion_message="Тексты подсказок не совпадают"
        )

    @allure.step("Ввод валидного номера телефона в поле ввода.")
    def enter_number_in_phone_field(self, phone: str):
        phone_field = self.browser.find_element(*self.locators_by.field_phone_locator)
        phone_field.send_keys(phone)

    @allure.step('Клик на кнопку "Продолжить".')
    def click_button_continue(self):
        continue_button = self.browser.find_element(*self.locators_by.button_continue_locator)
        continue_button.click()

    @allure.step("Клик на поле ввода кода из СМС.")
    def click_sms_code_field(self):
        sms_code_field = self.browser.find_element(*self.locators_by.field_sms_code_locator)
        sms_code_field.click()

    @allure.step("Ввод кода из СМС.")
    def enter_sms_code_in_field(self, sms_code: int):
        sms_code_field = self.browser.find_element(*self.locators_by.field_sms_code_locator)
        sms_code_field.send_keys(sms_code)

    @allure.step("Заполнение полей: имя, фамилия, отчество, номер паспорта, выбор радио-баттона резидент/не резидент.")
    def enter_user_data_for_registration_in_fields(
        self, first_name: str, middle_name: str, last_name: str, passport_number: int, email: str
    ):
        first_name_field = self.browser.find_element(*self.locators_by.field_first_name_locator)
        first_name_field.send_keys(first_name)

        middle_name_field = self.browser.find_element(*self.locators_by.field_middle_name_locator)
        middle_name_field.send_keys(middle_name)

        last_name_field = self.browser.find_element(*self.locators_by.field_last_name_locator)
        last_name_field.send_keys(last_name)

        passport_number_field = self.browser.find_element(*self.locators_by.field_passport_number_locator)
        passport_number_field.click()
        passport_number_field.send_keys(passport_number)

        not_resident_radio_button = self.browser.find_element(*self.locators_by.radio_button_no_resident_locator)
        not_resident_radio_button.click()

        email_field = self.browser.find_element(*self.locators_by.field_email_locator)
        email_field.send_keys(email)

    @allure.step('Клик кнопки "Войти" с заполненными полями регистрации.')
    def click_button_enter_with_registration_data(self):
        button_enter = self.browser.find_element(*self.locators_by.button_enter_with_registration_data_locator)
        button_enter.click()

    @allure.step("Заполнение полей ввода пароля валидным паролем.")
    def enter_create_password_and_confirm_for_registration_fields(self, password: str):
        create_password_field = self.browser.find_element(*self.locators_by.field_create_password_locator)
        create_password_field.send_keys(password)

        confirm_password_field = self.browser.find_element(*self.locators_by.field_confirm_create_password_locator)
        confirm_password_field.send_keys(password)

    @allure.step("Выбор контрольного вопроса из выпадающего списка и ввод ответа на него.")
    def select_secret_question_and_answer(self, answer: str):
        secret_question = self.browser.find_element(*self.locators_by.field_secret_question_locator)
        secret_question.click()
        select_secret_question = self.browser.find_element(*self.locators_by.field_selected_secret_question_locator)
        select_secret_question.click()
        answer_on_secret_question = self.browser.find_element(*self.locators_by.field_answer_on_secret_question_locator)
        answer_on_secret_question.send_keys(answer)

    @allure.step("Проверка успешности регистрации.")
    def check_successful_registration(self):
        congratulations_text = self.browser.find_element(*self.locators_by.congratulations_text_locator).text
        congratulations_message_text = self.browser.find_element(
            *self.locators_by.congratulations_message_text_locator
        ).text
        CommonChecker.check_field_equals(
            congratulations_text, "Поздравляем!", assertion_message="Произошла ошибка при регистрации пользователя"
        )
        CommonChecker.check_field_equals(
            congratulations_message_text,
            "Вы успешно зарегистрировались в GoR Bank Online!",
            assertion_message="Произошла ошибка при регистрации пользователя",
        )

    @allure.step(
        "Проверка активности ссылок 'Политика конфиденциальности и 'Правила дистанционного банковского обслуживания'"
    )
    def check_links_activity(self):
        window_before = self.browser.window_handles[0]
        link_privacy_policy = self.browser.find_element(*self.locators_by.link_privacy_policy_locator)
        link_privacy_policy.click()
        window_after = self.browser.window_handles[1]
        self.browser.switch_to.window(window_after)
        url_privacy_policy = self.browser.current_url
        CommonChecker.check_field_equals(
            url_privacy_policy, f"{MAIN_PAGE_URL}{PRIVACY_POLICY}", assertion_message="Ошибка перехода по ссылке"
        )

        self.browser.close()
        self.browser.switch_to.window(window_before)

        link_banking_rules = self.browser.find_element(*self.locators_by.link_banking_rules_locator)
        link_banking_rules.click()
        window_after_click = self.browser.window_handles[1]
        self.browser.switch_to.window(window_after_click)
        url_banking_rules = self.browser.current_url
        CommonChecker.check_field_equals(
            url_banking_rules, f"{MAIN_PAGE_URL}{PRIVACY_POLICY}", assertion_message="Ошибка перехода по ссылке"
        )

    @allure.step("Цикл регистрации с вводом валидных данных до шага выбора контрольного вопроса")
    def registration_under_step_create_secret_question(
        self,
        phone: str,
        sms_code: int,
        user_first_name,
        user_middle_name,
        user_last_name,
        passport_number,
        password,
        email: str,
    ):
        # Нажать на поле ввода номера телефона.
        self.check_hint_enter_number_after_click_on_phone_field()
        # Ввести валидный номер телефона в поле ввода.
        self.enter_number_in_phone_field(phone=phone)
        # Нажать кнопку "Продолжить".
        self.click_button_continue()
        # Нажать на поле ввода кода из СМС.
        self.click_sms_code_field()
        # Ввести код из СМС.
        self.enter_sms_code_in_field(sms_code=sms_code)
        # Нажать на кнопку "Продолжить".
        self.click_button_continue()
        # Заполнить поля Имя, Фамилия, Отчество (необязательно),
        # Номер паспорта, выбрать радио-баттон Резидент/ Не резидент
        self.enter_user_data_for_registration_in_fields(
            user_first_name, user_middle_name, user_last_name, passport_number, email
        )
        # Нажать на кнопку "Продолжить".
        self.click_button_enter_with_registration_data()
        # Заполнить поля ввода пароля валидным паролем.
        self.enter_create_password_and_confirm_for_registration_fields(password=password)
        # Нажать кнопку "Продолжить".
        self.click_button_continue()

    @allure.step("Создание своего контрольного вопроса и ввод ответа на него.")
    def select_create_secret_question_and_answer(self, your_secret_question: str, answer_on_secret_question: str):
        choose_secret_question = self.browser.find_element(*self.locators_by.field_secret_question_locator)
        choose_secret_question.click()
        select_create_secret_question = self.browser.find_element(
            *self.locators_by.field_select_create_secret_question_locator
        )
        select_create_secret_question.click()
        create_secret_question = self.browser.find_element(*self.locators_by.field_create_your_secret_question_locator)
        create_secret_question.send_keys(your_secret_question)
        answer_secret_question = self.browser.find_element(*self.locators_by.field_answer_on_secret_question_locator)
        answer_secret_question.send_keys(answer_on_secret_question)

    @allure.step("Клик на кнопку 'Назад.'")
    def click_on_button_back(self):
        button_back = self.browser.find_element(*self.locators_by.button_back_locator)
        button_back.click()

    @allure.step("Нажать на кнопку 'Закрыть.'")
    def click_on_button_close(self):
        button_close = self.browser.find_element(*self.locators_by.button_close_locator)
        button_close.click()

    @allure.step("Перезагрузка страницы.")
    def reload_page(self):
        self.browser.refresh()
