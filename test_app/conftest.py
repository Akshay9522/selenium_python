import lib2to3.pgen2.driver

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utility.config import *
import pytest
@pytest.fixture()
def login_application(request):
    service_obj = Service("..\\Driver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get(read_confg.read_config_file("self", "application", "url"))
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.quit()
