import allure
from selenium.webdriver import ActionChains

from locators.functional_locators import KonstrLocators
from locators.locators_pass_log import Locators
from pages.base_page import BasePage


class LentaPage(BasePage):
    def go_to_loginpage(self):
        self.go_to_mainpage()
        self.find_element(Locators.LOGIN_BUTTON).click()

    def authorisation_with_testdata_newuser(self, mail, passw):
        self.find_element(Locators.AUTH_EMAIL_FIELD).send_keys(mail)
        self.find_element(Locators.AUTH_PASSWORD_FIELD).send_keys(passw)
        self.find_element(Locators.AUTH_SIGNIN_BUTTON).click()

    def drag_and_drop_element(self, drag_elem, drop_elem):
        drag = self.find_element(drag_elem)
        drop = self.find_element(drop_elem)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag, drop)
        actions.perform()

    @allure.step('Создаем новый заказ в конструкторе (3 ингредиента)')
    def create_new_order(self,drag_elem_1, drag_elem_2, drop_elem):
        self.drag_and_drop_element(drag_elem_1, drop_elem)
        self.drag_and_drop_element(drag_elem_2,drop_elem)
        self.find_element(KonstrLocators.TO_ORDER).click()

