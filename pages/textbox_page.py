from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TextBoxPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    username = (By.ID, "userName")
    email = (By.ID, "userEmail")
    current_address = (By.ID, "currentAddress")
    permanent_address = (By.ID, "permanentAddress")
    submit_btn = (By.ID, "submit")

    # Actions
    def enter_username(self, name):
        self.type(self.username, name)

    def enter_email(self, email):
        self.type(self.email, email)

    def enter_current_address(self, address):
        self.type(self.current_address, address)

    def enter_permanent_address(self, address):
        self.type(self.permanent_address, address)

    def click_submit(self):
        self.scroll_to(self.submit_btn)
        self.click(self.submit_btn)