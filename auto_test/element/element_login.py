#-*-coding:utf-8 -*-
"""定位器，通过元素属性定位元素对象"""
from selenium.webdriver.common.by import By
class LoginElement(object):
    page_title = (By.CLASS_NAME, "logo")
    span_loc = (By.XPATH, "//div[@class='content']/h3")
    username_loc = (By.XPATH, "//input[@name='userId']")
    password_loc = (By.XPATH, "//input[@name='password']")
    submit_loc = (By.XPATH, "//button[@type='submit']")