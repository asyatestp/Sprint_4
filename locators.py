from selenium.webdriver.common.by import By

class MainPageLocators:

    ''' Локаторы "Вопросы о важном" '''

    FAQ_QUESTIONS_1 = (By.XPATH, ".//div[@id='accordion__heading-0']")
    FAQ_QUESTIONS_2 = (By.XPATH, ".//div[@id='accordion__heading-1']")
    FAQ_QUESTIONS_3 = (By.XPATH, ".//div[@id='accordion__heading-2']")
    FAQ_QUESTIONS_4 = (By.XPATH, ".//div[@id='accordion__heading-3']")
    FAQ_QUESTIONS_5 = (By.XPATH, ".//div[@id='accordion__heading-4']")
    FAQ_QUESTIONS_6 = (By.XPATH, ".//div[@id='accordion__heading-5']")
    FAQ_QUESTIONS_7 = (By.XPATH, ".//div[@id='accordion__heading-6']")
    FAQ_QUESTIONS_8 = (By.XPATH, ".//div[@id='accordion__heading-7']")

    ''' Локаторы ответы на вопросы '''

    FAQ_ANSWER_1 = (By.ID, "accordion__panel-0")
    FAQ_ANSWER_2 = (By.ID, "accordion__panel-1")
    FAQ_ANSWER_3 = (By.ID, "accordion__panel-2")
    FAQ_ANSWER_4 = (By.ID, "accordion__panel-3")
    FAQ_ANSWER_5 = (By.ID, "accordion__panel-4")
    FAQ_ANSWER_6 = (By.ID, "accordion__panel-5")
    FAQ_ANSWER_7 = (By.ID, "accordion__panel-6")
    FAQ_ANSWER_8 = (By.ID, "accordion__panel-7")


    COOKIES_BUTTON = (By.ID, 'rcc-confirm-button') # Кнопка "да все привыкли"
    LOCATOR_FAQ = (By.CLASS_NAME, 'Home_FAQ__3uVm4') # Список вопросов

class OrderPageLocators:

    BUTTON_ORDER_HEAD = (By.XPATH,".//div[@class = 'Header_Nav__AGCXC']/button[text()='Заказать']") # Кнопка "Заказать" наверху старницы
    FORM_ORDER = (By.XPATH, ".//div[text()='Для кого самокат']") # Форма заказ
    COOKIES_BUTTON = (By.ID, 'rcc-confirm-button')  # Кнопка "да все привыкли"
    BUTTON_ORDER_ON_THE_PAGE = (By.XPATH, "//div[@class = 'Home_FinishButton__1_cWm']/button[text()='Заказать']") # Кнопка "Заказать" на главной странице

    '''Локаторы Ошибки заполнения формы'''

    INCORRECT_FIRST_NAME = [By.XPATH, ".//input[contains(@placeholder,'Имя')]/parent::div/div"]  # Текст ошибки неправильного имени
    INCORRECT_LAST_NAME = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]/parent::div/div"]  # Текст ошибки неправильной фамилии
    INCORRECT_ADDRESS = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]/parent::div/div"]  # Текст ошибки адреса
    INCORRECT_PHONE_NUMBER = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]/parent::div/div"]  # Текст ошибки номера телефона

    ''' Локаторы формы "Для кого самокат?" '''

    LOCATOR_NAME = (By.XPATH, "//input[@placeholder='* Имя']")  # Поле ввода имени
    LOCATOR_LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")  # Поле ввода фамилии
    LOCATOR_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # Поле ввода адреса
    LOCATOR_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")  # Поле выбора метро
    STATION_DROPDOWN = (By.XPATH, "//div[contains(@class, 'select-search__select')]/ul/li")  # Список метро
    LOCATOR_PHONE_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # Поле ввода номера
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")  # Кнопка "Далее"

    ''' Локаторы формы "Про аренду" '''

    LOCATOR_FORM_RENT = (By.CLASS_NAME, 'Order_Header__BZXOb')
    LOCATOR_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # Поле ввода даты
    RENTAL_PERIOD = (By.XPATH, "//div[@class = 'Dropdown-arrow-wrapper']/span[@class = 'Dropdown-arrow']") # Поле срока аренды
    LOCATOR_PERIOD = (By.XPATH, "//div[@class='Dropdown-menu']") # Аренда
    LOCATOR_ONE_DAY = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='сутки')]")  # День
    LOCATOR_COLOUR = (By.ID, 'black') # Цвет самоката
    LOCATOR_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")  # Поле ввода коммента
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']") # Кнопка "Заказать"
    ENTER_ORDER = (By.XPATH, "//button[text() = 'Да']")
    ORDER_PLACED = (By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']")
    LOCATOR_STATUS = (By.XPATH, "//div[@class = 'Order_NextButton__1_rCA']/button[text()='Посмотреть статус']")

    ''' Локаторы "Самокат" и "Яндекс "'''

    LOCATOR_MAIN = (By.XPATH, "//img[@alt='Scooter']")
    MAIN_LOGO = (By.XPATH, "//div[@class = 'Home_Header__iJKdX']")
    LOCATOR_YANDEX = (By.XPATH, "//img[@alt='Yandex']")
    LOGO_DZEN = (By.XPATH, ".//a[@class = 'dzen-header-desktop__logoContainer-1Y']")










