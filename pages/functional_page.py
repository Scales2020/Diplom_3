import allure
from selenium.webdriver import ActionChains

from conftest import driver
from locators.locators_list import Locators
from pages.base_page import BasePage
from route_user import APIUser


class FunctionalPage(BasePage):
    def go_to_login(self):
        self.go_to_mainpage()
        self.find_element(Locators.LOGIN_BUTTON).click()


    @allure.step('Перетаскиваем ингредиент из списка в корзину(конструктор бургера)')
    def drag_and_drop_element(self, drag_elem, drop_elem):
        drag = self.find_element(drag_elem)
        drop = self.find_element(drop_elem)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag, drop)
        actions.perform()

    def authorisation_with_testdata_newuser(self, mail, passw):
        self.find_element(Locators.AUTH_EMAIL_FIELD).send_keys(mail)
        self.find_element(Locators.AUTH_PASSWORD_FIELD).send_keys(passw)
        self.find_element(Locators.AUTH_SIGNIN_BUTTON).click()


