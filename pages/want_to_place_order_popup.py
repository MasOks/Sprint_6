from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class WantToPlaceOrderPopup(BasePage):
    MODAL_WANT_TO_PLACE_ORDER = [By.XPATH, ".//div[@class='Order_Modal__YZ-d3']"]
    BUTTON_YES = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"]
    BUTTON_NO = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Нет']"]

    def __init__(self, driver):
        super().__init__(driver)

    def click_button_yes(self):
        with allure.step('Клик по кнопке "Да" всплывающего сообщения "Хотите оформить заказ?"'):
            self.click_element(self.BUTTON_YES)
