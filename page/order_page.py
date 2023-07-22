import allure
from page.base_page import BasePage
from locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step('Ввод данных')
    def input_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Заполнить поля раздела "Для кого самокат?"')
    def filling_form(self, user_name, user_last_name, user_address, user_phone):
        self.click_element(OrderPageLocators.COOKIES_BUTTON)
        self.click_element(OrderPageLocators.BUTTON_ORDER_HEAD)
        self.find_visibility_element(OrderPageLocators.FORM_ORDER)
        self.input_element(OrderPageLocators.LOCATOR_NAME, user_name)
        self.input_element(OrderPageLocators.LOCATOR_LAST_NAME, user_last_name)
        self.input_element(OrderPageLocators.LOCATOR_ADDRESS, user_address)
        self.click_element(OrderPageLocators.LOCATOR_STATION)
        self.find_visibility_element(OrderPageLocators.STATION_DROPDOWN)
        self.click_element(OrderPageLocators.STATION_DROPDOWN)
        self.input_element(OrderPageLocators.LOCATOR_PHONE_NUMBER, user_phone)
        self.find_clickable_element(OrderPageLocators.NEXT_BUTTON)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить поля раздела "Про аренду"')
    def filling_form_rent(self, date_time, comment):
        self.find_visibility_element(OrderPageLocators.LOCATOR_FORM_RENT)
        self.input_element(OrderPageLocators.LOCATOR_DATE, date_time)
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        self.find_visibility_element(OrderPageLocators.LOCATOR_PERIOD)
        self.click_element(OrderPageLocators.LOCATOR_ONE_DAY)
        self.click_element(OrderPageLocators.LOCATOR_COLOUR)
        self.input_element(OrderPageLocators.LOCATOR_COMMENT, comment)
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.ENTER_ORDER)

    @allure.step('Заполнить поля раздела "Для кого самокат?"')
    def filling_form_button_on_the_page(self, user_name, user_last_name, user_address, user_phone):
        self.click_element(OrderPageLocators.COOKIES_BUTTON)
        self.scroll_to_element(OrderPageLocators.BUTTON_ORDER_ON_THE_PAGE)
        self.click_element(OrderPageLocators.BUTTON_ORDER_ON_THE_PAGE)
        self.find_visibility_element(OrderPageLocators.FORM_ORDER)
        self.input_element(OrderPageLocators.LOCATOR_NAME, user_name)
        self.input_element(OrderPageLocators.LOCATOR_LAST_NAME, user_last_name)
        self.input_element(OrderPageLocators.LOCATOR_ADDRESS, user_address)
        self.click_element(OrderPageLocators.LOCATOR_STATION)
        self.click_element(OrderPageLocators.STATION_DROPDOWN)
        self.input_element(OrderPageLocators.LOCATOR_PHONE_NUMBER, user_phone)
        self.find_clickable_element(OrderPageLocators.NEXT_BUTTON)
        self.click_element(OrderPageLocators.NEXT_BUTTON)







