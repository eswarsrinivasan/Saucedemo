import time

import pytest
from pages.Add_to_cart_page import AddToCart

@pytest.mark.parametrize("URL, username, password, itemList, itemtoremove",
                         [("https://www.saucedemo.com/","standard_user", "secret_sauce",["Sauce Labs Backpack","Sauce Labs Fleece Jacket"],"Sauce Labs Fleece Jacket")])
def tests_remove_item(setup, URL, username, password, itemList, itemtoremove):
    cart = AddToCart(setup)
    cart.go_to(URL)
    cart.login(username, password)
    time.sleep(2)
    assert "/inventory.html" in setup.current_url
    for item in itemList:
        cart.add_to_cart(item)
    cart.goto_cart()
    assert "/cart.html" in setup.current_url
    cart.remove_item(itemtoremove)

