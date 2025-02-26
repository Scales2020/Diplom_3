from locators.locators_pass_log import Locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def go_to_loginpage(self):
        self.go_to_mainpage()
        self.find_element(Locators.LOGIN_BUTTON).click()

    def authorisation_with_testdata_newuser(self, mail, passw):
        self.find_element(Locators.AUTH_EMAIL_FIELD).send_keys(mail)
        self.find_element(Locators.AUTH_PASSWORD_FIELD).send_keys(passw)
        self.find_element(Locators.AUTH_SIGNIN_BUTTON).click()



