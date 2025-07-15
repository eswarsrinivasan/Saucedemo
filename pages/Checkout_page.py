from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .Add_to_cart_page import AddToCart
from .base_page import Basepage
from pages.login_page import Login
class Checkout(Basepage):
    CHECKOUT_BUTTON = (By.XPATH, "//button[@id='checkout']")
    FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME =(By.XPATH, "//input[@id='last-name']")
    POSTAL_CODE = (By.XPATH, "//input[@id='postal-code']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@id='continue']")
    CART_ITEM = (By.XPATH, "//div[@class='cart_item']")
    ITEM_NAME = (By.XPATH, ".//div[@class='inventory_item_name']")
    ITEM_PRICE = (By.XPATH, "//div[@class='summary_total_label']")
    FINISH_BUTTON = (By.XPATH, "//button[@id='finish']")

    def __init__(self, driver):
        super().__init__(driver)
        self.login = Login(driver)
        self.add_to_cart = AddToCart(driver)

    def go_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def fill_details(self, first_name, last_name, postal_code):
        self.sendkeys(self.FIRST_NAME, first_name)
        self.sendkeys(self.LAST_NAME, last_name)
        self.sendkeys(self.POSTAL_CODE, postal_code)

    def continue_button(self):
        self.click(self.CONTINUE_BUTTON)

    def check_order(self, ordered_item):
        containers = self.wait.until(EC.visibility_of_all_elements_located(self.CART_ITEM))
        for container in containers:
            name_elem = container.find_element(*self.ITEM_NAME)
            if name_elem.text.strip().lower() == ordered_item.strip().lower():
                return True
        return False

    def total_price(self):
        total_price = self.wait.until(EC.visibility_of_element_located(self.ITEM_PRICE)).text
        return total_price.replace("Total: $","")

    def click_finish(self):
        self.click(self.FINISH_BUTTON)