from selenium.webdriver.common.by import By


class TicketPage:

    def __init__(self,driver):
        self.driver = driver

    secure_check = (By.ID, "secure-trip")
    First_name = (By.ID, "AdultfirstName1")
    Middle_name = (By.ID, "AdultmiddleName1")
    Last_name = (By.ID, "AdultlastName1")
    Email = (By.ID, "email")
    Number = (By.ID, "mobile")
    proced_button= (By.XPATH,"//div[@class='fl width100 borderTop padLR15 padTB10']/button")

    def get_secure_check(self):
        return self.driver.find_element(*TicketPage.secure_check)

    def get_First_name(self):
        return self.driver.find_element(*TicketPage.First_name)

    def get_Middle_name(self):
        return self.driver.find_element(*TicketPage.Middle_name)

    def get_Last_name(self):
        return self.driver.find_element(*TicketPage.Last_name)

    def get_Email(self):
        return self.driver.find_element(*TicketPage.Email)

    def get_Number(self):
        return self.driver.find_element(*TicketPage.Number)

    def get_proced_button(self):
        # self.driver.find_element(*TicketPage.proced_button).click()
        # pay = Payment(self.driver)
        return self.driver.find_element(*TicketPage.proced_button)



