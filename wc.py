# #-*- coding:utf-8 -*-
from selenium import webdriver
import time
import unittest
from bs4 import BeautifulSoup
class wc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url =""
    def error(self):
         return 'This is Error'
    def test_wc(self):
        try:
            self.driver.get(self.url)
            self.driver.find_element_by_xpath("//input[@name='userId']").send_keys('')
            driver.find_element_by_xpath("//input[@name='password']").send_keys('')
            self.driver.page_source
        except Exception as e:
            print 'wc'
            raise  e
    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()
