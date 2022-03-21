from selenium.webdriver.common.by import By

from libs.base_element import BaseElement
from libs.base_page import BasePage
from libs.locators.base_locator import Locator


class TopMenu(BasePage):

    @property
    def shopping_cart_button(self):
        locator = Locator(by=By.XPATH, value="//a[@title='Shopping Cart']")
        return BaseElement(driver=self.driver, locator=locator)

    
