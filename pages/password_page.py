from locators.locators_list import Locators
from pages.base_page import BasePage


class PassPage(BasePage):
    def go_to_password_recovery_page(self):
        self.go_to_mainpage()
        self.find_element(Locators.LOGIN_BUTTON).click()
        self.find_element(Locators.PASSWORD_BUT).click()

