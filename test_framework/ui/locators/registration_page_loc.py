from selenium.webdriver.common.by import By


class LocatorsRegistrationPage:
    field_phone_locator = (By.XPATH, "//form[@class='form-Uleqs']/div/input")
    field_sms_code_locator = (By.XPATH, "//input[@name='smsCode']")

    field_first_name_locator = (By.XPATH, "//input[@name='name']")
    field_middle_name_locator = (By.XPATH, "//input[@name='patronymic']")
    field_last_name_locator = (By.XPATH, "//input[@name='surname']")
    field_passport_number_locator = (By.XPATH, "//*[@placeholder='Номер паспорта']")
    field_email_locator = (By.XPATH, "//input[@class='rectangular-input-eFigc']")

    field_create_password_locator = (By.XPATH, "//input[@placeholder='Придумайте пароль']")
    field_confirm_create_password_locator = (By.XPATH, "//input[@placeholder='Подтвердите пароль']")

    field_secret_question_locator = (By.XPATH, "//div[@class='container-k6_bS']")
    field_selected_secret_question_locator = (By.XPATH, "//div[text()='Какой ваш любимый цвет?']")
    field_select_create_secret_question_locator = (By.XPATH, "//div[text()='Написать свой вопрос']")
    field_create_secret_question_locator = (By.XPATH, "//textarea[@name='answer']")
    field_create_your_secret_question_locator = (By.XPATH, "//textarea[@name='question']")
    field_answer_on_secret_question_locator = (By.XPATH, "//textarea[@name='answer']")

    congratulations_text_locator = (By.XPATH, "//section[@class='popup-rZs7M']/h2")
    congratulations_message_text_locator = (By.XPATH, "//section[@class='popup-rZs7M']/p")

    button_continue_locator = (By.XPATH, "//button[@class='accept-active-oMhtC']")
    button_back_locator = (By.XPATH, "//button[@class='back-w0aMd']")
    button_close_locator = (By.XPATH, "//button[@class='close-HoR8X']")

    text_enter_number_locator = (By.XPATH, "//*[text()='Введите номер телефона']")

    radio_button_resident_locator = (By.XPATH, "//input[@name='resident']")
    radio_button_no_resident_locator = (By.XPATH, "//input[@name='notresident']")
    button_enter_with_registration_data_locator = (By.XPATH, '//button[@class="accept-active-oMhtC"]')

    link_privacy_policy_locator = (By.XPATH, "//*[text()[contains(.,'Политикой')]]")
    link_banking_rules_locator = (By.XPATH, "//*[text()[contains(.,'Правила')]]")
