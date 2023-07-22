from faker import Faker
import random
import datetime

class Answers:

    ''' Ответы на вопросы '''

    answer1 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    answer2 = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    answer3 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    answer4 = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    answer5 = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    answer6 = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    answer7 = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    answer8 = "Да, обязательно. Всем самокатов! И Москве, и Московской области."


class DataForm:

    ''' Форма заказа '''

    fake = Faker(locale="ru_RU")
    USER_FIRST_NAME = fake.first_name()
    USER_LAST_NAME = fake.last_name()
    USER_ADDRESS = 'Москва'  #fake.address()
    USER_PHONE = random.randint(79000000000, 79999999999)
    DATE_TIME = datetime.date.today().strftime('%d.%m.%Y')
    COMMENT = 'ТЕСТ'


    ''' Логотип в шапке '''

    SUCCESSFUL_ORDER_TEXT = 'Заказ оформлен'
    LOGO = 'Самокат'

class DataFormIncorrect:

    INCORRECT_FIRST_NAME = 'Test'
    INCORRECT_LAST_NAME = 'Test'
    INCORRECT_ADDRESS = 'Test'
    INCORRECT_PHONE_NUMBER = '1234'

    TEXT_NEGATIVE_FIRST_NAME = 'Введите корректное имя'
    TEXT_NEGATIVE_LAST_NAME = 'Введите корректную фамилию'
    TEXT_NEGATIVE_ADRESS = 'Введите корректный адрес'
    TEXT_NEGATIVE_PHONE_NUMBER = 'Введите корректный номер'






