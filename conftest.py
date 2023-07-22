import pytest
from selenium import webdriver
from faker import Faker
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture
def fake():
    faker = Faker()
    return faker