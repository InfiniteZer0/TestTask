from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import re

import time


class SbisPage:

    def __init__(self, driver):
        self.driver = driver
        self.contact = (By.CLASS_NAME, 'sbisru-Header__menu-item-1')
        self.banner = (By.CLASS_NAME, 'sbisru-Contacts__logo-tensor.mb-12')

    def click_contacts(self):
        self.driver.find_element(*self.contact).click()

    def click_banner(self):
        self.driver.find_element(*self.banner).click()


class TensorPage:
    def __init__(self, driver):
        self.driver = driver
        self.banner_content = (By.CLASS_NAME, 'tensor_ru-Index__block4-content.tensor_ru-Index__card')
        self.banner_title = (By.CLASS_NAME, 'tensor_ru-Index__card-title.tensor_ru-pb-16')
        self.banner_link = (By.CLASS_NAME, 'tensor_ru-link.tensor_ru-Index__link')
        self.image_1 = (By.XPATH, '//img[@alt="Продвигаем сервисы"]')
        self.image_2 = (By.XPATH, '//img[@alt="Создаем инфраструктуру"]')
        self.image_3 = (By.XPATH, '//img[@alt="Разрабатываем систему СБИС"]')
        self.image_4 = (By.XPATH, '//img[@alt="Сопровождаем клиентов"]')

    def switch_to_window(self, index):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[index])

    def get_banner_title_text(self):
        banner = self.driver.find_element(*self.banner_content)
        banner2 = banner.find_element(*self.banner_title)
        return banner2.text

    def click_banner_link(self):
        banner = self.driver.find_element(*self.banner_content)
        actions = ActionChains(self.driver)
        actions.move_to_element(banner).perform()
        banner.find_element(*self.banner_link).click()

    def size_image(self):
        if self.driver.current_url == 'https://tensor.ru/about':
            image = self.driver.find_element(*self.image_1)
            image2 = self.driver.find_element(*self.image_2)
            image3 = self.driver.find_element(*self.image_3)
            image4 = self.driver.find_element(*self.image_4)
            return image4.size, image3.size, image2.size, image.size























