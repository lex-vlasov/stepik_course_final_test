from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()


    def should_check_add_product(self):
        self.should_match_product_name()
        self.should_match_price()


    def should_match_product_name(self):
        original_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        added_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_ADD_BASKET_MESSAGE)
        assert original_product_name.text == added_product_name.text, f"Product name {original_product_name.text} != what was added in basket {added_product_name.text}"

    def should_match_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        total_basket_price = self.browser.find_element(*ProductPageLocators.TOTAL_BASKET_PRICE)
        assert product_price.text == total_basket_price.text, f"Total basket price {total_basket_price} != product price that was added in basket {product_price.text}"
