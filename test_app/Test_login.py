import time

import pytest
import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utility.config import *
class Test_login :

    def testlogin_application (self,login_application):
       print("Test")
       time.sleep(2)