from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from config import URL2


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

    def open_order_page(self):
        with allure.step('Открытие формы заказа "Для кого самокат"'):
            self.navigate(URL2)

    def enter_name(self, text):
        with allure.step('Заполнение поля "Имя"'):
            self.enter_text(self.FIELD_INPUT_NAME, text)

    def enter_surname(self, text):
        with allure.step('Заполнение поля "Фамилия"'):
            self.enter_text(self.FIELD_INPUT_SURNAME, text)

    def enter_address(self, text):
        with allure.step('Заполнение поля "Адрес"'):
            self.enter_text(self.FIELD_INPUT_ADDRESS, text)

    def click_metro_station(self):
        with allure.step('Заполнение поля "Станция метро"'):
            self.click_element(self.FIELD_INPUT_STATION)

    def enter_metro_station_6(self):
        self.scroll_to_element(self.METRO_STATION_6)
        return self.click_element(self.METRO_STATION_6)

    def enter_metro_station_237(self):
        self.scroll_to_element(self.METRO_STATION_237)
        return self.click_element(self.METRO_STATION_237)

    def enter_telephone(self, text):
        with allure.step('Заполнение поля "Телефон"'):
            self.enter_text(self.FIELD_INPUT_TELEPHONE, text)

    def click_button_next(self):
        with allure.step('Нажатие кнопки "Далее"'):
            self.wait_for_element_visible(self.BUTTON_NEXT)
            return self.click_element(self.BUTTON_NEXT)

    def second_form_is_visible(self):
        with allure.step('Ожидание отображения формы заказа "Про аренду"'):
            return self.wait_for_element_visible(self.HEADER_ABOUT_RENT)

    def enter_data_delivery(self, text):
        with allure.step('Заполнение поля "Когда привезти самокат"'):
            self.enter_text(self.FIELD_DATA_DELIVERY, text)

    def click_button_rental_period(self):
        with allure.step('Заполнение поля "Срок аренды"'):
            self.click_element(self.BUTTON_RENTAL_PERIOD)

    def menu_rental_period_is_visible(self):
        return self.wait_for_element_visible(self.MENU_RENTAL_PERIOD)

    def enter_rental_period_2(self):
        self.scroll_to_element(self.RENTAL_PERIOD_2)
        return self.click_element(self.RENTAL_PERIOD_2)

    def enter_rental_period_5(self):
        self.scroll_to_element(self.RENTAL_PERIOD_5)
        return self.click_element(self.RENTAL_PERIOD_5)

    def click_color_scooter_black(self):
        with allure.step('Заполнение поля "Цвет самоката"'):
            self.click_element(self.FIELD_COLOR_BLACK)

    def click_color_scooter_grey(self):
        with allure.step('Заполнение поля "Цвет самоката"'):
            self.click_element(self.FIELD_COLOR_GREY)

    def enter_comment(self, text):
        with allure.step('Заполнение поля "Комментарий для курьера"'):
            self.enter_text(self.FIELD_COMMENT, text)

    def click_order_button(self):
        with allure.step('Нажатие кнопки "Заказать" внизу формы заказа'):
            self.scroll_to_element(self.BUTTON_ORDER)
            return self.click_element(self.BUTTON_ORDER)
