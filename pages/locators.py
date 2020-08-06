from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    lOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
class ProductPageLocators():
    ADD_ITEM_BUTTON=(By.CSS_SELECTOR, '#add_to_basket_form>button')
    SUCCESS_MESSAGE=(By.CSS_SELECTOR, '#messages .alert:first-child .alertinner strong')
    CARD_PRICE=(By.CSS_SELECTOR,'.alert:last-child .alertinner strong')
    BOOK_PRICE=(By.CSS_SELECTOR,'.col-sm-6 .price_color')
    BOOK_NAME=(By.CSS_SELECTOR,'.col-sm-6.product_main h1')