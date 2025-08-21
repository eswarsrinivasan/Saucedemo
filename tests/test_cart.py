import time

import pytest
from pages.cart_page import AddToCart

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
    cart.checkout()
    assert "/checkout-step-one.html" in setup.current_url

@pytest.mark.parametrize("URL, username, password, itemList, Totalcost",
                         [("https://www.saucedemo.com/", "standard_user", "secret_sauce",["Sauce Labs Backpack","Sauce Labs Fleece Jacket"],"79.98")])
def tests_items_in_cart(setup, URL, username, password, itemList, Totalcost ):
    cart = AddToCart(setup)
    cart.go_to(URL)
    cart.login(username, password)
    assert "/inventory.html" in setup.current_url
    for item in itemList:
        cart.add_to_cart(item)
    cart.goto_cart()
    assert "/cart.html" in setup.current_url
    Totalprice = 0
    for item in itemList:
        item_cost = cart.get_price(item)
        Totalprice += float(item_cost)
    assert Totalprice == float(Totalcost)


