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
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".navbar").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Database Tools").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Genre List").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Add Genre").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "id_name").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "id_name").send_keys("ABC")
    time.sleep(1)
    self.driver.find_element(By.ID, "id_description").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "id_description").send_keys("123456")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(7)").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Genre List").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "ABC").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Database Tools").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Genre List").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(2) > .btn").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "id_name").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "id_name").send_keys("QWE")
    time.sleep(1)
    self.driver.find_element(By.ID, "id_description").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "id_description").send_keys("123")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(7)").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "ABCQWE").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Database Tools").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Genre List").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(3) > .btn").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".fa-user").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  

if __name__ == '__main__':
    unittest.main()