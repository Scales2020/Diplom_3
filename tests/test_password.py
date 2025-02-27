import allure
from conftest import driver
from constants import Constants
from locators.locators_pass_log import Locators
from pages.password_page import PassPage
from test_data import TestData


class TestPasswordPage:
    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_password_recovery_button_works_to_recovery_field(self, driver):
        pass_page = PassPage(driver)
        pass_page.go_to_password_recovery_page()
        with allure.step("Проверка: открывается форма для восстановления пароля"):
            assert "Восстановление пароля" in pass_page.find_element(Locators.PASSWORD_FORM).text

    @allure.title('Проверяем ввод почты и клик по кнопке "Восстановить"')
    def test_password_email_enter_and_recovery_button_click_success(self, driver):
        pass_page = PassPage(driver)
        pass_page.go_to_password_recovery_page()

        pass_page.find_element(Locators.PASS_RECOV_EMAIL_FIELD).send_keys(TestData.test_email)
        pass_page.find_element(Locators.PASS_RECOV_EMAIL_ENTER_BUT).click()
        with allure.step("Проверка: открывается форма для ввода пароля"):
            assert "Пароль" in pass_page.find_element(Locators.PASS_RECOV_PASSWORD_CHECK).text

    @allure.title('Проверяем клик по кнопке показать/скрыть пароль делает поле активным')
    def test_password_field_text_visibility_check(self, driver):
        pass_page = PassPage(driver)
        pass_page.go_to_password_recovery_page()

        pass_page.find_element(Locators.PASS_RECOV_EMAIL_FIELD).send_keys(TestData.test_email)
        pass_page.find_element(Locators.PASS_RECOV_EMAIL_ENTER_BUT).click()

        password_entry = pass_page.find_element(Locators.PASS_RECOV_PASSWORD_ENTRY)
        password_entry.click()
        password_entry.send_keys(TestData.new_pass)

        pass_page.find_element(Locators.PASS_RECOV_PASSWORD_FIELD_EYE).click()
        
        with allure.step("Проверка: при клике пароль становится видимым (меняется тип в локаторе)"):
            assert password_entry.get_attribute("type") == Constants.password_entry_attr



