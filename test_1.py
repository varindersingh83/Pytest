import unittest
import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

logging.basicConfig(filename='test.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)


class HackerNewsSearchTest(unittest.TestCase):

    def setUp(self):
        # caps = {'browserName': os.getenv('BROWSER', 'chrome'),
        #         'tz': 'America/Montreal'}
        # self.browser = webdriver.Remote(
        #     command_executor='http://localhost:4444/wd/hub',
        #     desired_capabilities=caps
        # )
        self.browser = webdriver.Chrome()

    def test_hackernews_search_for_testdrivenio(self):
        start_time = time.time()
        browser = self.browser
        browser.get('https://news.ycombinator.com')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven.io')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertIn('testdriven.io', browser.page_source)
        logging.info("--- %s seconds ---" % (time.time() - start_time))

    def test_hackernews_search_for_selenium(self):
        start_time = time.time()
        browser = self.browser
        browser.get('https://news.ycombinator.com')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('selenium')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertIn('selenium', browser.page_source)
        logging.info("--- %s seconds ---" % (time.time() - start_time))

    def test_hackernews_search_for_testdriven(self):
        start_time = time.time()
        browser = self.browser
        browser.get('https://news.ycombinator.com')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertIn('testdriven', browser.page_source)
        logging.info("--- %s seconds ---" % (time.time() - start_time))

    def test_hackernews_search_with_no_results(self):
        start_time = time.time()
        browser = self.browser
        browser.get('https://news.ycombinator.com')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('?*^^%')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertNotIn('<div>', browser.page_source)
        logging.info("--- %s seconds ---" % (time.time() - start_time))

    def tearDown(self):
        self.browser.quit()  # quit vs close?


if __name__ == '__main__':
    unittest.main()
