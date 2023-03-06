import allure
from selenium.webdriver.common.keys import Keys

from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.data.data_messages import DataMessages
from test_framework.ui.data.data_profile_page import DataProfilePage
from test_framework.ui.locators.personal_profile_pages_loc.profile_security_page_loc import LocatorsProfileSecurityPage
from test_framework.ui.pages.base_pages.base_page import BasePage


class ProfileSecurityPage(BasePage):
    locators_by = LocatorsProfileSecurityPage
    error = DataMessages
    data = DataProfilePage

    @allure.step("Клик на кнопку 'Изменить пароль'.")
    def click_on_button_change_password(self):
        button_change_password = self.browser.find_element(*self.locators_by.button_change_password_locator)
        button_change_password.click()

    @allure.step("Клик на кнопку 'Смена контрольного вопроса'.")
    def click_on_button_change_security_question(self):
        button_change_password = self.browser.find_element(*self.locators_by.button_change_security_question_locator)
        button_change_password.click()

    @allure.step("Клик на кнопку 'глаза', для проверки введенного текста")
    def click_on_button_eye(self, expected_locator):
        button_eye = self.browser.find_element(*getattr(self.locators_by, expected_locator))
        button_eye.click()

    @allure.step("Проверка, что кнопка 'глаза' в поле Введите текущий пароль в активном состоянии")
    def check_state_button_eye(self, expected_locator):
        button_eye = self.browser.find_element(*getattr(self.locators_by, expected_locator))
        state_eye = button_eye.get_attribute("type")
        CommonChecker.check_field_equals(state_eye, "text", assertion_message="Кнопка глаза в пассивном состоянии")

    @allure.step("Ввод текущего пароля.")
    def enter_current_password(self, current_password: str):
        current_password_field = self.browser.find_element(*self.locators_by.field_current_password_locator)
        current_password_field.clear()
        current_password_field.send_keys(current_password)

    @allure.step("Ввод нового пароля.")
    def enter_new_password(self, new_password: str):
        create_new_password_field = self.browser.find_element(*self.locators_by.field_create_new_password_locator)
        create_new_password_field.send_keys(new_password)

    @allure.step("Подтверждение нового пароля.")
    def enter_confirm_new_password(self, new_password: str):
        confirm_new_password_field = self.browser.find_element(*self.locators_by.field_confirm_new_password_locator)
        confirm_new_password_field.send_keys(new_password)

    @allure.step("Клик на кнопку 'Подтвердить'.")
    def click_submit_button(self):
        submit_button = self.browser.find_element(*self.locators_by.button_submit_locator)
        submit_button.click()

    @allure.step("Проверка успешности смены пароля.")
    def check_success_change_password(self):
        success_change_password_text = self.browser.find_element(
            *self.locators_by.text_success_change_password_locator
        ).text
        CommonChecker.check_field_equals(
            success_change_password_text,
            "Пароль успешно изменен",
            assertion_message="Произошла ошибка при смене пароля",
        )

    @allure.step("Проверка ввода не более 20ти символов(цифр и букв) в поле 'Введите текущий пароль'.")
    def check_enter_data_field_current_password(self):
        field_current_password_text = self.browser.find_element(*self.locators_by.field_current_password_locator).text
        return (
            "В поле 'Введите текущий пароль' содержится более 20 символов"
            if len(field_current_password_text) > 20
            else True
        )

    @allure.step("Проверка, что кнопка 'Подтвердить' неактивна.")
    def check_no_active_submit_button(self):
        button_submit_disabled = self.browser.find_element(*self.locators_by.button_submit_locator_disabled)
        button_submit_disabled.is_enabled()

    @allure.step("Проверка, что кнопка 'Отменить' неактивна, на страницы смены секретного вопроса.")
    def check_no_active_cancel_button_on_page_security_questions(self):
        button_submit_disabled = self.browser.find_element(
            *self.locators_by.button_cancel_data_on_page_change_security_question
        )
        button_submit_disabled.is_enabled()

    @allure.step("Клик по кнопке 'Отменить'")
    def click_button_cancel_data_on_page_change_password(self):
        self.wait_element_clickable(*self.locators_by.button_cancel_data)
        button_cancel = self.browser.find_element(*self.locators_by.button_cancel_data)
        button_cancel.click()

    @allure.step("Клик по кнопке 'Назад'")
    def click_button_back(self):
        self.wait_element_clickable(*self.locators_by.button_back)
        button_cancel = self.browser.find_element(*self.locators_by.button_back)
        button_cancel.click()

    @allure.step("Клик на поле 'Подтвердите введённый пароль'.")
    def click_field_confirm_new_password(self):
        field_confirm_new_password = self.browser.find_element(*self.locators_by.field_confirm_new_password_locator)
        field_confirm_new_password.click()

    @allure.step("Клик на поле 'Введите текущий пароль'.")
    def click_field_current_password(self):
        current_password_field = self.browser.find_element(*self.locators_by.field_current_password_locator)
        current_password_field.click()

    @allure.step("Клик на поле 'Задайте новый пароль'.")
    def click_field_new_password(self):
        new_password_field = self.browser.find_element(*self.locators_by.field_create_new_password_locator)
        new_password_field.click()

    @allure.step(
        'Проверка отображения сообщения "Пароль должен содержать не менее 6 знаков,'
        'строчные или заглавные буквы латинского алфавита A-z, цифры от 0 до 9".'
    )
    def check_message_validation_password(self, expected_locator):
        text_message_validation_password = self.browser.find_element(*getattr(self.locators_by, expected_locator)).text
        CommonChecker.check_field_equals(
            text_message_validation_password,
            self.error.message_validation_password,
            assertion_message="Ошибка отображения уведомления о валидации пароля",
        )

    @allure.step("Проверка отображания введеных букв в поле ввода.")
    def check_fields_value(self, expected_locator, expected_value: str):
        field_new_password = self.browser.find_element(*getattr(self.locators_by, expected_locator)).get_attribute(
            "value"
        )
        CommonChecker.check_field_equals(
            field_new_password, expected_value, assertion_message="Ошибка при проверке введенных символов"
        )

    @allure.step("Проверка не отображания введеных букв поле ввода 'Задайте новый пароль'.")
    def check_fields_on_page_change_password_not_equals(self, expected_locator, expected_value: str):
        field_new_password = self.browser.find_element(*getattr(self.locators_by, expected_locator)).get_attribute(
            "value"
        )
        CommonChecker.check_field_not_equals(
            field_new_password, expected_value, assertion_message="Ошибка при проверке введенных символов"
        )

    @allure.step("Очистка поля 'Введите текущий пароль'.")
    def clear_current_password_field(self):
        current_password_field = self.browser.find_element(*self.locators_by.field_current_password_locator)
        current_password_field.send_keys(Keys.CONTROL + "a")
        current_password_field.send_keys(Keys.DELETE)

    @allure.step("Очистка поля 'Задайте новый пароль'.")
    def clear_new_password_field(self):
        new_password_field = self.browser.find_element(*self.locators_by.field_create_new_password_locator)
        new_password_field.send_keys(Keys.CONTROL + "a")
        new_password_field.send_keys(Keys.DELETE)

    @allure.step("Очистка поля 'Подтвердите введённый пароль'.")
    def clear_confirm_password_field(self):
        confirm_password_field = self.browser.find_element(*self.locators_by.field_confirm_new_password_locator)
        confirm_password_field.send_keys(Keys.CONTROL + "a")
        confirm_password_field.send_keys(Keys.DELETE)

    @allure.step("Проверка отображения сообщения о несовпадении паролей.")
    def check_message_mismatch_password(self):
        text_message_mismatch_password = self.browser.find_element(
            *self.locators_by.text_message_missmatch_passwords_locator
        ).text
        CommonChecker.check_field_equals(
            text_message_mismatch_password,
            self.error.message_mismatch_passwords,
            assertion_message="Ошибка отображения уведомления о несовпадении паролей",
        )

    @allure.step("Проверка отображения сообщения о невозможности изменить пароль.")
    def check_message_password_not_change(self):
        text_message_mismatch_password = self.browser.find_element(
            *self.locators_by.text_validation_password_locator
        ).text
        CommonChecker.check_field_equals(
            text_message_mismatch_password,
            self.error.message_not_change_password,
            assertion_message="Ошибка отображения уведомления о неверном текущем пароле",
        )

    @allure.step("Проверка введенного текста в поле.")
    def check_text_in_field(self, expected_locator: str, expected_value: str):
        field_current_password = self.browser.find_element(*getattr(self.locators_by, expected_locator)).text
        CommonChecker.check_field_equals(
            field_current_password, expected_value, assertion_message="Ошибка при проверке введенных символов"
        )

    @allure.step("Проверка отображения кнопки 'Изменить пароль.")
    def check_displaying_button_change_password(self):
        button_change_password = self.browser.find_element(*self.locators_by.button_change_password_locator)
        button_change_password.is_displayed()

    @allure.step("Проверка отображения кнопки 'Смена контрольного вопроса'.")
    def check_displaying_button_change_secret_question(self):
        button_change_secret_question = self.browser.find_element(
            *self.locators_by.button_change_security_question_locator
        )
        button_change_secret_question.is_displayed()

    @allure.step("Проверка наличия элементов на странице.")
    def check_displaying_elements_on_page_change_password(self, expected_locator: str) -> None:
        element_on_page = self.browser.find_element(*getattr(self.locators_by, expected_locator))
        element_on_page.is_displayed()

    @allure.step("Проверка отсутвия элемента введите ваш вопрос на странице.")
    def check_not_displaying_elements_put_your_question(self):
        element_on_page = self.is_element_present(self.locators_by.field_put_your_question)
        CommonChecker.check_field_equals(element_on_page, False, assertion_message="Элемент есть на странице")

    @allure.step("Выбор элемента из всплывающего списка и клик на него.")
    def click_on_elements_on_drop_list(self, expected_locator):
        self.browser.find_element(*self.locators_by.button_drop_list).click()
        self.browser.find_element(*getattr(self.locators_by, expected_locator)).click()

    @allure.step("Ввод ответа на секретный вопрос.")
    def enter_answer_for_your_security_question(self, answer: str):
        create_new_password_field = self.browser.find_element(*self.locators_by.field_put_your_answer)
        create_new_password_field.send_keys(answer)

    @allure.step("Клик по кнопке 'Отменить', на странице секретного вопроса")
    def click_button_cancel_data_on_page_change_security_question(self):
        self.wait_element_clickable(*self.locators_by.button_cancel_data_on_page_change_security_question)
        button_cancel = self.browser.find_element(*self.locators_by.button_cancel_data_on_page_change_security_question)
        button_cancel.click()

    @allure.step("Ввод твоего секретного вопроса.")
    def enter_your_security_question(self, question: str):
        create_new_password_field = self.browser.find_element(*self.locators_by.field_put_your_question)
        create_new_password_field.send_keys(question)

    @allure.step("Нажатие на кнопку выпадение дроплиста")
    def click_on_button_drop_list(self):
        self.browser.find_element(*self.locators_by.button_drop_list).click()
