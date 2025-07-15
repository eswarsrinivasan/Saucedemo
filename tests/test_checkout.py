import time

import pytest
from pages.Checkout_page import Checkout
from pages.login_page import Login
from pages.Inventory_page import Inventory
from pages.Add_to_cart_page import AddToCart


@pytest.mark.parametrize("URL, Username, Password, itemlist,first_name, last_name, postal_code, total_cost",
                         [("https://www.saucedemo.com/","standard_user","secret_sauce",["Sauce Labs Backpack","Sauce Labs Fleece Jacket"],"Killua","zoldyck","787554","86.38")])
def tests_checkout(setup,URL,Username, Password, itemlist, first_name, last_name, postal_code, total_cost):
    login = Login(setup)
    login.go_to(URL)
    login.login(Username, Password)
    time.sleep(2)
    assert "/inventory.html" in setup.current_url
    cart = AddToCart(setup)
    for item in itemlist:
        cart.add_to_cart(item)
    cart.goto_cart()
    assert "/cart.html" in setup.current_url
    checkout = Checkout(setup)
    checkout.go_to_checkout()
    assert "/checkout-step-one.html" in setup.current_url
    checkout.fill_details(first_name, last_name, postal_code)
    checkout.continue_button()
    assert "/checkout-step-two.html" in setup.current_url
    # for item in itemlist:
    #     exist = checkout.check_order(item)
    #     if exist is True:
    #         pass
    assert float(checkout.total_price()) == float(total_cost)
    checkout.click_finish()
    assert "/checkout-complete.html" in setup.current_url

