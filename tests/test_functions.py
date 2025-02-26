import time
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver, api_user
from locators.functional_locators import KonstrLocators
from pages.functional_page import FunctionalPage
from test_data import TestData


class TestFunctions:
    @allure.title("Проверяем переход из кабинета в конструктор по кнопке Конструктор")
    def test_go_to_konstruktor_by_click_to_konstr_button(self, driver):
        test_page = FunctionalPage(driver)
        test_page.go_to_login()
        test_page.find_element(KonstrLocators.BUTTON_KONSTRUKTOR).click()

        with allure.step("При клике на Конструктор появляется раздел Соберите Бургер"):
            assert "Соберите бургер" in test_page.find_element(KonstrLocators.MAINPAGE_KONSTRUKTOR).text

    @allure.title("Проверяем переход из кабинета в Ленту заказов по кнопке ЛЕНТА")
    def test_go_to_lenta_zakazov_by_click_to_lenta_button(self, driver):
        test_page = FunctionalPage(driver)
        test_page.go_to_login()
        test_page.find_element(KonstrLocators.BUTTON_LENTA_ZAKAZOV).click()

        with allure.step("Открывается раздел Лента заказов"):
            assert "Лента заказов" in test_page.find_element(KonstrLocators.MAINPAGE_LENTA_ZAKAZOV).text

    @allure.title("Проверяем что если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_to_ingredient_opens_details(self, driver):
        test_page = FunctionalPage(driver)
        test_page.go_to_mainpage()
        test_page.find_element(KonstrLocators.BULKA_PICTURE).click()
        time.sleep(3)

        with allure.step("Открылось модальное окно с деталями"):
            assert "Детали ингредиента" in test_page.find_element(KonstrLocators.BULKA_DETAILS).text

    @allure.title("Проверяем что всплывающее окно закрывается кликом по крестику")
    def test_krestik_to_close_modal(self, driver):
        test_page = FunctionalPage(driver)
        test_page.go_to_mainpage()
        test_page.find_element(KonstrLocators.BULKA_PICTURE).click() #клик на ингредиент булка, чтобы вызвать модальное окно
        test_page.find_element(KonstrLocators.KRESTIK).click() #клик по крестику, чтобы закрыть модальное окно

        with allure.step("Проверка: модальное окно с деталями ингредиента закрывается"):
            assert WebDriverWait(driver,10).until(expected_conditions.invisibility_of_element_located(KonstrLocators.BULKA_DETAILS))

    @allure.title("Проверяем, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_ingredient_counter_raise_when_adding_ingredient_to_order(self, driver):
        test_page = FunctionalPage(driver)
        test_page.go_to_mainpage()
        test_page.drag_and_drop_element(KonstrLocators.INGR_DRAG, KonstrLocators.INGR_DROP)

        counter = test_page.find_element(KonstrLocators.INGR_COUNTER).text
        with allure.step("Проверка: при перетаскивании булочки ее счетчик уже не равен 0"):
            assert counter != "0"

    @allure.title("Проверяем, что залогиненный пользователь может оформить заказ")
    def test_authorised_user_makes_order_successfully(self, driver, api_user):
        test_page = FunctionalPage(driver)
        user = api_user
        test_page.go_to_login()
        test_page.authorisation_with_testdata_newuser(mail=TestData.new_user["email"], passw=TestData.new_user["password"])
        test_page.drag_and_drop_element(KonstrLocators.INGR_DRAG, KonstrLocators.INGR_DROP)
        test_page.find_element(KonstrLocators.TO_ORDER).click()
        time.sleep(4)

        with allure.step("Проверяем, что открывается модальное окно с фразой 'идентификатор заказа'"):
            assert 'идентификатор заказа' in test_page.find_element(KonstrLocators.ORDER_PLACED).text
        with allure.step("Выводим номер созданного заказа"):
            print(test_page.find_element(KonstrLocators.ORDER_NUMBER).text)




