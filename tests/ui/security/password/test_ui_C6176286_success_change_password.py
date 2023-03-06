import allure
import pytest

from test_data.ui.url_data import MAIN_PAGE_URL
from test_framework.ui.data.user_data import password, valid_password_ui_python, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)
from test_framework.ui.pages.personal_profile_pages.profile_security_page import ProfileSecurityPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6176286")
@allure.title("C6176286. Успешное изменение пароля в личном кабинете.")
def test_ui_C6176286_success_change_password(browser_change_password_after_test):
    main_page = MainPage(browser_change_password_after_test, MAIN_PAGE_URL)
    main_page.open()

    # Авторизация пользователя
    main_page.authorization(phone_number=valid_phone_number_ui_python, password=valid_password_ui_python)

    # Вход в личный кабинет
    profile_page = ProfileMainPage(
        browser_change_password_after_test, url=browser_change_password_after_test.current_url
    )
    profile_page.open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    ProfileGeneralInformationPage(
        browser_change_password_after_test, url=browser_change_password_after_test.current_url
    ).open_profile_security_page()

    # Клик на кнопку "Изменить пароль"
    profile_security_page = ProfileSecurityPage(
        browser_change_password_after_test, url=browser_change_password_after_test.current_url
    )
    profile_security_page.click_on_button_change_password()

    # Ввод текущего пароля
    profile_security_page.enter_current_password(valid_password_ui_python)

    # Проверка введенного текста
    profile_security_page.check_fields_value("field_current_password_locator", valid_password_ui_python)

    # Нажатие на кнопку "глаза" и проверка, что нажатие случилось
    profile_security_page.click_on_button_eye("button_eye_current_password_locator")
    profile_security_page.check_state_button_eye("field_current_password_locator")

    # Ввод нового пароля
    profile_security_page.enter_new_password(password)

    # Нажатие на кнопку "глаза" и проверка, что нажатие случилось
    profile_security_page.click_on_button_eye("button_eye_create_new_password_locator")
    profile_security_page.check_state_button_eye("field_create_new_password_locator")

    # Ввод поддтверждения пароля
    profile_security_page.enter_confirm_new_password(password)

    # Нажатие на кнопку "глаза" и проверка, что нажатие случилось
    profile_security_page.click_on_button_eye("button_eye_confirm_new_password_locator")
    profile_security_page.check_state_button_eye("field_confirm_new_password_locator")

    # Нажатие на кнопку подтвердить
    profile_security_page.click_submit_button()
