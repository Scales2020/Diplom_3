from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.URL

    def go_to_mainpage(self):
        self.driver.get(self.url)

    def find_element(self,locator, time=20):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))




