from selenium import webdriver
from selenium.webdriver.common.by import By
from login_page import LoginPageLocators
import time
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

logger.info("Starting the login and checkout tests")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(LoginPageLocators.URL)

# Click button login
driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
time.sleep(2)

# Input username dan passsword
driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(LoginPageLocators.USERNAME)
driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(LoginPageLocators.PASSWORD)

driver.find_element(*LoginPageLocators.BUTTON).click()
time.sleep(2)

assert "Log out" in driver.page_source
assert "Cart" in driver.page_source
time.sleep(10)

driver.find_element(*LoginPageLocators.SAMSUNG).click()
time.sleep(2)

driver.find_element(*LoginPageLocators.ADD_TO_CART).click()
time.sleep(2)

alert = driver.switch_to.alert
alert.accept()

driver.find_element(*LoginPageLocators.CART).click()
time.sleep(2)

assert "Samsung galaxy s6" in driver.page_source

# Place Order
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

# Form order
driver.find_element(By.ID, "name").send_keys("Testing Automation")
driver.find_element(By.ID, "country").send_keys("USA")
driver.find_element(By.ID, "city").send_keys("New York")
driver.find_element(By.ID, "card").send_keys("1234567890123456")
driver.find_element(By.ID, "month").send_keys("12")
driver.find_element(By.ID, "year").send_keys("2025")

# Purchase Click
driver.find_element(By.XPATH, "//button[text()='Purchase']").click()

time.sleep(2)

# Validation that order success
assert "Thank you for your purchase!" in driver.page_source
assert "No results found." not in driver.page_source
driver.quit()