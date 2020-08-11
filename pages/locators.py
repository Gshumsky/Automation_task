from selenium.webdriver.common.by import By

class LoginPageLocators():
    lOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_REPEAT_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')
class ProductPageLocators():
    ADD_ITEM_BUTTON=(By.CSS_SELECTOR, '#add_to_basket_form>button')
    SUCCESS_MESSAGE=(By.CSS_SELECTOR, '#messages .alert:first-child .alertinner strong')
    CARD_PRICE=(By.CSS_SELECTOR,'.alert:last-child .alertinner strong')
    BOOK_PRICE=(By.CSS_SELECTOR,'.col-sm-6 .price_color')
    BOOK_NAME=(By.CSS_SELECTOR,'.col-sm-6.product_main h1')
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class BasketPageLocators():
    GO_TO_BASKET = (By.CSS_SELECTOR, '.btn-group>a')
    GO_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg')
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner p')