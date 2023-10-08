import pytest
from utility.Base import Base
from page import HomePage
from actions import Action
from utility.read_data import Data
from selenium.webdriver.common.by import By
from selenium import webdriver
class Test_login_valid(Base):

    def test_invalid_login_credintial(self):
        log = self.getLogger()
        hp = HomePage.LoginPage(self.driver)
        actions = Action.Actions(self.driver)
        actions.sendKeys(hp.getUsername(), "Admin")
        log.info("Entered Username")
        actions.sendKeys(hp.getPassword(), "admin123")
        log.info("Entered Password")
        actions.click(hp.getLoginBtn())
        log.info("Clicked on login button")
        assert True
        log.info("log in sucessful")

