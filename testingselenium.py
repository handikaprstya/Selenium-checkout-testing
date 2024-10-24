from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()

# driver.maximize_window()
driver.get('https://demoqa.com/alerts')

# driver.find_element(By.ID, "alertButton").click()
# time.sleep(2)
# driver.switch_to.alert.accept()
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.ID, "confirmButton")).perform()

actions.scroll_by_amount(0, 500).perform()

driver.implicitly_wait(3)

driver.find_element(By.ID, "confirmButton").click()
time.sleep(3)
driver.switch_to.alert.accept()

driver.find_element(By.ID, "promtButton").click()
driver.switch_to.alert.send_keys("Hello")
driver.switch_to.alert.accept()
time.sleep(3)