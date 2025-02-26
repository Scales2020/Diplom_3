from selenium.webdriver.common.by import By


class LentaLocators:
    ORDER_DETAILS_CHECK = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']") #модальное окно с деталями заказа, есликликнуть на плашку любого заказа в ЛЕНТЕ
    ANY_ORDER_CLICK = (By.XPATH, "//a[@class='OrderHistory_link__1iNby']") #плашка одного из заказов в списке ЛЕНТЫ ЗАКАЗОВ
    LENTA_LAST_ORDER = (By.XPATH, "//p[@class='text text_type_digits-default']") #плашка с данными о новом заказе авторизованного пользователя (в ЛК)

    BUTTON_LENTA_ZAKAZOV = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")  # кнопка для перехода в Ленту заказов
    # номер заказа из модального окна, возникающего после создания заказ - номер появляется не сразу, вначале 9999
    ORDER_NUMBER = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")


    TOTAL_COUNTER = (By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    TODAY_COUNTER = (By.XPATH, "// *[text() = 'Выполнено за сегодня:']/following-sibling::p")

    INGR_DRAG_1 = (By.XPATH, "//img[@alt='Краторная булка N-200i']")
    INGR_DRAG_2 = (By.XPATH, "//img[@alt='Биокотлета из марсианской Магнолии']")
    INGR_DROP = (By.XPATH, "//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']")
    KRESTIK_ORDER_MODAL = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK' and @type='button']")

    ORDERS_IN_PROGRESS = (By.XPATH, "//li[@class='text text_type_digits-default mb-2']")





