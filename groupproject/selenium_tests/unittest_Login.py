# Generated by Selenium IDE
import json
import time
import unittest

from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class unittest_TestLogin(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def test_ll(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1936, 1056)
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "id_username").send_keys("kfritts")
    time.sleep(1)
    self.driver.find_element(By.ID, "id_password").send_keys("Pepper321")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()
  

if __name__ == '__main__':
    unittest.main()
