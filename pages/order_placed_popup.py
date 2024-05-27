from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class OrderPlacedPopup(BasePage):
    MODAL_ORDER_PLACED = [By.XPATH, ".//div[@class='Order_Modal__YZ-d3']"]
    BUTTON_STATUS = [By.XPATH,
                     ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']"]

    BUTTON_STATUS_TEXT = 'Посмотреть статус'

    def __init__(self, driver):
        super().__init__(driver)

    def get_text(self):
        with allure.step('Взять текст кнопки всплывающего окна "Заказ оформлен" для проверки'):
            return self.find_element(self.BUTTON_STATUS).text

