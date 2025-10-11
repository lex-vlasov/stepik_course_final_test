from .base_page import BasePage
from .locators import LoginPageLocators
#from .main_page import MainPage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This is not Login page based on URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not present on this page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register Form is not present on this page"


    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION_PASSWORD)
        password_field.send_keys(password)
        password_field_2 = self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION_PASSWORD_2)
        password_field_2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()



