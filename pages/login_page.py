from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import Basepage



class Login(Basepage):
    Username = (By.XPATH, "//input[@id='user-name']")
    Password = (By.XPATH, "//input[@id='password']")
    Login_button = (By.XPATH, "//input[@id='login-button']")
    Error_message = (By.CSS_SELECTOR, '[data-test="error"]')

    def visit(self, url):
        self.go_to(url)

    def login(self, username, password):
        self.sendkeys(self.Username, username)
        self.sendkeys(self.Password, password)
        self.click(self.Login_button)

    def get_error_msg(self):
        self.wait.until(EC.visibility_of_element_located(self.Error_message))
        return self.gettext(self.Error_message)