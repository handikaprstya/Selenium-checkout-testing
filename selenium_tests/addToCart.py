from selenium import webdriver
from selenium.webdriver.common.by import By
from login_page import LoginPageLocators
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(LoginPageLocators.URL)

# Click button login
driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
time.sleep(2)

# Input username dan passsword
driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(LoginPageLocators.USERNAME)
driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(*LoginPageLocators.PASSWORD)

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

driver.quit()