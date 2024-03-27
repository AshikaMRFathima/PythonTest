import pytest
from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    #elif request.param == "firefox":
     #   web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    #else:
     #   web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    request.cls.driver = web_driver
    yield
    web_driver.close()
