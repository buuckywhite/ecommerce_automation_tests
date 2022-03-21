from selenium.webdriver.common.by import By

from libs.base_element import BaseElement
from libs.base_page import BasePage
from libs.locators.base_locator import Locator


class Checkout(BasePage):

    @property
    def guest_checkout_radio_button(self):
        locator = Locator(by=By.XPATH, value="//input[@value='guest']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def checkout_option_continue_button(self):
        locator = Locator(by=By.XPATH, value="//input[@id='button-account']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def firstname_input(self):
        locator = Locator(by=By.XPATH, value="//input[@id='input-payment-firstname']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def lastname_input(self):
        locator = Locator(by=By.XPATH, value="//input[@id='input-payment-lastname']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def email_input(self):
        locator = Locator(by=By.XPATH, value="//input[@id='input-payment-email']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def telephone_input(self):
        locator = Locator(by=By.XPATH, value="//input[@id='input-payment-telephone']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def company_input(self):
        locator = Locator(by=By.XPATH, value="//input[@id='input-payment-company']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def address1_input(self):
        locator = Locator(by=By.XPATH, value="//input[@id='input-payment-address-1']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def address2_input(self):
        locator = Locator(by=By.XPATH, value="//input[@id='input-payment-address-2']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def city_input(self):
        locator = Locator(by=By.XPATH, value="//input[@id='input-payment-city']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def postcode_input(self):
        locator = Locator(by=By.XPATH, value="//input[@id='input-payment-postcode']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def country_select(self):
        locator = Locator(by=By.XPATH, value="//select[@id='input-payment-country']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def country_selected_from_list(self):
        locator = Locator(by=By.XPATH, value="//select[@id='input-payment-country']//option[@value='5']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def region_select(self):
        locator = Locator(by=By.XPATH, value="//select[@id='input-payment-zone']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def region_selected_from_list(self):
        locator = Locator(by=By.XPATH, value="//select[@id='input-payment-zone']//option[@value='123']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def billing_details_continue_button(self):
        locator = Locator(by=By.XPATH, value="//input[@id='button-guest']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_comment_input(self):
        locator = Locator(by=By.XPATH, value="//textarea[@name='comment']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def agreement_checkbox(self):
        locator = Locator(by=By.XPATH, value="//input[@name='agree']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def payment_method_continue_button(self):
        locator = Locator(by=By.XPATH, value="//input[@id='button-payment-method']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def missing_payment_method_warning(self):
        locator = Locator(by=By.XPATH, value="//div[@class='alert alert-danger alert-dismissible']")
        return BaseElement(driver=self.driver, locator=locator)
