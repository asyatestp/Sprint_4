import allure
from page.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Получить ответ на часто задаваемый вопрос')
    def check_answer_on_faq(self, faq_locator, answer_locator):
        self.driver.find_element(*faq_locator).click()
        return self.driver.find_element(*answer_locator).text

