import time

import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.URL

    @allure.step("Переход на главную страницу")
    def go_to_mainpage(self):
        self.driver.get(self.url)

    @allure.step("Поиск элемента с локатором {locator} с таймаутом {time} секунд")
    def find_element(self,locator, time=20):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Клик и ожидание прогрузки страницы")
    def click_and_wait(self, loc, sec):
        self.find_element(loc)
        time.sleep(sec)

    @allure.step("Ожидание прогрузки страницы и клик")
    def wait_and_click(self, sec, loc):
        time.sleep(sec)
        self.find_element(loc)

    @allure.step("Поиск элемента(заказа) с условием 'присутствия на странице'")
    def find_order(self,locator, time=20):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator))




