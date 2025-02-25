import time

import allure

from locators.konstruktor_locators import KonstrLocators
from locators.lenta_locators import LentaLocators
from locators.locators_list import Locators
from pages.lenta_page import LentaPage
from conftest import driver, api_user_and_order
from test_data import TestData


class TestLentaPage:
    @allure.title('Проверряем, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_to_order_shows_order_details(self,driver):
        test_page = LentaPage(driver)
        test_page.go_to_mainpage()
        test_page.find_element(KonstrLocators.BUTTON_LENTA_ZAKAZOV).click()
        time.sleep(4)
        test_page.find_element(LentaLocators.ANY_ORDER_CLICK).click()
        time.sleep(5)
        assert 'Cостав' in test_page.find_element(LentaLocators.ORDER_DETAILS_CHECK).text

    @allure.title('Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_authorised_user_orders_shown_in_lenta(self, driver, api_user_and_order):
        test_page = LentaPage(driver)
        user = api_user_and_order

        test_page.go_to_loginpage()
        test_page.authorisation_with_testdata_newuser(mail=TestData.new_user["email"],
                                                      passw=TestData.new_user["password"])
        time.sleep(2)
        test_page.find_element(Locators.LOGIN_BUTTON).click()
        test_page.find_element(Locators.HISTORY_OF_ORDERS_MENU).click()
        time.sleep(3)
        print(api_user_and_order.order_number.text)


        last_order_text = test_page.find_element(LentaLocators.LENTA_LAST_ORDER).text
        print(last_order_text)






