from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basepage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def sendkeys(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def gettext(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def go_to(self, url):
        self.driver.get(url)

