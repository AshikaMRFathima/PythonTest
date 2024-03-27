import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import PageLocators
import TestData.UserCredentials
from TestData.UserCredentials import UserData
from PageLocators.LoginPageLocator import LoginPageLocator

from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.common.exceptions import InvalidSessionIdException
from selenium.webdriver.support.wait import WebDriverWait


#file name should start with test_name.py
#pytest test_newfile.py
#python -m pytest
#py.test
#pytest -v


class TestSample(): #class name should start with capitalTest
    @pytest.fixture()
    def test_setup(self):  #self should pass argument
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(8)
        #driver.maximize_window()
        #yield  #this will call tear down method everytime

    def test_login(self,test_setup):
        driver.get("http://staging.maqta.ae")
        title = driver.title
        print(title)
        x = driver.title
        assert x == "ATLP - REG"
        enter_username = driver.find_element(By.ID, LoginPageLocator.USERNAME_ID)
        enter_username.send_keys(TestData.UserCredentials.UserData.enter_username)
        time.sleep(3)
        enter_password = driver.find_element(By.NAME, LoginPageLocator.PASSWORD_NAME)
        enter_password.send_keys(TestData.UserCredentials.UserData.enter_password)

    def test_navigate(self):
        click_login_btn = driver.find_element(By.ID, LoginPageLocator.LOGIN_BUTTON_ID)
        click_login_btn.click()
        time.sleep(3)
        click_on_menu = driver.find_element(By.ID, "burger-menu-nav")
        click_on_menu.click()
        time.sleep(3)
        (driver.find_element(By.XPATH, "//span[contains(text(),'Sea')]")
         .click())
        driver.find_element(By.XPATH," //span[normalize-space()='Vessel Operation']").click()

    def test_tear_down(self):
        driver.close()
        driver.quit()
        print("Test completed")


