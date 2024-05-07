import time
from telnetlib import EC
import pytest
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from PageLocators.LoginPageLocator import LoginPageLocator
from TestData.UserCredentials import userCredentials


class TestAdminLogin():

    def test_setup(self):
        global driver
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        #driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        driver.maximize_window()

    def test_login(self):
        driver.implicitly_wait(8)
        driver.get("https://testing.zabehaty.uae.zabe7ti.website/backend/login")
        title = driver.title
        print(title)

    def test_enter_credentials(self):
        enter_username = driver.find_element(By.NAME, LoginPageLocator.USERNAME_NAME)
        enter_username.send_keys(userCredentials["username"])
        enter_password = driver.find_element(By.XPATH, LoginPageLocator.PASSWORD_XPATH)
        enter_password.send_keys(userCredentials["password"])

        click_login_btn = driver.find_element(By.XPATH, LoginPageLocator.LOGIN_BUTTON_XPATH)
        click_login_btn.click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[contains(text(),'اختار اللغة : ar')]").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='English']").click()

        ack = ActionChains(driver)
        ack.move_to_element(driver.find_element(By.XPATH, "//span[normalize-space()='The Sales']")).perform()
        print("Clicked on interaction page")
        driver.find_element(By.XPATH, "//span[normalize-space()='Orders']").click()
        time.sleep(5)

    def test_select_order(self):
        driver.find_element(By.XPATH, "//div[9]//div[1]//a[1]").click()
        driver.find_element(By.XPATH, "//a[@class='btn btn-info']").click() #create button for new order
        time.sleep(10)
        driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[2]/div[1]/div/form/div[1]/div[1]/span/span[1]/span/span[2]/b").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@role='searchbox']").send_keys("chic")
        time.sleep(3)

        # actions = ActionChains(driver)
        # actions.send_keys(keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
        # try:   #test still will pass
        #     elem = driver.find_element(By.CSS_SELECTOR, "#select2-category_id-06-container")
        #     elem.click()
        # except NoSuchElementException:
        #     pass

        selectemirates = driver.find_element(By.NAME, "emirate_id")  #emrates
        sel = Select(selectemirates)
        sel.select_by_visible_text("Abu Dhabi")
        time.sleep(5)

        selectregion = driver.find_element(By.NAME, "region_id") #region
        sel = Select(selectregion)
        sel.select_by_index(5)
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[@placeholder='Search Users...']").send_keys("mohamed fathih")
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[contains(text(),'mohamed')]").click()
        time.sleep(3)

        select_user_address = driver.find_element(By.NAME, "address_id")
        sel = Select(select_user_address)
        sel.select_by_index(1)

        select_date = driver.find_element(By.CSS_SELECTOR, "input[name='date']")
        select_date.send_keys("07/05/2024")

        select_time = driver.find_element(By.NAME, "time")
        sel = Select(select_time)
        sel.select_by_index(3)

        select_payment_method = driver.find_element(By.NAME, "payment_method")
        sel = Select(select_payment_method)
        sel.select_by_visible_text("paylink")
        time.sleep(3)

        select_shipping_method = driver.find_element(By.NAME, "shipping_method_id")
        sel = Select(select_shipping_method)
        sel.select_by_index(3)

        enter_additional_request = driver.find_element(By.CSS_SELECTOR, "input[name='notes']")
        enter_additional_request.send_keys("test order")

    def test_order_details(self):
        enter_category_details = driver.find_element(By.NAME, "OrderDetail[0][category_id]")
        sel = Select(enter_category_details)
        sel.select_by_visible_text("chicken")
        time.sleep(3)

        select_product = driver.find_element(By.NAME, "OrderDetail[0][product_id]")
        sel = Select(select_product)
        sel.select_by_visible_text("Al Danat Chicken 1000g")
        time.sleep(3)

        enter_quantity = driver.find_element(By.NAME, "OrderDetail[0][quantity]")
        enter_quantity.send_keys("1")

        submit_order = driver.find_element(By.NAME, "save")
        submit_order.click()