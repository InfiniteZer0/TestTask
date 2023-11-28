import pytest
from selenium import webdriver



@pytest.fixture(scope='function')
def browser():

    driver = webdriver.Chrome()

    driver.implicitly_wait(15)

    yield driver

    driver.quit()




