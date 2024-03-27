import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager

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
        yield  #this will call tear down method everytime
        driver.close()
        #driver.quit()
        print("Test completed")


    def test_login(self,test_setup):
        driver.get("http://staging.maqta.ae")
        title = driver.title
        print(title)
        x = driver.title
        assert x == "ATLP - REG"

        enter_username = driver.find_element(By.ID, "Username")
        enter_username.send_keys('mskuser1')
        time.sleep(3)

        enter_password = driver.find_element(By.NAME, "Password")
        enter_password.send_keys('hOmM$26@8&2!M^T')

    def test_navigate(self):
        click_login_btn = driver.find_element(By.ID, "step-btn")
        click_login_btn.click()
        time.sleep(5)

        click_on_menu = driver.find_element(By.ID, "burger-menu-nav")
        click_on_menu.click()
        time.sleep(5)

        (driver.find_element(By.XPATH, "//span[contains(text(),'Sea')]")
         .click())
        time.sleep(4)

        driver.find_element(By.XPATH," //span[normalize-space()='Vessel Operation']").click()


