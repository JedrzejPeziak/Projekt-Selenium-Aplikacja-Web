from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from locators import SearchPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(BasePage):
    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(SearchPageLocators.SEARCH_BUTTON))

    def enter_min_area(self, area):
        self.driver.find_element(*SearchPageLocators.AREA_FROM).send_keys(area)

    def enter_max_area(self, area):
        self.driver.find_element(*SearchPageLocators.AREA_TO).send_keys(area)

    def select_first_offer(self):
        element = self.driver.find_elements(*SearchPageLocators.FIRST_OFFER)[0]
        ActionChains(self.driver).move_to_element(element).click(element).perform()

    def click_search_button(self):
        self.driver.find_element(*SearchPageLocators.SEARCH_BUTTON).click()

    def check_all_areas(self, area_min, area_max):
        elements = self.driver.find_elements(*SearchPageLocators.ALL_INVESTMENT_AREAS)
        iteration = 0
        for element in elements:
            #Required string edit - remove any unnecessary charaters, ensure X.XX number format
            area_string = element.get_attribute("innerHTML").replace(' ', '').replace('-', '').replace(',', '.')
            arr = area_string.split("&nbsp;")
            #Three elements when area from, area to and other infromation are present - ignore other cases
            if len(arr) == 3:
                if not (float(area_min) <= float(arr[0]) and
                        float(area_max) >= float(arr[1])):
                    print("Błąd w iteracji: ", iteration)
                    print("Zakres to: ", area_min, " - ", area_max)
                    print("Odczytany zakres to: ", arr[0], " - ", arr[1])
                    return False
            iteration = iteration + 1
        return True

    def toggle_favourite_investition(self, index):
        elements = self.driver.find_elements(*SearchPageLocators.FAVOURITE_BUTTON)
        iteration = 0
        for element in elements:
            if index == iteration:
                element.click()
                break
            else:
                iteration = iteration + 1
        #Give chance for page to hide the alert
        return SearchPage(self.driver).wait_for_info_to_disappear()

    def get_number_of_favourites(self):
        return self.driver.find_element(*SearchPageLocators.NUMBER_OF_FAVOURITES).get_attribute("innerHTML")

    #Custom wait required due to varying [style] string of alert
    def wait_for_info_to_disappear(self):
        for x in range(100):
            count1 = self.driver.find_elements(*SearchPageLocators.INFO_BAR_OPACITY_1)
            count2 = self.driver.find_elements(*SearchPageLocators.INFO_BAR_OPACITY_2)
            count3 = self.driver.find_elements(*SearchPageLocators.INFO_BAR_NO_OPACITY)
            if len(count1) > 0 or len(count2) > 0 or len(count3) > 0:
                return True
            sleep(0.1)
        return False
