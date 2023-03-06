import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType

from config import env
from test_framework.ui.data.user_data import (
    password,
    valid_email_ui_python,
    valid_password_ui_python,
    valid_phone_number_ui_python,
)
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)
from test_framework.ui.pages.personal_profile_pages.profile_security_page import ProfileSecurityPage
from test_framework.ui.pages.personal_profile_pages.profile_settings_page import ProfileSettingsPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


def pytest_addoption(parser):
    """
        Перед запуском Geckodriver(firefox) выполнить команду: pip install -U selenium
    для запуска :
        pytest -s -v --tb=short --browser_name=firefox test_conftest.py
    по умолчанию броузер 'chrome'
        pytest -s -v --tb=line test_main_page.py
    """
    parser.addoption("--browser_name", default="chrome", help="Выберите браузер: chrome или firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser = browser_set(request)
    browser.implicitly_wait(5)
    yield browser
    try:
        ProfileMainPage(browser).click_logout()
    except TimeoutException as err:
        return err
    finally:
        time.sleep(2)
        browser.quit()


@pytest.fixture(scope="function")
def browser_change_password_after_test(request):
    browser = browser_set(request)
    browser.implicitly_wait(5)
    yield browser
    try:
        ProfileGeneralInformationPage(browser, url=browser.current_url).open_profile_security_page()
        profile_security_page = ProfileSecurityPage(browser, url=browser.current_url)
        profile_security_page.click_on_button_change_password()
        profile_security_page.enter_current_password(password)
        profile_security_page.enter_new_password(valid_password_ui_python)
        profile_security_page.enter_confirm_new_password(valid_password_ui_python)
        profile_security_page.click_submit_button()
        ProfileMainPage(browser).click_logout()
    finally:
        time.sleep(2)
        browser.quit()


@pytest.fixture(scope="function")
def browser_change_email_after_test(request):
    browser = browser_set(request)
    browser.implicitly_wait(5)
    yield browser
    try:
        profile_settings_page = ProfileSettingsPage(browser)
        profile_settings_page.open_profile_options_page()
        profile_settings_page.click_on_button_change_email()
        profile_settings_page.enter_new_email_to_email_field(valid_email_ui_python)
        profile_settings_page.click_on_save_changes_button()
        ProfileMainPage(browser).click_logout()
    finally:
        time.sleep(2)
        browser.quit()


@pytest.fixture(scope="function")
def browser_change_phone_number_after_test(request):
    browser = browser_set(request)
    browser.implicitly_wait(5)
    yield browser
    try:
        profile_settings_page = ProfileSettingsPage(browser)
        profile_settings_page.open_profile_options_page()
        profile_settings_page.click_on_button_change_phone_number()
        profile_settings_page.enter_new_phone_number_to_phone_number_field(valid_phone_number_ui_python)
        profile_settings_page.click_on_save_changes_button()
        ProfileMainPage(browser).click_logout()
    finally:
        time.sleep(2)
        browser.quit()


def browser_set(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name.lower() == "chrome":
        if env == "linux":
            return __create_chrome_ci()
        return __create_chrome()
    elif browser_name.lower() == "firefox" or "ff":
        return __create_firefox()
    elif browser_name.lower() == "chromium":
        return __create_chromium()
    else:
        raise ValueError(f"{browser_name} не поддерживается. --browser_name должен быть chrome или firefox")


def __create_chrome():
    browser_chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser_chrome.maximize_window()
    return browser_chrome


def __create_chrome_ci():
    chrom_options = webdriver.ChromeOptions()
    chrom_options.add_argument("--no-sandbox")
    chrom_options.add_argument("--headless")
    chrom_options.add_argument("--disable-gpu")
    browser_chrome = webdriver.Chrome(chrome_options=chrom_options)
    return browser_chrome


def __create_firefox():
    browser_firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser_firefox.maximize_window()
    return browser_firefox


def __create_chromium():
    browser_chromium = webdriver.Chrome(executable_path=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    browser_chromium.set_window_size(1280, 860)
    return browser_chromium
