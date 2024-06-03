import pytest
from pages.home_page import HomePage
import allure


class TestHomePageFAQ:
    faq_locators = [
        HomePage.FAQ_1_LOCATOR,
        HomePage.FAQ_2_LOCATOR,
        HomePage.FAQ_3_LOCATOR,
        HomePage.FAQ_4_LOCATOR,
        HomePage.FAQ_5_LOCATOR,
        HomePage.FAQ_6_LOCATOR,
        HomePage.FAQ_7_LOCATOR,
        HomePage.FAQ_8_LOCATOR
    ]

    answer_locators = [
        HomePage.ANSWER_1_LOCATOR,
        HomePage.ANSWER_2_LOCATOR,
        HomePage.ANSWER_3_LOCATOR,
        HomePage.ANSWER_4_LOCATOR,
        HomePage.ANSWER_5_LOCATOR,
        HomePage.ANSWER_6_LOCATOR,
        HomePage.ANSWER_7_LOCATOR,
        HomePage.ANSWER_8_LOCATOR
    ]

    answers_text = [
        'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
        'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать '
        'несколько заказов — один за другим.',
        'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды '
        'начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная '
        'аренда закончится 9 мая в 20:30.',
        'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
        'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
        'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без '
        'передышек и во сне. Зарядка не понадобится.',
        'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
        'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    ]

    @allure.title('Проверка соответствующего текста в выпадающем списке раздела "Вопросы о важном"')
    @pytest.mark.parametrize('faq_locator, answer_locator, answer_text',
                             zip(faq_locators, answer_locators, answers_text))
    def test_correct_answer_to_question(self, driver, faq_locator, answer_locator, answer_text):
        home_page_faq = HomePage(driver)
        home_page_faq.open_home_page()
        home_page_faq.click_cookies_button()
        home_page_faq.click_faq_field(faq_locator)
        home_page_faq.get_text_answer_field(answer_locator)
        assert home_page_faq.get_text_answer_field(answer_locator) == answer_text
