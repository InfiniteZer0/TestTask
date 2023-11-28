from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import re

import time


class SbisPage:

    def __init__(self, driver):
        self.driver = driver
        self.footer = (By.CLASS_NAME, 'sbisru-Footer__container')
        self.button_footer = (By.XPATH, '//a[@href="/download?tab=ereport&innerTab=ereport25"]')
        self.button_download = (By.XPATH, '//div[@data-id="plugin"]')
        self.link = (By.XPATH, '//a[@href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')

    def search_plugin(self):
        footer = self.driver.find_element(*self.footer)
        actions = ActionChains(self.driver)
        actions.move_to_element(footer).perform()
        self.driver.find_element(*self.button_footer).click()

    def download_plugin(self):

        time.sleep(10)
        self.driver.find_element(*self.button_download).click()
        self.driver.find_element(*self.link).click()
        time.sleep(30)

        file = './sbisplugin-setup-web.exe'

        if os.path.exists(file):
            file_size = os.path.getsize(file)
            file_size_mb = file_size / (1024 * 1024)
            file_size_mb = round(file_size_mb, 2)

            size = self.driver.find_element(*self.link)
            number = re.search(r'\d+\.\d+', size.text)
            number = float(number.group())
            return file_size_mb, number







































