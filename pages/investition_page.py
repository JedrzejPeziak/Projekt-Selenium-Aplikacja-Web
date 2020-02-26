import re

from selenium.webdriver.support.wait import WebDriverWait

from locators import InvestitionPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class InvestitionPage(BasePage):
    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(InvestitionPageLocators.SHOW_NUMBER_BUTTON))

    def get_telephone_number_count(self):
        number = self.driver.find_element(*InvestitionPageLocators.TELEPHONE_NUMBER).get_attribute("innerHTML")
        clean_number = re.sub(r'\<(.*?)\>', '', number) #Remove any < /> markings (and its inside data)
        clean_number = re.sub('[^0-9]','', clean_number) #Remove any non number characters
        return len(clean_number)

    def is_send_button_clickable(self):
        if self.driver.find_element(*InvestitionPageLocators.SEND_BUTTON).get_attribute("disabled") == "true":
            return False
        else:
            return True

    def click_show_number_button(self):
        self.driver.find_element(*InvestitionPageLocators.SHOW_NUMBER_BUTTON).click()

    def click_accept_rules_checkbox(self):
        self.driver.find_element(*InvestitionPageLocators.ACCEPT_CHECKBOX).click()

    def send_question_message(self):
        self.driver.find_element(*InvestitionPageLocators.SEND_BUTTON).click()

    def input_name(self, name):
        self.driver.find_element(*InvestitionPageLocators.NAME_INPUT).send_keys(name)

    def input_email(self, email):
        self.driver.find_element(*InvestitionPageLocators.EMAIL_INPUT).send_keys(email)

    def await_email_sent(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(InvestitionPageLocators.SUCCESS_EMAIL_SENT))