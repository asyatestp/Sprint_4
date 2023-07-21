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
    LOCATOR_FAQ = (By.CLASS_NAME, 'Home_FAQ__3uVm4')



