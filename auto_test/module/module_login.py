#-*-coding:utf-8 -*-
import unittest
from auto_test.page.page_login import LoginPage
from selenium import webdriver
import time
from auto_test.drivers.excel import Excel
from auto_test.drivers.log import Logger
mylogger = Logger(logger='CaseLogin').getlog()
class CaseLogin(unittest.TestCase):
    """登录自动化测试"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.login_content = ["SHERPA'S DMS","Login to your account","Login"]
        self.filepath = r'E:\python_web\mail\data\data.xlsx'
        self.sheetname = 'loginDate'
        self.dict_env = Excel(self.filepath, self.sheetname).next()
        self.driver.maximize_window()
    # 用例执行体
    def test_login(self):
        """测试登录界面"""
        mylogger.info(u'----------********测试登录界面********----------')
        mylogger.info(u'已获取dict_env元素,并进行遍历：%s'%(self.dict_env))
        for env in self.dict_env:
        # 声明LoginPage类对象
            mylogger.info(u'打开登录窗口\n%s\n%s'%(env['URL'], env['TITLE']))
            login_page = LoginPage(self.driver, env['URL'], env['TITLE'])
            # 调用打开页面组件
            mylogger.info(u'调用打开页面组件')
            login_page.open()
            #验证页面元素
            mylogger.info(u'验证页面元素')
            self.assertEqual(login_page.web_title(), env['TITLE'],msg='%s and %s is unlike'%(login_page.web_title(), env['TITLE']))
            self.assertEqual(login_page.show_span()[u'页面标题'],self.login_content[0],msg='%s and %s is unlike'%(login_page.show_span()[u'页面标题'],self.login_content[0]))
            self.assertEqual(login_page.show_span()[u'表单标题'],self.login_content[1],msg='%s and %s is unlike'%(login_page.show_span()[u'页面标题'],self.login_content[1]))
            self.assertEqual(login_page.show_span()[u'提交按钮内容'],self.login_content[2],msg='%s and %s is unlike'%(login_page.show_span()[u'页面标题'],self.login_content[2]))
            #空密码提交验证
            mylogger.info(u'空密码提交验证')
            login_page.click_submit()
            time.sleep(1)
            login_page.accept_alert()
            time.sleep(2)
            # 调用用户名输入组件，输入错误用户
            mylogger.info(u'调用用户名输入组件，输入错误用户:%s'%('test_error'))
            login_page.input_username('test_error')
            # 调用密码输入组件，输入错误用户密码
            mylogger.info(u'调用密码输入组件，输入错误用户密码:%s'%('test_error'))
            login_page.input_password('test_error')
            # 调用点击登录按钮组件
            mylogger.info(u'调用点击登录按钮组件')
            login_page.click_submit()
            time.sleep(1)
            login_page.accept_alert()
            time.sleep(1)
            #调用用户名输入组件
            mylogger.info(u'调用用户名输入组件:%s'%(env['USER']))
            login_page.input_username(env['USER'])
            # 调用密码输入组件
            mylogger.info(u'调用密码输入组件:%s'%(env['PWD']))
            login_page.input_password(env['PWD'])
            # 调用点击登录按钮组件
            mylogger.info(u'调用点击登录按钮组件,进入main界面')
            login_page.click_submit()
            time.sleep(2)
            js = "alert('test pass')"
            login_page.exec_script(js)
            time.sleep(1)
            login_page.click_alert()
            time.sleep(3)
            mylogger.info(u'登录模块测试完毕')

    def tearDown(self):
        #self.driver.get_screenshot_as_file(r'E:\python_web\mail\png\%s.png'%(u'LOGIN'))
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()