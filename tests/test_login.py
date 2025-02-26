import time
import allure

from conftest import driver, api_user
from locators.locators_pass_log import Locators
from pages.login_page import LoginPage
from test_data import TestData


class TestLoginPage:
    def test_login_click_to_login_page(self, driver):
        login_p = LoginPage(driver)
        login_p.go_to_mainpage()
        login_p.find_element(Locators.LOGIN_BUTTON).click()
        with allure.step("Проверяем переход по кнопке Личный кабинет- появляется надпись 'Вход' "):
            assert "Вход" in login_p.find_element(Locators.LOGIN_PAGE_CHECK).text

    def test_go_to_orders_history_success(self, driver, api_user):
        login_p = LoginPage(driver)
        user = api_user
        login_p.go_to_loginpage()
        login_p.authorisation_with_testdata_newuser(mail=TestData.new_user["email"], passw=TestData.new_user["password"])
        time.sleep(3)
        login_p.find_element(Locators.LOGIN_BUTTON).click()

        history_button = login_p.find_element(Locators.HISTORY_OF_ORDERS_MENU)
        history_button.click()

        with allure.step("Проверяем переход в раздел История заказов - цвет названия раздела при клике изменился"):
            assert history_button.get_attribute("class") == "Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9"


    def test_logout_success(self, driver, api_user):
        login_p = LoginPage(driver)
        user = api_user
        login_p.go_to_loginpage()
        login_p.authorisation_with_testdata_newuser(mail=TestData.new_user["email"], passw=TestData.new_user["password"])
        time.sleep(3)
        login_p.find_element(Locators.LOGIN_BUTTON).click()
        login_p.find_element(Locators.AUTH_SIGNOUT_BUTTON).click()

        with allure.step("Проверяем  выход из аккаунта - появилась надпись ВХОД"):
            assert "Вход" in login_p.find_element(Locators.LOGIN_PAGE_CHECK).text


