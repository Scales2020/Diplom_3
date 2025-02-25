from selenium.webdriver.common.by import By


class LentaLocators:
    ORDER_DETAILS_CHECK = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
    ANY_ORDER_CLICK = (By.XPATH, "//a[@class='OrderHistory_link__1iNby']")
    LENTA_LAST_ORDER = (By.XPATH, "//p[@class='text text_type_digits-default']")
