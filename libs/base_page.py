from selenium import webdriver


class BasePage(object):
    base_URL = "https://opencart.abstracta.us/"

    def __init__(self, driver: webdriver):
        self.driver = driver
