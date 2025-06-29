import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    chrome_options = Options()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        # Potentially more aggressive:
        # Disable Safe Browse (this is a big hammer, use with caution and ONLY for testing)
        "safeBrowse.enabled": False,
        "safeBrowse.in_safe_list_enabled": False,
        "safeBrowse.in_malware_list_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Add command-line arguments to potentially suppress security warnings
    chrome_options.add_argument("--disable-features=PasswordManagerRedesign") # Newer Chrome UI
    chrome_options.add_argument("--disable-save-password-bubble") # Might target this specific bubble
    chrome_options.add_argument("--no-default-browser-check") # Sometimes helps with initial prompts
    chrome_options.add_argument("--disable-site-navigation-jingle") # Related to security warnings

    # Other common arguments (keep if needed)
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()