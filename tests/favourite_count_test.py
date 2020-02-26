import unittest
from time import sleep

from faker import Faker

from pages.contact_page import ContactPage
from pages.main_page import MainPage
from pages.search_page import SearchPage
from tests.base_test import BaseTest


class ContactFormTest(BaseTest):
    """ TC.2 """
    """ Warning! Funcionality unstable - send issue to developers. """
    def test_engine_search(self):
        MainPage(self.driver).click_search_button()

        SearchPage(self.driver).wait_for_page_to_load()
        self.assertTrue(SearchPage(self.driver).toggle_favourite_investition(1))
        self.assertTrue(SearchPage(self.driver).toggle_favourite_investition(2))
        self.assertEqual(SearchPage(self.driver).get_number_of_favourites(), "2")

        self.assertTrue(SearchPage(self.driver).toggle_favourite_investition(3))
        self.assertEqual(SearchPage(self.driver).get_number_of_favourites(), "3")

        self.assertTrue(SearchPage(self.driver).toggle_favourite_investition(3))
        self.assertEqual(SearchPage(self.driver).get_number_of_favourites(), "2")


if __name__ == "__main__":
    unittest.main(verbosity=2)