import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    @allure.step('Открываем браузер Mozilla Firefox')
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Найти кликабельный элемент')
    def find_clickable_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    @allure.step('Найти элемент на странице')
    def find_visibility_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    @allure.step('Клик на элемент')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Текст элемента')
    def find_element_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Скролл до раздела "Вопросы о важном"')
    def scroll_to_element(self, locator):
        faq = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", faq)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))


    def wait_for_page_load(self, url):
        WebDriverWait(self.driver, 20).until(EC.url_to_be(url))






