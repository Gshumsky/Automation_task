from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    #добавление в корзину с решением капчи
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

    #добавление в корзину без решения капчи
    def add_to_basket_without_alert(self):
        button=self.browser.find_element(*ProductPageLocators.ADD_ITEM_BUTTON)
        button.click()
        book_message_name=self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        card_price=self.browser.find_element(*ProductPageLocators.CARD_PRICE).text
        book_price=self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_name=self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_message_name==book_name, "book name doesn't match"
        assert card_price==book_price, "book price doesn't match"

    #уведомление об успешном добавлении не должно отображаться
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should not be'

    #уведомление об успешном добавлении должно исчезать
    def success_message_should_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message didn't dissapear"