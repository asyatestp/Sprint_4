import allure
from page.base_page import BasePage
from locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    @allure.step('Скролл до раздела "Вопросы о важном"')
    def scroll_to_faq(self):
        faq = self.driver.find_element(*MainPageLocators.LOCATOR_FAQ)
        self.driver.execute_script("arguments[0].scrollIntoView();", faq)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.LOCATOR_FAQ))

    @allure.step('Нажать и принять все куки')
    def click_cookie_button(self):
        self.driver.find_element(*MainPageLocators.COOKIES_BUTTON).click()


    @allure.step('Получить ответ на часто задаваемый вопрос')
    def check_answer_on_faq(self, faq_locator, answer_locator):
        self.driver.find_element(*faq_locator).click()
        return self.driver.find_element(*answer_locator).text

