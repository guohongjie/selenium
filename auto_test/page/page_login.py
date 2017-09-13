#-*-coding:utf-8 -*-
from auto_test.drivers.base import BasePage
from selenium import webdriver
from auto_test.element.element_login import LoginElement
import time
class LoginPage(BasePage,LoginElement):
    #操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
    # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)
    # 输入用户名：调用send_keys对象，输入用户名
    def show_title(self, page_title):
        return self.page_title
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
    # 验证页面元素
    def show_span(self):
        list_text ={u'表单标题':self.find_element(*self.span_loc).text,
        u'页面标题':self.find_element(*self.page_title).text,
        u'提交按钮内容':self.find_element(*self.submit_loc).text}
        return  list_text
    def web_title(self):
        return self.explorer_title()
    def exec_script(self,src):
        self.script(src)
    def click_alert(self):
        self.accept_alert()

if __name__ ==  "__main__":
    driver = webdriver.Chrome()
    base_url = r'http://192.168.98.22:8013/sherpa-dms3/login'
    pagetitle = "Sherpa's Login"
    a = LoginPage(driver,base_url,pagetitle)
    a.open()
    #a.show_span()
    a.input_username('yumi')
    a.input_password('111111')
    a.click_submit()