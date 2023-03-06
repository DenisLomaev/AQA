from selenium.webdriver.common.by import By


class LocatorsProfileNotificationPage:
    profile_notification_page_locator = (By.XPATH, "//*[text()='Настройки']")

    checkbox_email_notification_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/span/span[1]/input')
    checkbox_sms_notification_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/span/span[1]/input')
    checkbox_push_notification_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/span/span[1]/input')

    field_input_email_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[1]/div[1]/input')
    field_input_phone_number_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[2]/div[1]/div/input')

    text_success_change_email_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[1]/div[2]/p')
    text_success_change_phone_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[2]/div[2]/p')

    button_save_changes_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[3]/div[1]')
    button_skip_changes_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[3]/div[2]')

    label_email_notification_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/label[2]')
    label_sms_notification_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/label[2]')
    label_push_notification_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/label[2]')
