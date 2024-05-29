from pages.home_page import HomePage
from pages.order_form_page import OrderFormPage
from pages.want_to_place_order_popup import WantToPlaceOrderPopup
from pages.order_placed_popup import OrderPlacedPopup
from data import get_first_set_of_data, get_second_set_of_data
import allure


class TestOrderFormPage:
    @allure.title('Позитивный сценарий заказа самоката по кнопке "Заказать" вверху главной страницы')
    def test_ordering_scooter_positive_with_first_set_of_data(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_cookies_button()
        home_page.click_order_button_up()
        order_form_page = OrderFormPage(driver)
        name, surname, address, telephone, date_delivery, comment = get_first_set_of_data()
        order_form_page.open_order_page()
        order_form_page.enter_name(name)
        order_form_page.enter_surname(surname)
        order_form_page.enter_address(address)
        order_form_page.click_metro_station()
        order_form_page.enter_metro_station_6()
        order_form_page.enter_telephone(telephone)
        order_form_page.click_button_next()
        order_form_page.second_form_is_visible()
        order_form_page.enter_data_delivery(date_delivery)
        order_form_page.click_button_rental_period()
        order_form_page.menu_rental_period_is_visible()
        order_form_page.enter_rental_period_5()
        order_form_page.click_color_scooter_grey()
        order_form_page.enter_comment(comment)
        order_form_page.click_order_button()
        order_popup_first = WantToPlaceOrderPopup(driver)
        order_popup_first.click_button_yes()
        order_popup_second = OrderPlacedPopup(driver)
        assert order_popup_second.get_text() == order_popup_second.BUTTON_STATUS_TEXT

    @allure.title('Позитивный сценарий заказа самоката по кнопке "Заказать" внизу главной страницы')
    def test_ordering_scooter_positive_with_second_set_of_data(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_cookies_button()
        home_page.click_order_button_down()
        order_form_page = OrderFormPage(driver)
        name, surname, address, telephone, date_delivery, comment = get_second_set_of_data()
        order_form_page.open_order_page()
        order_form_page.enter_name(name)
        order_form_page.enter_surname(surname)
        order_form_page.enter_address(address)
        order_form_page.click_metro_station()
        order_form_page.enter_metro_station_237()
        order_form_page.enter_telephone(telephone)
        order_form_page.click_button_next()
        order_form_page.second_form_is_visible()
        order_form_page.enter_data_delivery(date_delivery)
        order_form_page.click_button_rental_period()
        order_form_page.menu_rental_period_is_visible()
        order_form_page.enter_rental_period_2()
        order_form_page.click_color_scooter_black()
        order_form_page.enter_comment(comment)
        order_form_page.click_order_button()
        order_popup_first = WantToPlaceOrderPopup(driver)
        order_popup_first.click_button_yes()
        order_popup_second = OrderPlacedPopup(driver)
        assert order_popup_second.get_text() == order_popup_second.BUTTON_STATUS_TEXT
