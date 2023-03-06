from selenium.webdriver.common.by import By


class LocatorsProfileSettingsPage:
    profile_settings_page_locator = (By.XPATH, "//*[text()='Настройки']")
    button_change_email_locator = (By.XPATH, '//*[@class="form-J8xza"]/div[1]/div[2]/button')
    button_change_phone_number_locator = (By.XPATH, '//*[@class="form-J8xza"]/div[2]/div[2]/button')
    button_save_changes_locator = (By.XPATH, '//*[@class="btn-container-taqlj"]/div[1]')
    button_skip_changes_locator = (By.XPATH, '//*[@class="btn-container-taqlj"]/div[2]')
    field_email_locator = (By.XPATH, "//*[@id='email']")
    field_phone_number_locator = (By.XPATH, "//*[@id='phone']")
    message_email_success_changed = (By.XPATH, "//*[@class='text-sIyPi'][text()='Email адрес подтверждён']")
    message_email_not_changed = (By.XPATH, "//div[@class='edit-wrapper-MLr_R']/p")
    message_phone_number_success_changed_locator = (By.XPATH, "//*[@class='text-sIyPi'][text()='Номер подтверждён']")
    message_phone_number_not_changed_locator = (By.XPATH, "//*[@class='text-FGFeZ'][text()='Номер не подтверждён']")
    link_how_deactivate_account_locator = (By.XPATH, '//div[@class="questions-XwDcA"]/p[1]/a')
    link_in_change_fio_block_locator = (By.XPATH, '//div[@class="questions-XwDcA"]/p[2]/a')
    link_other_way_to_change_fio_block_locator = (By.XPATH, '//div[@class="questions-XwDcA"]/div[2]/a')
