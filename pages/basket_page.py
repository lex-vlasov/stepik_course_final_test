from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS_SUMMARY), "Products in the basket, but they should not be."


    def should_be_empty_basket_message(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert "Your basket is empty." in empty_basket_message.text, "There is no empty basket message on the page"