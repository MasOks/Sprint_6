from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self, url: str):
        self.driver.get(url)

    def find_element(self, locator, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            print(f'Element with locator {locator} not found within {timeout} seconds.')
            return None

    def click_element(self, locator: tuple, timeout: int = 10):
        element = self.find_element(locator, timeout)
        if element:
            element.click()
        else:
            print(f'Failed to click on element with locator {locator}.')

    def wait_for_element_visible(self, locator, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            print(f'Element with locator {locator} not visible after {timeout} seconds.')
            return None

    def scroll_to_element(self, locator: tuple, timeout: int = 10):
        element = self.find_element(locator, timeout)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return True
        except TimeoutException:
            return None

    def enter_text(self, locator: tuple, text: str, timeout: int = 10):
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print(f'Failed to enter text in element with locator {locator}.')

    def wait_url_after_redirect(self, url, timeout: int = 10):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.url_changes(url))
            return True
        except TimeoutException:
            return False
