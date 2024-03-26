import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager


driver = webdriver.Chrome()
driver.implicitly_wait(10)

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

time.sleep(3)


click_on_menu = driver.find_element(By.ID, "burger-menu-nav")
click_on_menu.click()


(driver.find_element(By.XPATH, "//*[@id='mat-expansion-panel-header-5']/span[1]/mat-panel-description/span")
 .click())
time.sleep(4)