from selenium.webdriver.common.by import By


class KonstrLocators:
    BUTTON_KONSTRUKTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # кнопка для перехода в конструктор
    MAINPAGE_KONSTRUKTOR = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")  # заголовок который появляется при загрузкеконструктора на главной странице
    BUTTON_LENTA_ZAKAZOV = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")  # кнопка для перехода в Ленту заказов
    MAINPAGE_LENTA_ZAKAZOV = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")  # заголовок который появляется при загрузке Ленты Заказов

    BULKA_PICTURE = (By.XPATH, '//img[@alt="Краторная булка N-200i"]')  # картинка из раздела Булки
    BULKA_DETAILS = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]")

    KRESTIK = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK' and @type='button']") #крестик чтобы закрыть модальное окно

    INGR_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")
    INGR_DRAG = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    INGR_DROP = (By.XPATH, "//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']")

    TO_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")  #кнопка Сделать заказ (если авторизован)
    ORDER_PLACED = (By.XPATH, "//p[contains(text(),'идентификатор заказа')]") #модальное окно если заказ успешно размещен - есть идентификатор заказа
    # номер заказа из модального окна, возникающего после создания заказ - номер появляется не сразу, вначале 9999
    ORDER_NUMBER = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
