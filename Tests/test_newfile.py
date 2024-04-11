import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import PageLocators
import TestData.UserCredentials
from TestData.UserCredentials import UserData
from PageLocators.LoginPageLocator import LoginPageLocator
from selenium.webdriver.common.selenium_manager import SeleniumManager


# file name should start with test_name.py
# pytest test_newfile.py
# python -m pytest
# py.test
# pytest -v
class TestSample():  # class name should start with capitalTest
    def test_setup(self):  # self should pass argument
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(8)
        # driver.maximize_window()
        # yield  #this will call tear down method ever

    def test_login(self):
        driver.get("http://staging.maqta.ae")
        title = driver.title
        print(title)
        x = driver.title
        assert x == "ATLP - REG"
        enter_username = driver.find_element(By.ID, "Username")
        enter_username.send_keys('mscuser1')
        time.sleep(3)
        enter_password = driver.find_element(By.NAME, "Password")
        enter_password.send_keys('P@ssw0rd')
        click_login_btn = driver.find_element(By.ID, "step-btn")
        click_login_btn.click()

    def test_navigate_sea(self):
        click_on_menu = driver.find_element(By.ID, "burger-menu-nav")
        click_on_menu.click()
        time.sleep(3)
        (driver.find_element(By.XPATH, "//span[contains(text(),'Sea')]")
         .click()), time.sleep(3)
        driver.find_element(By.XPATH, " //span[normalize-space()='Vessel Operation']").click()
        time.sleep(4)

    def test_visit_voyage_page(self):
        driver.find_element(By.XPATH, "//button[@id='customMenu']").click()
        driver.find_element(By.XPATH, "//button[@id='btnCreate']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Select Request Type']").click(),time.sleep(3)
        print("test completed")
        driver.find_element(By.XPATH,"//span[normalize-space()='Container Release Order']").click()

    def test_tear_down(self):
        driver.close()
        driver.quit()
        print("Test completed")
