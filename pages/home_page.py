import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    FAQ_1_LOCATOR = (By.XPATH, ".//div[contains(text(), 'Сколько это стоит')]")
    FAQ_2_LOCATOR = (By.XPATH, ".//div[contains(text(), 'Хочу сразу несколько самокатов')]")
    FAQ_3_LOCATOR = (By.XPATH, ".//div[contains(text(), 'Как рассчитывается время аренды')]")
    FAQ_4_LOCATOR = (By.XPATH, ".//div[contains(text(), 'заказать самокат прямо на сегодня')]")
    FAQ_5_LOCATOR = (By.XPATH, ".//div[contains(text(), 'продлить заказ')]")
    FAQ_6_LOCATOR = (By.XPATH, ".//div[contains(text(), 'Вы привозите зарядку вместе с самокатом')]")
    FAQ_7_LOCATOR = (By.XPATH, ".//div[contains(text(), 'отменить заказ')]")
    FAQ_8_LOCATOR = (By.XPATH, ".//div[contains(text(), 'за МКАДом')]")

    ANSWER_1_LOCATOR = (By.XPATH, ".//p[contains(text(), 'Оплата курьеру')]")
    ANSWER_2_LOCATOR = (By.XPATH, ".//p[contains(text(), 'один заказ')]")
    ANSWER_3_LOCATOR = (By.XPATH, ".//p[contains(text(), 'Отсчёт времени аренды')]")
    ANSWER_4_LOCATOR = (By.XPATH, ".//p[contains(text(), 'с завтрашнего дня')]")
    ANSWER_5_LOCATOR = (By.XPATH, ".//p[contains(text(), 'позвонить в поддержку')]")
    ANSWER_6_LOCATOR = (By.XPATH, ".//p[contains(text(), 'с полной зарядкой')]")
    ANSWER_7_LOCATOR = (By.XPATH, ".//p[contains(text(), 'пока самокат не привезли')]")
    ANSWER_8_LOCATOR = (By.XPATH, ".//p[contains(text(), 'Московской области')]")

    ORDER_BUTTON_UP = [By.XPATH, ".//button[@class='Button_Button__ra12g' and text()='Заказать']"]
    ORDER_BUTTON_DOWN = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"]
    COOKIES_BUTTON = [By.ID, 'rcc-confirm-button']
    IMG_SCOOTER = [By.XPATH, ".//img[@src='/assets/scooter.png']"]
    SUBHEADER = [By.XPATH, ".//div[@class='Home_SubHeader__zwi_E' and text()='Как это работает']"]

    SUBHEADER_TEXT = 'Как это работает'

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, url):
        with allure.step('Открытие главной страницы "Самоката"'):
            self.navigate(url)

    def click_faq_field(self, locator):
        with allure.step('Клик по вопросу раздела "Вопросы о важном"'):
            self.scroll_to_element(locator)
            self.wait_for_element_visible(locator)
            return self.click_element(locator)

    def get_text_answer_field(self, locator):
        with allure.step('Получение текста ответа к вопросу раздела "Вопросы о важном"'):
            return self.find_element(locator).text

    def click_cookies_button(self, locator):
        return self.click_element(locator)

    def click_order_button_up(self, locator):
        with allure.step('Клик по кнопке "Заказать" вверху страницы'):
            return self.click_element(locator)

    def click_order_button_down(self, locator):
        with allure.step('Нажатие кнопки "Заказать" внизу формы заказа'):
            self.scroll_to_element(locator)
            self.wait_for_element_visible(locator)
            return self.click_element(locator)

    def get_text_subheader(self, locator):
        with allure.step('Получение текста подзаголовка на главной странице "Самоката"'):
            self.scroll_to_element(locator)
            return self.find_element(locator).text
