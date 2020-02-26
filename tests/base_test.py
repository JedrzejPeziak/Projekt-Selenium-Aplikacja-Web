import unittest

from selenium import webdriver

from pages.main_page import MainPage


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://dopoznania.pl/')
        self.driver.maximize_window()
        MainPage(self.driver).wait_for_page_to_load()
        MainPage(self.driver).close_cookies_info()

    def tearDown(self):
        self.driver.quit()