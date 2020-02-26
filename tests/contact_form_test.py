import unittest

from faker import Faker

from pages.contact_page import ContactPage
from pages.main_page import MainPage
from tests.base_test import BaseTest


class ContactFormTest(BaseTest):
    """ TC.1 """
    def test_engine_search(self):
        MainPage(self.driver).click_contact_button()

        ContactPage(self.driver).wait_for_page_to_load()
        ContactPage(self.driver).click_send_button()
        self.assertTrue(ContactPage(self.driver).is_checkbox_error_present())
        self.assertTrue(ContactPage(self.driver).is_email_error_present())

        ContactPage(self.driver).enter_email(Faker("pl_PL").email())
        ContactPage(self.driver).click_checkbox()
        ContactPage(self.driver).click_send_button()
        self.assertFalse(ContactPage(self.driver).is_checkbox_error_present())
        self.assertFalse(ContactPage(self.driver).is_email_error_present())


if __name__ == "__main__":
    unittest.main(verbosity=2)