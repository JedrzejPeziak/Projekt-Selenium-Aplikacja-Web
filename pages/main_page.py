from selenium.webdriver.support.wait import WebDriverWait

from locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.SEARCH_BUTTON))

    def click_search_button(self):
        self.driver.find_element(*MainPageLocators.SEARCH_BUTTON).click()

    def close_cookies_info(self):
        self.driver.find_element(*MainPageLocators.CLOSE_COOKIES_BUTTON).click()

    def click_contact_button(self):
        self.driver.find_elements(*MainPageLocators.CONTACT_BUTTON)[1].click()