#-*-coding:utf-8 -*-
from selenium.webdriver.common.by import By
from auto_test.drivers.base import BasePage
from selenium import webdriver
from auto_test.element.element_callCenter import CallcenterElement
import time
from bs4 import BeautifulSoup
import re
class CallcenterPage(BasePage,CallcenterElement):
    def forwordstep(self,user,passwd):
        #封装登录操作
        self.logininCase(user,passwd)
    def open_module(self):
        self.find_element(*self.module_name).click()
    def display_tab_cs(self):
        self.script(self.js)
    def close_tab_cd(self):
        #关闭菜单页，进行模块操作
        self.script(self.hidden_js)
    def iframs_switch(self):
        #进入模块内嵌HTML
        s = self.find_element(*self.iframe)
        self.switch_frame(s)
        time.sleep(2)
    def need_follow_order_total(self):
        self.find_element(*self.btn_follow).click()#需跟进订单总量
        elements = self.find_elements(*self.title_follow)
        self.title = []
        for m in elements:
            self.title.append(m.text)
        time.sleep(30)
        return self.title
    def return_datereport(self,innerhtml):
        """抓取需跟进订单总量"""
        elements = self.find_elements(*self.no_data_display)
        if elements:
            return elements[0].text
        else:
            temp_list, result = [], []
            soup = BeautifulSoup(innerhtml, 'html.parser')
            tr_html = soup.find_all('tr', attrs={'class': re.compile('bui-grid-row bui-grid-row-[a-z]+')})
            for m in range(len(tr_html)):
                new_html1 = """<html><body>%s</body></html>""" % tr_html[m]
                soup1 = BeautifulSoup(new_html1, 'html.parser')
                w = [content for content in soup1.stripped_strings]
                temp_list.append(w)
            for list_date in temp_list:
                result.append(dict(zip(self.title,list_date)))
            return result
    def dispose_order_total(self):
        self.find_element(*self.btn_response).click()
        time.sleep(3)
        self.find_element(*self.btn_go_response).click()
        time.sleep(30)
        elements = self.find_elements(*self.no_data_display)
        if elements:
             return elements[0].text
        else:
            return u'页面存在数据，待以后进行抓取'
    def product_manager(self):
        self.find_element(*self.btn_complaint).click()
        time.sleep(3)
        self.find_element(*self.btn_go).click()
        time.sleep(30)
        elements = self.find_elements(*self.no_data_display)
        if elements:
            return elements[0].text
        else:
            return u'页面存在数据，待以后进行抓取'
    def html(self):
        return self.return_html()
if __name__ == "__main__":
    driver = webdriver.Chrome()
    base_url = r'http://192.168.98.22:8013/sherpa-dms3/login'
    pagetitle = "Sherpa's Login"
    a = CallcenterPage(driver, base_url, pagetitle)
    a.forwordstep('yumi', '111111')
    a.display_tab_cs()
    a.open_module()
    a.close_tab_cd()
    a.iframs_switch()
    title = a.need_follow_order_total()
    new_html = a.html()
    print a.return_datereport(new_html)
    print a.dispose_order_total()
    print a.product_manager()

