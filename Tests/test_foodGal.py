import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
import string
import random


class TestSelenium():
    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(8)
        #driver.maximize_window()
        #yield
        #driver.close()
        #driver.quit()

    def test_login(self):
        driver.get("https://royalfoodgallery.com")
        title = driver.title
        print(title)
        #x = driver.title
        #assert x == "AdminLTE 3|Dashboard"
        enter_username = driver.find_element(By.ID, "email")
        enter_username.send_keys('ashikamrf71@gmail.com')
        time.sleep(3)
        enter_password = driver.find_element(By.ID, "password")
        enter_password.send_keys('123')
        click_login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        click_login_btn.click()

    def test_navigates_to_main_category(self):
        click_Category_menu = driver.find_element(By.XPATH, "//p[contains(text(),'Categories &')]")
        click_Category_menu.click()
        click_subCategory = driver.find_element(By.XPATH,"//p[normalize-space()='Categories']")
        click_subCategory.click()
        # time.sleep(5)

    #def test_id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
       # assert ''.join(random.choice(chars) for _ in range(size))

    def test_select_new_category(self):
        add_new_category = driver.find_element(By.XPATH, "//a[@class='btn btn-success']")
        add_new_category.click()
        time.sleep(3)

        add_category_name = driver.find_element(By.ID, 'name')
        add_category_name.send_keys(self.test_id_generator())
        #print(self.test_id_generator())
        time.sleep(3)

        click_submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        click_submit_btn.click()
        time.sleep(3)


    #def test_teardown(self):
        #driver.close()
        #driver.quit()
