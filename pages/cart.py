from selenium.webdriver.common.by import By

from libs.base_element import BaseElement
from libs.base_page import BasePage
from libs.locators.base_locator import Locator


class Cart(BasePage):

    @property
    def product_name_in_cart(self):
        locator = Locator(by=By.XPATH, value="//div[@class='col-sm-12']//td[@class='text-left']//a")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def checkout_button(self):
        locator = Locator(by=By.XPATH, value="//div[@class='buttons clearfix']//a[@class='btn btn-primary']")
        return BaseElement(driver=self.driver, locator=locator)
