from selenium.webdriver.common.by import By
from PageObjectMobel.TicketsDetails import TicketPage


class FlightDeatils:

    def __init__(self, driver):
        self.driver = driver

    left_arrow = (By.XPATH, "//div[@class='fltHpyOnwrdWrp']/div/ul/li[4]/span")
    all_left_radio = (By.XPATH, "//div[@class='dF justifyBetween alignItemsEnd padTB10']/div[2]/div/span[2]/label")
    right_arrow = (By.XPATH, "//i[@class='ico13 icon-arrow2-up hpyBlueLt ']")
    all_right_radio = (By.XPATH, "//div[@data-cy='flightItem_MP#:UK841UK848#1']/div/div[2]/div[2]/div/span[2]/label")
    book_button = (By.XPATH, "//span[@class='db clearfix padTB15']/button")


    def get_left_arrow(self):
        return self.driver.find_element(*FlightDeatils.left_arrow)

    def get_all_left_radio(self):
        return self.driver.find_elements(*FlightDeatils.all_left_radio)

    def get_right_arrow(self):
        return self.driver.find_element(*FlightDeatils.right_arrow)

    def get_all_right_radio(self):
        return self.driver.find_elements(*FlightDeatils.all_right_radio)

    def get_book_button(self):
        self.driver.find_element(*FlightDeatils.book_button).click()
        Ticket = TicketPage(self.driver)
        return Ticket



