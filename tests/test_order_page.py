import allure
from page.order_page import OrderPage
from locators import OrderPageLocators
from data import DataForm
from data import DataFormIncorrect

class TestOrder:

    @allure.title('Оформление заказа по кнопке "Заказать" в шапке страницы')
    def test_order_button_on_header(self, driver):
        order_page = OrderPage(driver)
        order_page.button_order_head()
        order_page.filling_form(DataForm.USER_FIRST_NAME, DataForm.USER_LAST_NAME, DataForm.USER_ADDRESS, DataForm.USER_PHONE)
        order_page.filling_form_rent(DataForm.DATE_TIME, DataForm.COMMENT)
        text_order = order_page.find_element_text(OrderPageLocators.ORDER_PLACED)

        assert DataForm.SUCCESSFUL_ORDER_TEXT in text_order

    @allure.title('Оформление заказа по кнопке "Заказать" на странице')
    def test_order_button_on_main(self, driver):
        order_page = OrderPage(driver)
        order_page.button_order_on_the_page()
        order_page.filling_form(DataForm.USER_FIRST_NAME, DataForm.USER_LAST_NAME, DataForm.USER_ADDRESS, DataForm.USER_PHONE)
        order_page.filling_form_rent(DataForm.DATE_TIME, DataForm.COMMENT)
        text_order = order_page.find_element_text(OrderPageLocators.ORDER_PLACED)

        assert DataForm.SUCCESSFUL_ORDER_TEXT in text_order

    @allure.title('Оформление заказа с некорректными данными')
    @allure.description('Некорректное Имя пользователя')
    def test_order_page_first_name_incorrect(self, driver):
        order_page = OrderPage(driver)
        order_page.button_order_head()
        order_page.filling_form(DataFormIncorrect.INCORRECT_FIRST_NAME, DataForm.USER_LAST_NAME, DataForm.USER_ADDRESS,DataForm.USER_PHONE)
        text_first_name = order_page.find_element_text(OrderPageLocators.INCORRECT_FIRST_NAME)

        assert text_first_name == DataFormIncorrect.TEXT_NEGATIVE_FIRST_NAME

    @allure.title('Оформление заказа с некорректными данными')
    @allure.description('Некорректная Фамиилия пользователя')
    def test_order_page_last_name_incorrect(self, driver):
        order_page = OrderPage(driver)
        order_page.button_order_head()
        order_page.filling_form(DataForm.USER_FIRST_NAME, DataFormIncorrect.INCORRECT_LAST_NAME, DataForm.USER_ADDRESS, DataForm.USER_PHONE)
        text_last_name = order_page.find_element_text(OrderPageLocators.INCORRECT_LAST_NAME)

        assert text_last_name == DataFormIncorrect.TEXT_NEGATIVE_LAST_NAME

    @allure.title('Оформление заказа с некорректными данными')
    @allure.description('Некорректный Адрес пользователя')
    def test_order_page_adress_incorrect(self, driver):
        order_page = OrderPage(driver)
        order_page.button_order_head()
        order_page.filling_form(DataForm.USER_FIRST_NAME, DataForm.USER_LAST_NAME, DataFormIncorrect.INCORRECT_ADDRESS, DataForm.USER_PHONE)
        text_adress = order_page.find_element_text(OrderPageLocators.INCORRECT_ADDRESS)

        assert text_adress == DataFormIncorrect.TEXT_NEGATIVE_ADRESS

    @allure.title('Оформление заказа с некорректными данными')
    @allure.description('Некорректный Телефон пользователя')
    def test_order_page_number_incorrect(self, driver):
        order_page = OrderPage(driver)
        order_page.button_order_head()
        order_page.filling_form(DataForm.USER_FIRST_NAME, DataForm.USER_LAST_NAME, DataForm.USER_ADDRESS, DataFormIncorrect.INCORRECT_PHONE_NUMBER)
        text_number = order_page.find_element_text(OrderPageLocators.INCORRECT_PHONE_NUMBER)

        assert text_number == DataFormIncorrect.TEXT_NEGATIVE_PHONE_NUMBER











