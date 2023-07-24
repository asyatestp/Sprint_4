import allure
import pytest
from page.main_page import MainPage
from locators import MainPageLocators
from data import Answers


class TestFaq:
    @pytest.mark.parametrize('faq_locator, answer_locator, answer', [
    [MainPageLocators.FAQ_QUESTIONS_1, MainPageLocators.FAQ_ANSWER_1, Answers.answer1],
    [MainPageLocators.FAQ_QUESTIONS_2, MainPageLocators.FAQ_ANSWER_2, Answers.answer2],
    [MainPageLocators.FAQ_QUESTIONS_3, MainPageLocators.FAQ_ANSWER_3, Answers.answer3],
    [MainPageLocators.FAQ_QUESTIONS_4, MainPageLocators.FAQ_ANSWER_4, Answers.answer4],
    [MainPageLocators.FAQ_QUESTIONS_5, MainPageLocators.FAQ_ANSWER_5, Answers.answer5],
    [MainPageLocators.FAQ_QUESTIONS_6, MainPageLocators.FAQ_ANSWER_6, Answers.answer6],
    [MainPageLocators.FAQ_QUESTIONS_7, MainPageLocators.FAQ_ANSWER_7, Answers.answer7],
    [MainPageLocators.FAQ_QUESTIONS_8, MainPageLocators.FAQ_ANSWER_8, Answers.answer8]
    ])


    @allure.title('Проверка открытия ответа по клику на вопрос')
    def test_expand_faq_by_click_answer_expanded(self, driver, faq_locator, answer_locator, answer):
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.LOCATOR_FAQ)
        main_page.click_element(MainPageLocators.COOKIES_BUTTON)

        assert main_page.check_answer_on_faq(faq_locator, answer_locator) == answer

