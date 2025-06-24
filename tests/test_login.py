import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login

test_data = [
        ("standard_user", "secret_sauce", "/inventory.html", None),
        ("locked_out_user", "secret_sauce", None, "Epic sadface: Sorry, this user has been locked out."),
        ("invalid_user", "secret_sauce", None, "Epic sadface: Username and password do not match any user in this service"),
        ("standard_user", "wrong_password", None, "Epic sadface: Username and password do not match any user in this service"),
        ("", "secret_sauce", None, "Epic sadface: Username is required"),
        ("standard_user", "", None, "Epic sadface: Password is required"),
        ("", "", None, "Epic sadface: Username is required")
    ]


@pytest.mark.parametrize("username, password, expected_url, error_msg", test_data)
def tests_invalid_credentials(setup, username, password, expected_url, error_msg):
    login = Login(setup)
    login.go_to("https://www.saucedemo.com/")
    login.login(username,password)
    if expected_url :
        WebDriverWait(setup, 10).until(EC.url_contains(expected_url))
        assert expected_url in setup.current_url
    elif error_msg:
        error_text = login.get_error_msg()
        assert error_text == error_msg
    else:
        pytest.fail("Testdata is wrong")

