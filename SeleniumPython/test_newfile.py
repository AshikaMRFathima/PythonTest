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
        driver.maximize_window()
        yield  #this will call tear down method everytime
        driver.close()
        driver.quit()
        print("Test completed")


    def test_login(self,test_setup):
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

        click_on_menu = driver.find_element(By.ID, "burger-menu-nav")
        click_on_menu.click()

        (driver.find_element(By.XPATH, "//*[@id='mat-expansion-panel-header-5']/span[1]/mat-panel-description/span")
         .click())
        time.sleep(4)


