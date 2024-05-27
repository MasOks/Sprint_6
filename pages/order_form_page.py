from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class OrderFormPage(BasePage):
    FIELD_INPUT_NAME = [By.XPATH, ".//input[@placeholder='* Имя']"]
    FIELD_INPUT_SURNAME = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    FIELD_INPUT_ADDRESS = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    FIELD_INPUT_STATION = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    METRO_STATION_6 = [By.XPATH, ".//li[@data-value='6']"]
    METRO_STATION_237 = [By.XPATH, ".//li[@data-value='237']"]
    FIELD_INPUT_TELEPHONE = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    BUTTON_NEXT = [By.XPATH, ".//button[text()='Далее']"]

    HEADER_ABOUT_RENT = [By.XPATH, ".//div[@class='Order_Header__BZXOb' and text()='Про аренду']"]
    FIELD_DATA_DELIVERY = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    BUTTON_RENTAL_PERIOD = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    MENU_RENTAL_PERIOD = [By.XPATH, ".//div[@class='Dropdown-menu']"]
    RENTAL_PERIOD_2 = [By.XPATH, ".//div[text()='двое суток']"]
    RENTAL_PERIOD_5 = [By.XPATH, ".//div[text()='пятеро суток']"]
    FIELD_COLOR_BLACK = [By.ID, "black"]
    FIELD_COLOR_GREY = [By.ID, "grey"]
    FIELD_COMMENT = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]
    BUTTON_ORDER = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"]

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, url):
        with allure.step('Открытие формы заказа "Для кого самокат"'):
            self.navigate(url)

    def enter_name(self, locator, text):
        with allure.step('Заполнение поля "Имя"'):
            self.enter_text(locator, text)

    def enter_surname(self, locator, text):
        with allure.step('Заполнение поля "Фамилия"'):
            self.enter_text(locator, text)

    def enter_address(self, locator, text):
        with allure.step('Заполнение поля "Адрес"'):
            self.enter_text(locator, text)

    def click_metro_station(self, locator):
        with allure.step('Заполнение поля "Станция метро"'):
            self.click_element(locator)

    def enter_metro_station(self, locator):
        self.scroll_to_element(locator)
        return self.click_element(locator)

    def enter_telephone(self, locator, text):
        with allure.step('Заполнение поля "Телефон"'):
            self.enter_text(locator, text)

    def click_button_next(self, locator):
        with allure.step('Нажатие кнопки "Далее"'):
            self.wait_for_element_visible(locator)
            return self.click_element(locator)

    def second_form_is_visible(self, locator):
        with allure.step('Ожидание отображения формы заказа "Про аренду"'):
            return self.wait_for_element_visible(locator)

    def enter_data_delivery(self, locator, text):
        with allure.step('Заполнение поля "Когда привезти самокат"'):
            self.enter_text(locator, text)

    def click_button_rental_period(self, locator):
        with allure.step('Заполнение поля "Срок аренды"'):
            self.click_element(locator)

    def menu_rental_period_is_visible(self, locator):
        return self.wait_for_element_visible(locator)

    def enter_rental_period(self, locator):
        self.scroll_to_element(locator)
        return self.click_element(locator)

    def click_color_scooter(self, locator):
        with allure.step('Заполнение поля "Цвет самоката"'):
            self.click_element(locator)

    def enter_comment(self, locator, text):
        with allure.step('Заполнение поля "Комментарий для курьера"'):
            self.enter_text(locator, text)

    def click_order_button(self, locator):
        with allure.step('Нажатие кнопки "Заказать" внизу формы заказа'):
            self.scroll_to_element(locator)
            return self.click_element(locator)
