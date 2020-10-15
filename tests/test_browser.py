import unittest
import argparse
import sys
from driver_util.browser import Browser
from page_objects.google_search_pom import GoogleSearchPage
from page_objects.search_results_pom import SearchResultsPage


class RunTest(unittest.TestCase):

    def setUp(self):
        self.driver = Browser().getbrowser("chrome")
        self.driver.get("https://www.google.com/")
        self.googlesearchpage = GoogleSearchPage(self.driver)
        self.searchresultspage = SearchResultsPage(self.driver)

    def testExample(self):
        self.googlesearchpage.searchfor("Selenium")
        self.searchresultspage.link_selenium_present()

    def tearDown(self):
        self.driver.quit()
