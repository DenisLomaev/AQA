from typing import Any

import allure
import keyboard
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, browser: webdriver.Chrome, url: str) -> None:
        self.browser = browser
        self.url = url

    def open(self) -> None:
        """Открывает указанную веб-страницу в браузере
        :return: None
        """
        return self.browser.get(self.url)

    def get_url(self):
        """Получает url текущей страницы"""
        return self.browser.current_url

    def is_element_present(self, locator: Any) -> bool:
        """Проверяет, есть ли элемент на странице
        :param locator: Используется для поиска элемента
        :return: True или False
        """
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def wait_element_located(self, find_by: Any, locator: Any, time: int = 10) -> Any:
        """Ожидание для проверки наличия элемента в DOM страницы.
         Это не обязательно означает, что элемент виден.
         :param find_by: Указываем тип поиска(By.ID/By.XPATH и т.п.)
         :param locator: Используется для поиска элемента
         :param time: Время ожидания элемента
        :return: Any
        """
        return WebDriverWait(self.browser, time).until(
            EC.presence_of_element_located((find_by, locator)),
            message=f"Элемент не может быть найден при помощи {locator}",
        )

    def wait_elements_located(self, find_by: Any, locator: Any, time: int = 10) -> dict:
        """Ожидание для проверки наличия хотя бы одного элемента на веб-странице
        :param find_by: Указываем тип поиска(By.ID/By.XPATH и т.п.)
        :param locator: Используется для поиска элемента
        :param time: Время ожидания элемента
        :return: dict
        """
        return WebDriverWait(self.browser, time).until(
            EC.presence_of_all_elements_located((find_by, locator)),
            message=f"Элементы не могут быть найдены при помощи {locator}",
        )

    def wait_element_clickable(self, find_by: Any, locator: Any, time: int = 10) -> Any:
        """Ожидание для проверки кликабельности элемента
        :param find_by: Указываем тип поиска(By.ID/By.XPATH и т.п.)
        :param locator: Используется для поиска элемента
        :param time: Время ожидания элемента
        """
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable((find_by, locator)))

    def wait_for_url(self, url: str, timeout: int = 15) -> Any:
        button = WebDriverWait(self.browser, timeout).until(EC.url_to_be(url))
        return button

    @allure.step("Нажатие клавиши Capslock")
    def turn_on_capslock(self):
        keyboard.send("capslock")
