import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.lenta_locators import LentaLocators
from locators.locators_pass_log import Locators
from pages.lenta_page import LentaPage
from conftest import driver, api_user_and_order, api_user
from test_data import TestData


class TestLentaPage:
    @allure.title('Проверяем, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_to_order_shows_order_details(self,driver):
        test_page = LentaPage(driver)
        test_page.go_to_mainpage()
        test_page.find_element(LentaLocators.BUTTON_LENTA_ZAKAZOV).click()
        test_page.find_element(LentaLocators.ANY_ORDER_CLICK).click()
        assert 'Cостав' in test_page.find_element(LentaLocators.ORDER_DETAILS_CHECK).text

    @allure.title('Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_authorised_user_orders_shown_in_lenta(self, driver, api_user_and_order):
        test_page = LentaPage(driver)
        user = api_user_and_order

        test_page.go_to_loginpage()
        test_page.authorisation_with_testdata_newuser(mail=TestData.new_user["email"], passw=TestData.new_user["password"])
        test_page.find_element(Locators.LOGIN_BUTTON).click()
        time.sleep(8)
        test_page.find_element(Locators.HISTORY_OF_ORDERS_MENU).click()

        with allure.step('Получаем номер последнего заказа'):
            last_order_text = test_page.find_element(LentaLocators.LENTA_LAST_ORDER).text

        test_page.find_element(LentaLocators.BUTTON_LENTA_ZAKAZOV).click()
        time.sleep(5)
        element_locator = (By.XPATH, f"//p[contains(text(), '{last_order_text}')]")
        with allure.step('Проверяем, что в Ленте Заказов есть заказ с таким же номером'):
            assert last_order_text in WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(element_locator)).text


    @allure.title('Проверяем, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_new_order_increases_general_counter_of_all_orders(self , driver, api_user):
        test_page = LentaPage(driver)
        user = api_user
        test_page.go_to_mainpage()
        test_page.find_element(LentaLocators.BUTTON_LENTA_ZAKAZOV).click()
        total_count_before = test_page.find_element(LentaLocators.TOTAL_COUNTER).text
        with allure.step(f'Счетчик заказов в начале (ДО создания заказа): {total_count_before}'):
            test_page.go_to_loginpage()

        test_page.authorisation_with_testdata_newuser(mail=TestData.new_user["email"], passw=TestData.new_user["password"])
        test_page.create_new_order(LentaLocators.INGR_DRAG_1, LentaLocators.INGR_DRAG_2, LentaLocators.INGR_DROP)
        time.sleep(3)
        test_page.find_element(LentaLocators.KRESTIK_ORDER_MODAL).click()

        test_page.find_element(LentaLocators.BUTTON_LENTA_ZAKAZOV).click()

        with allure.step('Счетчик заказов ПОСЛЕ создания заказа'):
            total_count_after = test_page.find_element(LentaLocators.TOTAL_COUNTER).text

        with allure.step(f'Проверяем увеличение счетчика: ДО ({total_count_before}) и ПОСЛЕ ({total_count_after}) создания заказа'):
            assert total_count_after > total_count_before


    @allure.title('Проверяем, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_new_order_increases_today_counter_of_all_orders(self, driver, api_user):
        test_page = LentaPage(driver)
        user = api_user
        test_page.go_to_mainpage()
        test_page.find_element(LentaLocators.BUTTON_LENTA_ZAKAZOV).click()
        today_count_before = test_page.find_element(LentaLocators.TODAY_COUNTER).text
        with allure.step(f'Счетчик заказов в начале (ДО создания заказа): {today_count_before}'):
            test_page.go_to_loginpage()

        test_page.authorisation_with_testdata_newuser(mail=TestData.new_user["email"], passw=TestData.new_user["password"])
        test_page.create_new_order(LentaLocators.INGR_DRAG_1, LentaLocators.INGR_DRAG_2, LentaLocators.INGR_DROP)
        time.sleep(3)
        test_page.find_element(LentaLocators.KRESTIK_ORDER_MODAL).click()

        test_page.find_element(LentaLocators.BUTTON_LENTA_ZAKAZOV).click()

        with allure.step('Счетчик заказов ПОСЛЕ создания заказа'):
            today_count_after = test_page.find_element(LentaLocators.TODAY_COUNTER).text

        with allure.step(f'Проверяем увеличение счетчика: ДО ({today_count_before}) и ПОСЛЕ ({today_count_after}) создания заказа увеличился'):
            assert today_count_after > today_count_before


    @allure.title('Проверяем, что после оформления заказа его номер появляется в разделе В РАБОТЕ')
    def test_new_order_is_shown_in_list_of_orders_in_progress(self, driver, api_user):
        test_page = LentaPage(driver)
        user = api_user

        test_page.go_to_loginpage()
        test_page.authorisation_with_testdata_newuser(mail=TestData.new_user["email"], passw=TestData.new_user["password"])

        test_page.create_new_order(LentaLocators.INGR_DRAG_1, LentaLocators.INGR_DRAG_2, LentaLocators.INGR_DROP)
        time.sleep(3)
        latest_order = test_page.find_element(LentaLocators.ORDER_NUMBER).text
        with allure.step(f'Соханяем номер нового заказа: {latest_order} и закрываем окно'):
            test_page.find_element(LentaLocators.KRESTIK_ORDER_MODAL).click()

        with allure.step('Переходим в ЛЕНТУ ЗАКАЗОВ и проверяем список заказов, которые готовятся'):
            test_page.find_element(LentaLocators.BUTTON_LENTA_ZAKAZOV).click()
            time.sleep(1)
        order_in_list = test_page.find_element(LentaLocators.ORDERS_IN_PROGRESS).text
        order_in_progress = order_in_list[1:] #убираем лишний знак (0 в начале)
        with allure.step(f'Cверяем номер созданного заказа {latest_order} и заказа в списке В РАБОТЕ {order_in_progress}'):
            assert latest_order == order_in_progress



