import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def Browser(request):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("start-maximized")
    driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver_win32 (1)\chromedriver.exe",options=chrome_options)
    driver.get("https://www.goibibo.com/")
    request.cls.driver = driver
    # yield
    # driver.close()