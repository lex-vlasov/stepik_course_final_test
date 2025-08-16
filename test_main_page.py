from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем страницу
    page.go_to_login_page()             # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_products_in_basket()
    page.should_be_empty_basket_message()





#Login page separate tests

# def test_login_page_url_is_correct(browser):
#     link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_url()
#
#
# def test_login_form_is_shown_on_login_page(browser):
#     link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_form()
#
#
# def test_register_form_is_shown_on_login_page(browser):
#     link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_register_form()