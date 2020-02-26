import unittest

from pages.investition_page import InvestitionPage
from pages.main_page import MainPage
from pages.search_page import SearchPage
from tests.base_test import BaseTest


class ShowNumberTest(BaseTest):
    """ TC.5 """
    def test_show_number(self):
        MainPage(self.driver).click_search_button()

        SearchPage(self.driver).wait_for_page_to_load()
        SearchPage(self.driver).select_first_offer()

        InvestitionPage(self.driver).wait_for_page_to_load()
        self.assertNotEqual(InvestitionPage(self.driver).get_telephone_number_count(), 9)

        InvestitionPage(self.driver).click_show_number_button()
        self.assertEqual(InvestitionPage(self.driver).get_telephone_number_count(), 9)


if __name__ == "__main__":
    unittest.main(verbosity=2)