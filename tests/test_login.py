import allure
from conftest import driver, api_user
from constants import Constants
from locators.locators_pass_log import Locators
from pages.login_page import LoginPage
from test_data import TestData


class TestLoginPage:
    @allure.title('Проверяем переход по кнопке "Личный кабинет"')
    def test_login_click_to_login_page(self, driver):
        login_p = LoginPage(driver)
        login_p.go_to_mainpage()
        login_p.find_element(Locators.LOGIN_BUTTON).click()
        with allure.step("Проверяем переход по кнопке Личный кабинет- появляется надпись 'Вход' "):
            assert "Вход" in login_p.find_element(Locators.LOGIN_PAGE_CHECK).text

    @allure.title('Проверяем переход в раздел «История заказов»')
    def test_go_to_orders_history_success(self, driver, api_user):
        login_p = LoginPage(driver)
        user = api_user
        login_p.go_to_loginpage()
        login_p.authorisation_with_testdata_newuser(mail=TestData.new_user["email"], passw=TestData.new_user["password"])
        login_p.wait_and_click(10, Locators.LOGIN_BUTTON)

        attribute = login_p.button_attribute_check(10, Locators.HISTORY_OF_ORDERS_MENU)

        with allure.step("Проверка: цвет названия раздела при клике изменился"):
            assert attribute == Constants.button_new_look


    @allure.title('Проверяем выход из аккаунта')
    def test_logout_success(self, driver, api_user):
        login_p = LoginPage(driver)
        user = api_user
        login_p.go_to_loginpage()
        login_p.authorisation_with_testdata_newuser(mail=TestData.new_user["email"], passw=TestData.new_user["password"])
        login_p.wait_and_click(5, Locators.LOGIN_BUTTON)
        login_p.find_element(Locators.AUTH_SIGNOUT_BUTTON).click()

        with allure.step("Проверка: появилась надпись ВХОД"):
            assert "Вход" in login_p.find_element(Locators.LOGIN_PAGE_CHECK).text


