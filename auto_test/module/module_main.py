#-*-coding:utf-8 -*-
import unittest
from auto_test.page.page_main import MainPage
from selenium import webdriver
import time
from auto_test.drivers.excel import Excel
from auto_test.drivers.log import Logger
mylogger = Logger(logger='CaseMain').getlog()
class CaseMain(unittest.TestCase):
    """主界面自动化测试"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.filepath = r'E:\python_web\mail\data\data.xlsx'
        self.sheetname = 'loginDate'
        self.dict_env = Excel(self.filepath, self.sheetname).next()
        self.driver.maximize_window()
        # 用例执行体
    def test_main(self):
        """登录主页测试：模块名称，进入各模块"""
        mylogger.info(u'----------********登录主页测试********----------')
        mylogger.info(u'已获取dict_env属性:%s'%(self.dict_env))
        for env in self.dict_env:
            mylogger.info(u'启动谷歌浏览器\n 输入URL:%s\n判断TITLE:%s'%(env['URL'], env['TITLE']))
            test = MainPage(self.driver, env['URL'], env['TITLE'])
            test.open()
            mylogger.info(u'调用用户名输入组件:%s' % (env['USER']))
            test.input_username(env['USER'])
            mylogger.info(u'调用密码输入组件:%s' % (env['PWD']))
            test.input_password(env['PWD'])
            time.sleep(1)
            mylogger.info(u'调用点击登录按钮组件,进入main界面')
            test.click_submit()
            time.sleep(1)
            mylogger.info(u'点击OK按钮，取消CALL CENTER工具提示框')
            test.click_ok()
            #显示菜单模块栏
            mylogger.info(u'显示菜单模块栏')
            test.alter_property()
            test.open_module()
            mylogger.info(u'遍历打开功能模块成功')

    def tearDown(self):
        #self.driver.get_screenshot_as_file(r'E:\python_web\mail\png\%s.png'%(u'MAIN_TEST'))
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()