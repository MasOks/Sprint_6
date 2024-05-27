from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class HeaderLogo(BasePage):
    LOGO_SCOOTER = [By.XPATH, ".//img[@src='/assets/scooter.svg']"]
    LOGO_YANDEX = [By.XPATH, ".//img[@src='/assets/ya.svg']"]

    def __init__(self, driver):
        super().__init__(driver)

    def click_logo_scooter(self, locator):
        with allure.step('Клик по логотипу "Самокат"'):
            self.click_element(locator)

    def click_logo_yandex(self, locator):
        with allure.step('Клик по логотипу "Яндекс"'):
            self.click_element(locator)

    def wait_redirect_dzen(self):
        with allure.step('Осуществление редиректа'):
            self.wait_url_after_redirect('https://dzen.ru/?yredirect=true')
