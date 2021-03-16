from selenium.webdriver.common.by import By

from PageObjectMobel.FlightDetails import FlightDeatils


class Home:
    def __init__(self, driver):
        self.driver = driver

    round_trip = (By.ID, "roundTrip")
    from_details = (By.ID, "gosuggest_inputSrc")
    from_list = (By.XPATH, "//ul[@id='react-autosuggest-1']/li/div/div[2]/div[1]/span[1]")
    to_details = (By.ID, "gosuggest_inputDest")
    to_list = (By.XPATH, "//ul[@id='react-autosuggest-1']/li/div/div[2]/div[1]/span[1]")
    from_date = (By.ID, "fare_20210316")
    coming_date = (By.ID, "fare_20210320")
    search_button = (By.ID, "gi_search_btn")

    def get_round_trip(self):
        return self.driver.find_element(*Home.round_trip)

    def get_from_details(self,text):
        return self.driver.find_element(*Home.from_details).send_keys(text)

    def get_from_list(self):
        return self.driver.find_elements(*Home.from_list)

    def get_to_details(self, text):
        return self.driver.find_element(*Home.to_details).send_keys(text)

    def get_to_list(self):
        return self.driver.find_elements(*Home.to_list)

    def get_from_date(self):
        return self.driver.find_element(*Home.from_date)

    def get_coming_date(self):
        return self.driver.find_element(*Home.coming_date)

    def get_search_button(self):
        self.driver.find_element(*Home.search_button).click()
        Flight = FlightDeatils(self.driver)
        return Flight
