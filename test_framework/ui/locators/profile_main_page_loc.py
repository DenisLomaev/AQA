from selenium.webdriver.common.by import By


class LocatorsProfileMainPage:
    profile_general_information_page_locator = (By.XPATH, "//div[@class='user-photo-tkrf0']")
    profile_cards_page_locator = (By.XPATH, "//a[@class='item-base-HF_xD'][@href='#/my_cards']")
    button_credits_section = (By.XPATH, "//span[text()='Кредиты']")
    button_credit_product = (By.XPATH, "//span[text()='Кредитные продукты']")
    profile_transfer_via_cards_locator = (By.XPATH, "//*[@class='item-text-OfK2X'][text()='Переводы']")
    button_logout_locator = (By.XPATH, '//*[@id="root"]/header/div/div[1]/a[2]/div')

    exchange_table_currency_column_name = (By.XPATH, "//p[@class='currency-tBF8u'][text()='Валюта']")
    exchange_table_purchase_column_name = (By.XPATH, "//p[@class='buying-_GWMD'][text()='Покупка']")
    exchange_table_sale_column_name = By.XPATH, "//p[text()='Продажа']"
    exchange_table_flag_image = (By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div[1]/img')
    exchange_table_country_code = (By.XPATH, "//strong[text()='CHF']")
    exchange_table_currency_country_name = (By.XPATH, "//label[text()='Швейцарский франк']")
    exchange_table_bye_currency = (By.XPATH, '//*[@class="content-SJCj4"]/div[2]/div/div[2]/div[1]')
    exchange_table_sell_currency = (By.XPATH, '//*[@class="content-SJCj4"]/div[2]/div/div[2]/div[2]')

    popular_services_phone_pay_locator = (By.XPATH, '//span[@class="icon-NPK39 icon1-k6fvd"]')
    popular_services_phone_pay_label_locator = (By.XPATH, "//span[text()='Оплата связи']")
    popular_services_money_transfer_locator = (By.XPATH, '//span[@class="icon-NPK39 icon2-j4QaK"]')
    popular_services_money_transfer_label_locator = (By.XPATH, "//span[text()='Перевод на карту']")
    popular_services_utilities_locator = (By.XPATH, '//span[@class="icon-NPK39 icon3-JdyWG"]')
    popular_services_utilities_label_locator = (By.XPATH, "//span[@class='text-Op1t3'][text()='Депозиты']")
    popular_services_exchange_locator = (By.XPATH, '//span[@class="icon-NPK39 icon4-Oarh9"]')
    popular_services_exchange_label_locator = (By.XPATH, "//span[text()='Обмен валюты']")
    popular_services_add_new_service_locator = (By.XPATH, '//span[@class="icon-NPK39 icon-add-Zmtt_"]')
    popular_services_add_new_service_label_locator = (By.XPATH, "//span[text()='Добавить']")

    footer_consultation_loc = (By.XPATH, "//*[text()='Консультация по картам']")
    footer_for_fiz_client = (By.XPATH, "//*[text()='Для физических лиц']")
    footer_address = (By.XPATH, "//*[text()='Юридический адрес']")
    footer_button_link_appstore_locator = (By.XPATH, "//button[@class='apple-onWRl']")
    footer_button_link_play_market_locator = (By.XPATH, "//button[@class='google-N2BzP']")
