from selenium.webdriver.common.by import By


class LocatorsProfileGeneralInformationPage:
    profile_security_page_locator = (By.XPATH, "//*[@class='item-h0ZnP'][text()='Безопасность']")

    tab_general_information_locator = (By.XPATH, "//*[text()='Общая информация']")
    tab_security_locator = (By.XPATH, "//*[text()='Безопасность']")
    tab_notifications_locator = (By.XPATH, "//*[text()='Уведомления']")
    tab_settings_locator = (By.XPATH, "//*[text()='Настройки']")

    label_first_name_locator = (By.XPATH, "//span[text()='Имя']")
    label_last_name_locator = (By.XPATH, "//span[text()='Фамилия']")
    label_past_name_locator = (By.XPATH, "//span[text()='Отчество']")
    field_id_locator = (By.XPATH, "//span[text()='ID']")
    label_telephone_locator = (By.XPATH, "//span[text()='Телефон']")
    label_email_locator = (By.XPATH, "//span[text()='Электронная почта']")
    label_resident_locator = (By.XPATH, "//span[text()='Резидентство']")

    field_last_name_locator = (By.XPATH, '//*[@class="container-fACr2"]/div[1]/p')
    field_first_name_locator = (By.XPATH, '//*[@class="container-fACr2"]/div[2]/p')
    field_past_name_locator = (By.XPATH, '//*[@class="container-fACr2"]/div[3]/p')
    field_telephone_locator = (By.XPATH, '//*[@class="container-fACr2"]/div[4]/p')
    field_email_locator = (By.XPATH, '//*[@class="container-fACr2"]/div[5]/p')
    field_resident_locator = (By.XPATH, '//*[@class="container-fACr2"]/div[6]/p')

    radio_button_resident_locator = (By.XPATH, "//label[text()='Резидент РФ']")
    radio_button_no_resident_locator = (By.XPATH, "//label[text()='Нерезидент РФ']")
