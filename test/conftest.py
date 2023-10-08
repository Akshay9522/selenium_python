
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utility.config import *
import pytest

@pytest.fixture()
def setup(request):
    service_obj = Service("..\\Driver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    request.cls.driver = driver
    driver.get(read_confg.read_config_file("self","application","url"))
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield
    driver.quit()


