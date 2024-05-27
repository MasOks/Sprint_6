from pages.home_page import HomePage
from pages.order_form_page import OrderFormPage
from pages.header_logo import HeaderLogo
from config import URL
import allure


class TestLogoHeader:
    @allure.title('Проверка перехода на главную страницу "Самоката" по клику на логотип "Самокат"')
    def test_go_to_home_page_scooter_by_click_logo_scooter(self, driver):
        home_page = HomePage(driver)
        home_page.open_page(URL)
        home_page.click_cookies_button(HomePage.COOKIES_BUTTON)
        home_page.click_order_button_up(HomePage.ORDER_BUTTON_UP)

        order_form_page = OrderFormPage(driver)
        order_form_page.open_page(f'{URL}order')

        header_logo = HeaderLogo(driver)
        header_logo.click_logo_scooter(HeaderLogo.LOGO_SCOOTER)
        assert home_page.get_text_subheader(HomePage.SUBHEADER) == home_page.SUBHEADER_TEXT

    @allure.title('Проверка перехода через редирект на главную страницу Дзена по клику на логотип "Яндекс"')
    def test_go_to_home_page_dzen_by_click_logo_yandex(self, driver):
        home_page = HomePage(driver)
        home_page.open_page(URL)
        home_page.click_cookies_button(HomePage.COOKIES_BUTTON)

        header_logo = HeaderLogo(driver)
        header_logo.click_logo_yandex(HeaderLogo.LOGO_YANDEX)
        header_logo.wait_redirect_dzen()
        assert True
