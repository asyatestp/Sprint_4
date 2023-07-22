import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:


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

    @allure.step('Получить текст элемента')
    def find_element_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))


    def wait_for_page_load(self, url):
        WebDriverWait(self.driver, 20).until(EC.url_to_be(url))

    @allure.step('Ввод данных')
    def input_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def new_window(self):
        new_window = self.driver.switch_to.window(self.driver.window_handles[-1])
        return

    def current_url(self):
        current_url = self.driver.current_url
        return current_url






