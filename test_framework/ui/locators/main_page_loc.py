from selenium.webdriver.common.by import By


class LocatorsMainPage:
    button_by_passport_loc = (By.XPATH, "//button[text()='По паспорту']")
    button_registration_locator = (By.XPATH, "//[@class='button-oQZpw']")
    button_by_phone_locator = (By.XPATH, '//button[text()="По телефону"]')
    button_by_passport_number_locator = (By.XPATH, '//button[@name="passport"]')
    button_hidden_password_locator = (By.XPATH, '//button[@class="openPassword-iJrI1"]')
    button_login_locator = (By.XPATH, '//button[text()="Войти"]')
    button_login_status_enabled = (By.XPATH, "//*[@class='accept-active-oMhtC']")
    button_login_status_disabled = (By.XPATH, '//*[text()="Войти"][@disabled]')
    button_account_locator = (By.XPATH, '//*[@id="root"]/header/div/div[1]/a[1]/div')

    field_phone_locator = (By.XPATH, '//*[@id="telephone"]')
    field_passport_number_locator = (By.XPATH, '//input[@placeholder="Паспорт"]')
    field_password_locator = (By.XPATH, "//*[@id='password']")
    field_passport_loc = (By.XPATH, "//input[@class='input-_IqRo' and @placeholder='Паспорт']")
    text_above_the_passport_field = (By.XPATH, "//*[text()='Паспорт']")
    text_above_the_password_field = (By.XPATH, "//*[text()='Пароль']")
    text_not_enough_characters_locator = (By.XPATH, '//*[@class="error-n1TVM"]')
    text_about_on_turned_capslock_locator = (By.XPATH, '//div[@class="error-uqtw3"]')
    text_validation_password_locator = (By.XPATH, '//*[@class="error-uqtw3"]')
    logo_locator = (By.XPATH, "//*[@class='logo-qpYYn']")

    registration_form_locator = (By.XPATH, '//*[@id="root"]/div/section/div[7]')
