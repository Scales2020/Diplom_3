from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]") #переходс гл страницы по кнопке "Личный кабинет"
    PASSWORD_BUT = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    PASSWORD_FORM = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")
    PASS_RECOV_EMAIL_FIELD = (By.XPATH,'//input[@class="text input__textfield text_type_main-default"]') #поле ввода емейла
    PASS_RECOV_EMAIL_ENTER_BUT = (By.XPATH, "//button[contains(text(),'Восстановить')]") #кнопка "восстановить" для подтверждения емейла
    PASS_RECOV_PASSWORD_CHECK = (By.XPATH, "//label[contains(text(),'Пароль')]")
    PASS_RECOV_PASSWORD_ENTRY = (By.XPATH, '//input[@class="text input__textfield text_type_main-default" and @name="Введите новый пароль"]')
    PASS_RECOV_PASSWORD_FIELD_EYE = (By.XPATH, "//div[@class='input__icon input__icon-action']")

    LOGIN_PAGE_CHECK = (By.XPATH, "//h2[contains(text(),'Вход')]") #заголовок для страницы логина
    AUTH_EMAIL_FIELD = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    AUTH_PASSWORD_FIELD = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    AUTH_SIGNIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")  # Кнопка "Войти" после ввода почты и пароля для входа в ЛК
    HISTORY_OF_ORDERS_MENU = (By.XPATH, "//a[contains(text(),'История заказов')]")
    HISTORY_OF_ORDERS_LIST = (By.XPATH, "//p[@class='text text_type_main-default text_color_inactive')]")
    #HISTORY_OF_ORDERS_LIST = (By.CLASS_NAME, "//h2[@class='text text_type_main-medium mb-2']")
    AUTH_SIGNOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]") #кнопка для выходаиз учетной записи из меню в ЛК



