from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import URL3
import allure


class HeaderLogo(BasePage):
    LOGO_SCOOTER = [By.XPATH, ".//img[@src='/assets/scooter.svg']"]
    LOGO_YANDEX = [By.XPATH, ".//img[@src='/assets/ya.svg']"]

    def __init__(self, driver):
        super().__init__(driver)

    def click_logo_scooter(self):
        with allure.step('Клик по логотипу "Самокат"'):
            self.click_element(self.LOGO_SCOOTER)

    def click_logo_yandex(self):
        with allure.step('Клик по логотипу "Яндекс"'):
            self.click_element(self.LOGO_YANDEX)

    def wait_redirect_dzen(self):
        with allure.step('Осуществление редиректа'):
            self.wait_changed_url_after_redirect(URL3)
            return True
