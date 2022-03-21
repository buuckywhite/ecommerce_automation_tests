from selenium.webdriver.common.by import By

from libs.base_element import BaseElement
from libs.base_page import BasePage
from libs.locators.base_locator import Locator


class Homepage(BasePage):

    @property
    def add_to_cart_button(self):
        locator = Locator(by=By.XPATH, value="//div[@class='button-group']//span[@class='hidden-xs hidden-sm hidden-md']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def featured_product_name(self):
        locator = Locator(by=By.XPATH, value="//div[@class='product-layout col-lg-3 col-md-3 col-sm-6 col-xs-12']//div[@class='caption']//a")
        return BaseElement(driver=self.driver, locator=locator)
