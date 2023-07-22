import allure
from page.base_page import BasePage
from data import DataForm
from locators import BasePageLocators
from urls import Urls

@allure.title('Проверка: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
def test_page_main(driver):
    base_page = BasePage(driver)
    base_page.click_element(BasePageLocators.BUTTON_ORDER_HEAD)
    base_page.find_visibility_element(BasePageLocators.FORM_ORDER)
    base_page.click_element(BasePageLocators.LOCATOR_MAIN)
    text_logo = base_page.find_element_text(BasePageLocators.MAIN_LOGO)

    assert DataForm.LOGO in text_logo


@allure.title('Проверка: если нажать на логотип Яндекса, в новом окне откроется главная страница Яндекса.')
def test_page_yandex(driver):
    base_page = BasePage(driver)
    base_page.find_visibility_element(BasePageLocators.LOCATOR_MAIN)
    base_page.click_element(BasePageLocators.LOCATOR_YANDEX)
    base_page.new_window()
    base_page.wait_for_page_load(Urls.DZEN)

    assert base_page.current_url() == Urls.DZEN