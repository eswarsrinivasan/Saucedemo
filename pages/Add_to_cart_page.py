from selenium.webdriver.common.by import By
from pages.Inventory_page import Inventory
from selenium.webdriver.support import expected_conditions as EC


class AddToCart(Inventory):
    Add_to_cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")
    Cart_item = (By.XPATH, "//div[@class ='inventory_item_name']")
    Remove = (By.XPATH, "//button[text()='Remove']")
    Checkout = (By.XPATH, "//button[text()='Checkout']")
    URL = "https://www.saucedemo.com/cart.html"

    def goto_cart(self):
        self.click(self.Add_to_cart_icon)

    def check_list(self, itemname):
        items = self.wait.until(EC.visibility_of_all_elements_located(self.Cart_item))
        for item in items:
            if item.text == itemname:
                return item
        return None

    def remove_item(self, item):
        item_locator = self.check_list(item)
        if item_locator:
            removebtn = item_locator.find_element(*self.Remove)
            removebtn.click()
        else:
            raise ValueError("Product not present in cart")

    def checkout(self):
        self.click(self.Checkout)