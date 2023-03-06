from selenium.webdriver.common.by import By


class LocatorsProfileCardsPage:
    button_expand_locator = (By.XPATH, "//button[@class='expand-M1khJ']")

    card_gor_classic_image_locator = (By.XPATH, "//*[text()='GoR Classic']")
    card_gor_gold_image_locator = (By.XPATH, "//*[text()='GoR Gold']")
    card_gor_smart_image_locator = (By.XPATH, "//*[text()='GoR Smart Purchase ']")

    card_one_locator = (By.XPATH, "//li[@class='container-XBhb4'][1]")
    card_two_locator = (By.XPATH, "//li[@class='container-XBhb4'][2]")
    card_four_locator = (By.XPATH, "//li[@class='container-XBhb4'][4]")
    card_five_locator = (By.XPATH, "//li[@class='container-XBhb4'][5]")

    tab_information_locator = (By.XPATH, "//*[text()='Информация']")
    tab_history_locator = (By.XPATH, "//*[text()='История']")
    tab_control_locator = (By.XPATH, "//*[text()='Управление']")

    label_status_locator = (By.XPATH, "//*[text()='Статус']")
    label_currency_locator = (By.XPATH, "//*[text()='Валюта']")
    label_validity_date_locator = (By.XPATH, "//*[text()='Срок действия']")
    label_client_locator = (By.XPATH, "//*[text()='Держатель карты']")
    label_card_number_locator = (By.XPATH, "//*[text()='Номер карты']")
    label_account_number_locator = (By.XPATH, "//*[text()='Номер счета']")

    field_status_locator = (By.XPATH, "//*[@class ='content-A6tlz']/div/div[1]/div[2]/p")
    field_currency_locator = (By.XPATH, "//*[@class ='content-A6tlz']/div/div[2]/div[2]/p")
    field_validity_date_locator = (By.XPATH, "//*[@class ='content-A6tlz']/div/div[3]/div[2]/p")
    field_client_locator = (By.XPATH, "//*[@class ='content-A6tlz']/div/div[4]/div[2]/p")
    field_card_number_locator = (By.XPATH, "//*[@class ='content-A6tlz']/div/div[5]/div[2]/p")
    field_account_number_locator = (By.XPATH, "//*[@class ='content-A6tlz']/div/div[6]/div[2]/p")

    copy_info_client_locator = (By.XPATH, "//*[@class ='content-A6tlz']/div/div[4]/div[2]/button")
    copy_info_card_number_locator = (By.XPATH, "//*[@class ='content-A6tlz']/div/div[5]/div[2]/button")
    copy_info_account_number_locator = (By.XPATH, "//*[@class ='content-A6tlz']/div/div[6]/div[2]/button")

    button_card_money_transfer_loc = (By.XPATH, "//*[text()='Перевод на другую карту']")
    button_credit_detail_locator = (By.XPATH, "//*[text()='Детали кредита']")

    form_card_info_locator = (By.XPATH, "//div[@class='statement-cgAhB']")
    calendar_locator = (By.XPATH, "//div[@class='calendarBody']")
