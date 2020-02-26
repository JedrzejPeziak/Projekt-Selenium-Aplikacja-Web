import unittest

from pages.main_page import MainPage
from pages.search_page import SearchPage
from tests.base_test import BaseTest


class SearchEngineTest(BaseTest):
    """ TC.3 """
    """ Warning! - Functionality is not working as expected - report to developers. """
    def test_engine_search(self):
        area_min = 20
        area_max = 100

        MainPage(self.driver).click_search_button()

        SearchPage(self.driver).wait_for_page_to_load()
        SearchPage(self.driver).enter_min_area(area_min)
        SearchPage(self.driver).enter_max_area(area_max)
        SearchPage(self.driver).click_search_button()

        SearchPage(self.driver).wait_for_page_to_load()
        self.assertTrue(SearchPage(self.driver).check_all_areas(area_min, area_max))


if __name__ == "__main__":
    unittest.main(verbosity=2)