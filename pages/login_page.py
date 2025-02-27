import time
import allure

from locators.locators_pass_log import Locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Переход на страницу логина")
    def go_to_loginpage(self):
        self.go_to_mainpage()
        self.find_element(Locators.LOGIN_BUTTON).click()

    @allure.step("Авторизация нового пользователя  с тестовыми данными")
    def authorisation_with_testdata_newuser(self, mail, passw):
        self.find_element(Locators.AUTH_EMAIL_FIELD).send_keys(mail)
        self.find_element(Locators.AUTH_PASSWORD_FIELD).send_keys(passw)
        self.find_element(Locators.AUTH_SIGNIN_BUTTON).click()


    @allure.step("Поиск аттрибута элемента для проверки теста")
    def button_attribute_check(self, sec, loc):
        time.sleep(sec)
        button = self.find_element(loc)
        button.click()
        return button.get_attribute("class")





