from selenium.webdriver.common.by import By


class LocatorsProfileSecurityPage:
    button_change_password_locator = (By.XPATH, "//span[@class='text-pStQs'][text()='Изменить пароль']")
    button_change_security_question_locator = (By.XPATH, "//a[@class='link-MmrZA'][2]/span[2]")
    button_eye_current_password_locator = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/form/div[1]/div/button")
    button_eye_create_new_password_locator = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/form/div[2]/div/button")
    button_eye_confirm_new_password_locator = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/form/div[3]/div/button")
    button_back = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/button")
    button_confirm = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/form/div[4]/button[1]")
    button_cancel = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/form/div[4]/button[2]")
    button_drop_list = (By.XPATH, "//span[@class='toggle-wLw71']")

    field_current_password_locator = (By.XPATH, "//input[@name='oldPassword']")
    field_create_new_password_locator = (By.XPATH, "//input[@name='password']")
    field_confirm_new_password_locator = (By.XPATH, "//input[@name='confirmPassword']")
    field_choose_your_question = (By.XPATH, '//input[@class ="selected-NAG4q"]')
    field_put_your_question = (By.XPATH, '//textarea[@name="question"]')
    field_put_your_answer = (By.XPATH, '//textarea[@name="answer"]')

    button_submit_locator = (By.XPATH, "//button[@type='submit']")
    button_submit_locator_disabled = (By.XPATH, "//button[@type='submit'][@disabled]")
    button_cancel_data = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/form/div[4]/button[2]")
    button_cancel_data_on_page_change_security_question = (By.XPATH, '//button[@class="cancel-nsgiP"]')

    text_success_change_password_locator = (By.XPATH, "//*[@class='span-OyM7u']")

    text_validation_password_locator = (By.XPATH, "//span[@class='message-qcCa_ message-error-Rscxs']")
    text_message_missmatch_passwords_locator = (By.XPATH, "// div[@class ='container-tYrbX'][3] / span[2]")
    text_validation_password_locator_under_new_password = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div/div/form/div[2]/span[2]",
    )
    text_header = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/span")
    text_header_down = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/p")

    element_put_your_question_in_drop_list = (By.XPATH, "//div[@class='questions-open-lUIr9']/div[6]")
    element_lastname_your_mother_in_drop_list = (By.XPATH, "//div[@class='question-Yhn2l'][1]")
    element_name_your_close_friend = (By.XPATH, "//div[@class='question-Yhn2l'][2]")
    element_your_favorite_book = (By.XPATH, "//div[@class='question-Yhn2l'][3]")
    element_your_favorite_color = (By.XPATH, "//div[@class='question-Yhn2l'][4]")
    element_your_favorite_dish = (By.XPATH, "//div[@class='question-Yhn2l'][5]")
