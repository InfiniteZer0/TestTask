from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import re

import time


class SbisPage:

    def __init__(self, driver):
        self.driver = driver
        self.contact = (By.CLASS_NAME, 'sbisru-Header__menu-item-1')
        self.region = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text.sbis_ru-link')
        self.city = (By.ID, 'city-id-2')
        self.region41 = (By.XPATH, '//span[@title="Камчатский край"]')

    def click_contacts(self):
        self.driver.find_element(*self.contact).click()
        time.sleep(10)

    def verify_city(self):
        region = self.driver.find_element(*self.region)
        city = self.driver.find_element(*self.city)
        return region.text, city.text

    def change_and_verify_new_region(self):
        self.driver.find_element(*self.region).click()
        self.driver.find_element(*self.region41).click()
        region = self.driver.find_element(*self.region)
        city = self.driver.find_element(*self.city)
        time.sleep(10)
        title = self.driver.title
        url = self.driver.current_url
        return region.text, city.text, title, url


























