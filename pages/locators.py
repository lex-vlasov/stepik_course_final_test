from selenium.webdriver.common.by import By

class MainPageLocators():
     pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    PRODUCT_PRICE = (By.XPATH, "//*[@class='price_color']")
    PRODUCT_IN_ADD_BASKET_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    TOTAL_BASKET_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div//strong")
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket') and (@type='submit')]")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

