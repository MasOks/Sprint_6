from pages.home_page import HomePage
from pages.order_form_page import OrderFormPage
from pages.want_to_place_order_popup import WantToPlaceOrderPopup
from pages.order_placed_popup import OrderPlacedPopup
from config import URL
import allure


class TestOrderFormPage:
    @allure.title('Позитивный сценарий заказа самоката по кнопке "Заказать" вверху главной страницы')
    def test_ordering_scooter_positive_with_first_set_of_data(self, driver):
        home_page = HomePage(driver)
        home_page.open_page(URL)
        home_page.click_cookies_button(HomePage.COOKIES_BUTTON)
        home_page.click_order_button_up(HomePage.ORDER_BUTTON_UP)

        order_form_page = OrderFormPage(driver)
        order_form_page.open_page(f'{URL}order')
        order_form_page.enter_name(OrderFormPage.FIELD_INPUT_NAME, 'Василий')
        order_form_page.enter_surname(OrderFormPage.FIELD_INPUT_SURNAME, 'Тёркин')
        order_form_page.enter_address(OrderFormPage.FIELD_INPUT_ADDRESS, 'Комсомольская площадь, 2Б')
        order_form_page.click_metro_station(OrderFormPage.FIELD_INPUT_STATION)
        order_form_page.enter_metro_station(OrderFormPage.METRO_STATION_6)
        order_form_page.enter_telephone(OrderFormPage.FIELD_INPUT_TELEPHONE, '89876543210')
        order_form_page.click_button_next(OrderFormPage.BUTTON_NEXT)
        order_form_page.second_form_is_visible(OrderFormPage.HEADER_ABOUT_RENT)
        order_form_page.enter_data_delivery(OrderFormPage.FIELD_DATA_DELIVERY, '31.05.2024')
        order_form_page.click_button_rental_period(OrderFormPage.BUTTON_RENTAL_PERIOD)
        order_form_page.menu_rental_period_is_visible(OrderFormPage.MENU_RENTAL_PERIOD)
        order_form_page.enter_rental_period(OrderFormPage.RENTAL_PERIOD_5)
        order_form_page.click_color_scooter(OrderFormPage.FIELD_COLOR_GREY)
        order_form_page.enter_comment(OrderFormPage.FIELD_COMMENT, 'Не звоните, спит ребёнок')
        order_form_page.click_order_button(OrderFormPage.BUTTON_ORDER)

        order_popup_first = WantToPlaceOrderPopup(driver)
        order_popup_first.click_button_yes(WantToPlaceOrderPopup.BUTTON_YES)

        order_popup_second = OrderPlacedPopup(driver)
        assert order_popup_second.get_text() == order_popup_second.BUTTON_STATUS_TEXT

    @allure.title('Позитивный сценарий заказа самоката по кнопке "Заказать" внизу главной страницы')
    def test_ordering_scooter_positive_with_second_set_of_data(self, driver):
        home_page = HomePage(driver)
        home_page.open_page(URL)
        home_page.click_cookies_button(HomePage.COOKIES_BUTTON)
        home_page.click_order_button_down(HomePage.ORDER_BUTTON_DOWN)

        order_form_page = OrderFormPage(driver)
        order_form_page.open_page(f'{URL}order')
        order_form_page.enter_name(OrderFormPage.FIELD_INPUT_NAME, 'Раиса')
        order_form_page.enter_surname(OrderFormPage.FIELD_INPUT_SURNAME, 'Маркова')
        order_form_page.enter_address(OrderFormPage.FIELD_INPUT_ADDRESS, 'пр-д Черепановых, 72')
        order_form_page.click_metro_station(OrderFormPage.FIELD_INPUT_STATION)
        order_form_page.enter_metro_station(OrderFormPage.METRO_STATION_237)
        order_form_page.enter_telephone(OrderFormPage.FIELD_INPUT_TELEPHONE, '+79012345678')
        order_form_page.click_button_next(OrderFormPage.BUTTON_NEXT)
        order_form_page.second_form_is_visible(OrderFormPage.HEADER_ABOUT_RENT)
        order_form_page.enter_data_delivery(OrderFormPage.FIELD_DATA_DELIVERY, '30.05.2024')
        order_form_page.click_button_rental_period(OrderFormPage.BUTTON_RENTAL_PERIOD)
        order_form_page.menu_rental_period_is_visible(OrderFormPage.MENU_RENTAL_PERIOD)
        order_form_page.enter_rental_period(OrderFormPage.RENTAL_PERIOD_2)
        order_form_page.click_color_scooter(OrderFormPage.FIELD_COLOR_BLACK)
        order_form_page.enter_comment(OrderFormPage.FIELD_COMMENT, 'Звоните в любое время')
        order_form_page.click_order_button(OrderFormPage.BUTTON_ORDER)

        order_popup_first = WantToPlaceOrderPopup(driver)
        order_popup_first.click_button_yes(WantToPlaceOrderPopup.BUTTON_YES)

        order_popup_second = OrderPlacedPopup(driver)
        assert order_popup_second.get_text() == order_popup_second.BUTTON_STATUS_TEXT
