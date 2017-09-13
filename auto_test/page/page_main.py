#-*-coding:utf-8 -*-
from selenium.webdriver.common.by import By
from auto_test.drivers.base import BasePage
from selenium import webdriver
from auto_test.element.element_main import MainElement
import time
class MainPage(BasePage,MainElement):
    js = """var elements = document.getElementsByClassName("dl-tab-item dl-collapse");
                    for (var i=0;i<elements.length;i++)
                    {elements[i].className="dl-tab-item";}
                    """
    def all_forword_step(self):
        self.logininCase()
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)
    def input_username(self, username):
        self.find_element(*self.username_loc).clear()
        return self.find_element(*self.username_loc).send_keys(username)
    # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        self.find_element(*self.password_loc).clear()
        return self.find_element(*self.password_loc).send_keys(password)
    # 点击登录：调用send_keys对象，点击登录
    def click_submit(self):
        self.find_element(*self.submit_loc).click()
    def click_ok(self):
        self.find_element(*self.ok).click()
    def alter_property(self):
        """修改页面class属性，使隐藏菜单栏显示"""

        self.script(self.js)
    def modulename_test(self):
        """获取模块名称"""
        return self.find_element(*self.tab_name).text
    def open_module(self):
        moduleName = self.find_elements(*self.module_click)
        for m in moduleName:
            m.click()
            #
            #print type(b(m.text))
            #if self.find_element(*b(m.text)):
                #print u'TITLE与 %s 一致'%(m.text)
    def db(self):
        """预留查询数据库，匹配前后台数据一致"""
        pass
if __name__ == "__main__":
    driver = webdriver.Chrome()
    base_url = r'http://192.168.98.22:8013/sherpa-dms3/login'
    pagetitle = "Sherpa's Login"
    a = MainPage(driver, base_url, pagetitle)
    a.all_forword_step()
    a.click_ok()
    a.alter_property()
    a.open_module