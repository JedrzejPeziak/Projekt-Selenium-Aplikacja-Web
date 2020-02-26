from selenium.webdriver.support.wait import WebDriverWait

from locators import ContactPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ContactPage(BasePage):
    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ContactPageLocators.SEND_BUTTON))

    def click_send_button(self):
        self.driver.find_element(*ContactPageLocators.SEND_BUTTON).click()

    def is_email_error_present(self):
        if self.driver.find_element(*ContactPageLocators.EMAIL_ERROR).get_attribute("style") == "display: none;":
            return False
        else:
            return True

    def enter_email(self, email):
        self.driver.find_element(*ContactPageLocators.EMAIL_FIELD).send_keys(email)

    def is_checkbox_error_present(self):
        if self.driver.find_element(*ContactPageLocators.CHECKBOX_ERROR).get_attribute("style") == "display: none;":
            return False
        else:
            return True

    def click_checkbox(self):
        self.driver.find_element(*ContactPageLocators.CHECKBOX).click()


