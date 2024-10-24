from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.ID, "login2")
    USERNAME_INPUT = (By.ID, "loginusername")
    USERNAME = "edinson"
    PASSWORD = "B@ndung12"
    PASSWORD_INPUT = (By.ID, "loginpassword")
    BUTTON = (By.XPATH, "//button[text()='Log in']")
    URL = "https://www.demoblaze.com/index.html"
    SAMSUNG = (By.LINK_TEXT, "Samsung galaxy s6")
    ADD_TO_CART = (By.XPATH, "//a[text()='Add to cart']")
    CART = (By.XPATH, "//a[text()='Cart']")
