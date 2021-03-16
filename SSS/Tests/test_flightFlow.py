import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from PageObjectMobel.Home import Home
from Utility.Baseclass import Baseclass


@pytest.mark.usefixtures("Browser")
class TestFlightFlow(Baseclass):

    def test_home(self):

        Homepage = Home(self.driver)
        Homepage.get_round_trip().click()
        Homepage.get_from_details("del")

        wait = WebDriverWait(self.driver, 5)
        wait.until(ec.presence_of_element_located((By.ID, "react-autosuggest-1")))
        fromlist = Homepage.get_from_list()
        for i in fromlist:
            if i.text == "Delhi, India":
                i.click()
                break

        Homepage.get_to_details("mum")

        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located((By.ID, "react-autosuggest-1")))

        tolist = Homepage.get_to_list()
        for j in tolist:
            if j.text == "Mumbai, India":
                j.click()
                break

        Homepage.get_from_date().click()
        Homepage.get_coming_date().click()
        Flight = Homepage.get_search_button()

        time.sleep(3)
        Flight.get_left_arrow().click()
        time.sleep(3)
        alldata = Flight.get_all_left_radio()
        alldata[0].click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//i[@class='ico13 icon-arrow2-up hpyBlueLt ']")))
        Flight.get_right_arrow().click()
        time.sleep(3)
        al = Flight.get_all_right_radio()
        al[0].click()
        Ticket = Flight.get_book_button()
        time.sleep(3)
        Ticket.get_secure_check().click()

        adult = Select(self.driver.find_element_by_id("Adulttitle1"))
        adult.select_by_visible_text("Mr")

        Ticket.get_First_name().send_keys("abhay")
        Ticket.get_Middle_name().send_keys("kumar")
        Ticket.get_Last_name().send_keys("kushwaha")
        Ticket.get_Email().send_keys("abhay@gmail.com")
        Ticket.get_Number().send_keys("9856325698")
        Ticket.get_proced_button().click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='dF padT20']/button").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='posRel']/div[15]/ul[5]/li").click()
        time.sleep(5)
        self.driver.find_element_by_class("ico16 quicks f700").click()