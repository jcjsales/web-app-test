from datetime import datetime
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class PageActions:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_and_click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )
        self.driver.find_element(By.XPATH, locator).click()

    def wait_for_textfield_and_input_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )
        self.driver.find_element(By.XPATH, locator).send_keys(text)

    def wait_for_element_to_be_visible(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )

    def capture_page_screenshot(self, screenshot_name):
        now = datetime.now()
        formatted_date = now.strftime("%d%m%H%M%S")
        self.driver.save_screenshot(screenshot_name + "-" + formatted_date + ".png")