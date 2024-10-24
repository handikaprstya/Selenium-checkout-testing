from selenium import webdriver
from login_page import LoginPageLocators
from selenium.webdriver.common.by import By
import time
import logging

# Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

logger.info("Starting the login test")

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(LoginPageLocators.URL)

# Click button login
driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
time.sleep(2)

# Input username dan passsword
driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(LoginPageLocators.USERNAME)
driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(LoginPageLocators.PASSWORD)

driver.find_element(*LoginPageLocators.BUTTON).click()
time.sleep(3)

assert "Log out" in driver.page_source
assert "Cart" in driver.page_source
time.sleep(10)

