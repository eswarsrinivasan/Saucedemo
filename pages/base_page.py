import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidSelectorException
from pages.ai_utility import ai_heal

class Basepage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,50)

    def click(self, locator, retries= 2):
        current_locator= locator
        attempts = 0

        while attempts <= retries:
            try:
                current_wait = self.wait if attempts == 0 else WebDriverWait(self.driver, 5)
                print(f"current locator : {current_locator}")
                current_wait.until(EC.visibility_of_element_located(current_locator)).click
                return
            except (TimeoutException, NoSuchElementException, InvalidSelectorException) as e:
                attempts+=1
                print(f"Attempts at healing : {attempts}")
                if attempts > retries:
                    print("Locator cannot be fixed by LLM")
                    raise e
            
                page_html = self.driver.page_source
                selector_type = current_locator[0]
                locator_value = current_locator[1]
                print(f"locator value: {locator_value}")
                healed_locator = ai_heal(page_html, locator_value, selector_type)

                if healed_locator:
                    print(f"healed_locator: {healed_locator}")
                    current_locator = (By.CSS_SELECTOR, healed_locator)
                    print(f"healed_current_locator: {current_locator}")
                else:
                    print("Locator cannot be fixed by LLM")
                    raise e
                time.sleep(1)



    def sendkeys(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def gettext(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def go_to(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

