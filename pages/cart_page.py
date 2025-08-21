from selenium.webdriver.common.by import By
from pages.Inventory_page import Inventory
from selenium.webdriver.support import expected_conditions as EC


class AddToCart(Inventory):
    Add_to_cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")
    item_name = (By.XPATH, "//div[@class ='inventory_item_name']")
    cart_item = (By.XPATH, "//div[@class ='cart_item']")
    Remove = (By.XPATH, "//button[text()='Remove']")
    Checkout = (By.XPATH, "//button[text()='Checkout']")
    URL = "https://www.saucedemo.com/cart.html"
    Price = (By.XPATH, ".//div[@class ='inventory_item_price']")

    def goto_cart(self):
        self.click(self.Add_to_cart_icon)

    def check_list(self, itemname):
        containers = self.driver.find_elements(By.XPATH, "//div[@class='cart_item']")
        for container in containers:
            name_elem = container.find_element(By.CLASS_NAME, "inventory_item_name")
            if name_elem.text.strip().lower() == itemname.strip().lower():
                return container
        return None

    def remove_item(self, item):
        item_locator = self.check_list(item)
        if item_locator:
            removebtn = item_locator.find_element(*self.Remove)
            removebtn.click()
        else:
            raise ValueError("Product not present in cart")

    def get_price(self, item):
        item_locator = self.check_list(item)
        if item_locator:
            price_elem = item_locator.find_element(*self.Price)
            return price_elem.text.strip().replace("$","")
        return None

    def checkout(self):
        self.click(self.Checkout)