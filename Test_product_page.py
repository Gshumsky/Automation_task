from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest

    #переход по множеству ссылок, в одной из них баг
@pytest.mark.parametrize('links', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", 
                                               marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, links):    
    link=f'{links}'
    page=ProductPage(browser, link)
    page.open()
    page.add_to_basket()

    #Негативный тест. Отображение оповещения после добавления товара в корзину
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link='http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page=ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

    #Негативный тест. Отображение оповещения при открытии страницы
def test_guest_cant_see_success_message(browser):
    link='http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page=ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    
    #Негативный тест. Исчезновение оповещения после добавления товара
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link='http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page=ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.success_message_should_dissapear()

    #Отображение ссылки на логин на продуктовой странице
def test_guest_should_see_login_link_on_product_page(browser):
    link='http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page=ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    #переход на страницу логина с продуктовой страницы

def test_guest_can_go_to_login_page_from_product_page(browser):
    link='http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page=ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link='http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page=ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page=BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.should_be_empty_basket_message()