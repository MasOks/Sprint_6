from pages.home_page import HomePage
from pages.order_form_page import OrderFormPage
from pages.header_logo import HeaderLogo
import allure


class TestLogoHeader:
    @allure.title('Проверка перехода на главную страницу "Самоката" по клику на логотип "Самокат"')
    def test_go_to_home_page_scooter_by_click_logo_scooter(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_cookies_button()
        home_page.click_order_button_up()
        order_form_page = OrderFormPage(driver)
        order_form_page.open_order_page()
        header_logo = HeaderLogo(driver)
        header_logo.click_logo_scooter()
        assert home_page.get_text_subheader() == home_page.SUBHEADER_TEXT

    @allure.title('Проверка перехода через редирект на главную страницу Дзена по клику на логотип "Яндекс"')
    def test_redirect_after_click_logo_yandex(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_cookies_button()
        header_logo = HeaderLogo(driver)
        header_logo.click_logo_yandex()
        assert header_logo.wait_redirect_dzen() is True
