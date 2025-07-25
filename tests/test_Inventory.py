import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import Login
from pages.Inventory_page import Inventory

@pytest.mark.parametrize("username, password, product", [("standard_user", "secret_sauce","Sauce Labs Backpack")])
def tests_Add_to_cart(setup, username, password, product):
    login_obj = Login(setup)
    login_obj.go_to("https://www.saucedemo.com/")
    login_obj.login(username,password)
    assert "/inventory.html" in setup.current_url
    item = Inventory(setup)

    assert item.InventoryUrl == item.get_current_url()
    item.add_to_cart(product)

@pytest.mark.parametrize("username, password, product", [("standard_user", "secret_sauce","Sauce Labs Fleece Jacket")])
def tests_remove_from_cart(setup, username, password, product):
    login = Login(setup)
    login.go_to("https://www.saucedemo.com/")
    login.login(username, password)
    assert "/inventory.html" in setup.current_url
    item = Inventory(setup)
    assert item.InventoryUrl == item.get_current_url()
    item.add_to_cart(product)
    item.remove_from_cart(product)

