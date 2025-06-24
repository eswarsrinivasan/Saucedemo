from os import remove

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import Basepage

class Inventory(Basepage):
    Product_Container = (By.XPATH, "//div[@class='inventory_item']")
    Product_Name_Locator = (By.XPATH, "//div[@class='inventory_item_name ']")
    Add_to_cart_button = (By.XPATH, ".//button[text()='Add to cart']")
    Remove_button = (By.XPATH, ".//button[text()='Remove']")

    def find_product(self, product_name)  -> WebElement | None:
        all_products = self.wait.until(EC.visibility_of_all_elements_located(self.Product_Container))
        for product in all_products:
            try:
                product_name_element = self.wait.until(EC.visibility_of_element_located(product, *self.Product_Name_Locator))
                if product_name_element.text == product_name:
                    return product
            except:
                continue
        return None

    def add_to_cart(self, product_name):
        product_container = self.find_product(product_name)

        if product_container:
            add = self.wait.until(EC.element_to_be_clickable(product_container,*self.Add_to_cart_button))
            add.click()
        else:
            raise ValueError("Product not found to add")

    def remove_from_cart(self, product_name):
        product_container = self.find_product(product_name)

        if product_container:
            remove_button = self.wait.until(EC.element_to_be_clickable(product_container,*self.Remove_button))
            remove_button.click()
        else:
            raise ValueError("Product not found to add")