from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    #есть текст о пустой корзине
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), 'empty basket text is missing'

    #в корзине отсутствуют товары
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.GO_TO_CHECKOUT_BUTTON), 'page contains chekout button'
