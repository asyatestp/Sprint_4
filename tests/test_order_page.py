import allure
import pytest
from page.order_page import OrderPage
from locators import OrderPageLocators
from data import DataForm
from urls import Urls
import time



class TestOrder:
    @allure.title('Оформление заказа по кнопке "Заказать" в шапке страницы')
    def test_order_button_on_header(self, driver):
        order_page = OrderPage(driver)
        order_page.filling_form(DataForm.USER_FIRST_NAME, DataForm.USER_LAST_NAME, DataForm.USER_ADDRESS, DataForm.USER_PHONE)
        order_page.filling_form_rent(DataForm.DATE_TIME, DataForm.COMMENT)
        text_order = order_page.find_element_text(OrderPageLocators.ORDER_PLACED)
        assert DataForm.SUCCESSFUL_ORDER_TEXT in text_order

    @allure.title('Оформление заказа по кнопке "Заказать" на странице')
    def test_order_button_on_header(self, driver):
        order_page = OrderPage(driver)
        order_page.filling_form_button_on_the_page(DataForm.USER_FIRST_NAME, DataForm.USER_LAST_NAME, DataForm.USER_ADDRESS, DataForm.USER_PHONE)
        order_page.filling_form_rent(DataForm.DATE_TIME, DataForm.COMMENT)
        text_order = order_page.find_element_text(OrderPageLocators.ORDER_PLACED)
        assert DataForm.SUCCESSFUL_ORDER_TEXT in text_order

    @allure.title('Проверка: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_page_main(self, driver):
        order_page = OrderPage(driver)
        order_page.filling_form(DataForm.USER_FIRST_NAME, DataForm.USER_LAST_NAME, DataForm.USER_ADDRESS, DataForm.USER_PHONE)
        order_page.filling_form_rent(DataForm.DATE_TIME, DataForm.COMMENT)
        order_page.click_element(OrderPageLocators.LOCATOR_STATUS)
        order_page.click_element(OrderPageLocators.LOCATOR_MAIN)
        text_logo = order_page.find_element_text(OrderPageLocators.MAIN_LOGO)

        assert DataForm.LOGO in text_logo

    @allure.title('Проверка: если нажать на логотип Яндекса, в новом окне откроется главная страница Яндекса.')
    def test_page_main(self, driver):
        order_page = OrderPage(driver)
        order_page.find_visibility_element(OrderPageLocators.LOCATOR_MAIN)
        order_page.click_element(OrderPageLocators.LOCATOR_YANDEX)
        driver.switch_to.window(driver.window_handles[-1])
        order_page.wait_for_page_load(Urls.DZEN)

        assert driver.current_url == Urls.DZEN







