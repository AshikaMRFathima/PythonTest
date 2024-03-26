import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager


def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(8)
    driver.maximize_window()


def test_login():
    driver.get("http://staging.maqta.ae")
    title = driver.title
    print(title)
    enter_username = driver.find_element(By.ID, "Username")
    enter_username.send_keys('mscuser1')
    time.sleep(3)

    enter_password = driver.find_element(By.NAME, "Password")
    enter_password.send_keys('P@ssw0rd')

    click_login_btn = driver.find_element(By.ID, "step-btn")
    click_login_btn.click()

    click_on_menu = driver.find_element(By.ID, "burger-menu-nav")
    click_on_menu.click()

    (driver.find_element(By.XPATH, "//*[@id='mat-expansion-panel-header-5']/span[1]/mat-panel-description/span")
     .click())
    time.sleep(4)


def test_teardown():
    driver.close()
    driver.quit()
    print("Test completed")