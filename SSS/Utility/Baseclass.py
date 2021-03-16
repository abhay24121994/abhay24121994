import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.usefixtures("Browser")
class Baseclass:
    def time_checking(self, text):
        wait = WebDriverWait(self.driver, 5)
        wait.until(ec.presence_of_element_located((By.ID, text)))
