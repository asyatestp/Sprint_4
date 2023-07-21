import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import Urls

class BasePage:

    @allure.step('Открываем браузер Mozilla Firefox')
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Найти кликабельный элемент')
    def find_clickable_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    @allure.step('Найти элемент')
    def find_visibility_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Not find {locator}')


