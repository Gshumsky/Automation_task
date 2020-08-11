from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
#проверка элементов страницы логина
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

#ссылка содержит в себе слово login
    def should_be_login_url(self):
        url=self.browser.current_url
        assert "login" in url, 'Login url missing'

#есть форма логина
    def should_be_login_form(self):        
        assert self.is_element_present(*LoginPageLocators.lOGIN_FORM), 'Login form missing'

#есть форма регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form missing'

#регистрация юзера    
    def register_new_user(self, email, password):
        email_field=self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        password1=self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password2=self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT_FIELD)
        reg_button=self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_field.send_keys(email)
        password1.send_keys(password)
        password2.send_keys(password)
        reg_button.click()