#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
class MainElement(object):
    username_loc = (By.XPATH, "//input[@name='userId']")
    password_loc = (By.XPATH, "//input[@name='password']")
    submit_loc = (By.XPATH, "//button[@type='submit']")
    ok = (By.XPATH, "//button[text()='Ok']")
    class_tab = (By.XPATH, "//li[@class='dl-tab-item dl-collapse']")
    tab_name = (By.CLASS_NAME, 'dl-tab-item')
    module_click = (By.XPATH, "//li[contains(@class,'bui-menu-item menu-leaf')]")
    close_tab = (By.XPATH, "//s[@class='tab-item-close']")
    iframe = (By.XPATH, "//div[@id='J_DMS3Tab']/div[1]/div[2]/div[1]/iframe")
    title_modulename = lambda modulename:(By.XPATH, "//li[@title='%s']"%modulename)