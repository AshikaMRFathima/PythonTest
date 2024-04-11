import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager

class TestSelenium():
    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(8)
        driver.maximize_window()
        #yield
        #driver.close()
        #driver.quit()

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

        time.sleep(5)

        click_on_menu = driver.find_element(By.ID, "burger-menu-nav")
        click_on_menu.click()
        time.sleep(5)

        driver.find_element(By.XPATH, "//*[@id='mat-expansion-panel-header-5']/span[1]/mat-panel-description/span").click()
        time.sleep(4)

    def test_teardown(self):
        driver.close()
        driver.quit()
