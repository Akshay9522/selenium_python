from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def getUsername(self):
        return self.driver.find_element(By.NAME, "username")

    def getPassword(self):
        return self.driver.find_element(By.NAME, "password")

    def getLoginBtn(self):
        return self.driver.find_element(By.XPATH, "//button[@type='submit']")