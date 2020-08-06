from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        button=self.browser.find_element(*ProductPageLocators.ADD_ITEM_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        book_message_name=self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        card_price=self.browser.find_element(*ProductPageLocators.CARD_PRICE).text
        book_price=self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_name=self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_message_name==book_name, "book name doesn't match"
        assert card_price==book_price, "book price doesn't match"