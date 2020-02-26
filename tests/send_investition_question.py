import unittest

from faker import Faker

from pages.investition_page import InvestitionPage
from pages.main_page import MainPage
from pages.search_page import SearchPage
from tests.base_test import BaseTest


class SendQuestionTest(BaseTest):
    """ TC.4 """
    def test_investition_question(self):
        MainPage(self.driver).click_search_button()

        SearchPage(self.driver).wait_for_page_to_load()
        SearchPage(self.driver).select_first_offer()

        InvestitionPage(self.driver).wait_for_page_to_load()
        self.assertTrue(InvestitionPage(self.driver).is_send_button_clickable())

        InvestitionPage(self.driver).input_name((Faker("pl_PL").name()))
        InvestitionPage(self.driver).input_email((Faker("en_GB").email()))
        InvestitionPage(self.driver).click_accept_rules_checkbox()
        InvestitionPage(self.driver).send_question_message()

        InvestitionPage(self.driver).send_question_message()
        self.assertFalse(InvestitionPage(self.driver).is_send_button_clickable())


if __name__ == "__main__":
    unittest.main(verbosity=2)