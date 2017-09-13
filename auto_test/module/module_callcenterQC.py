#-*-coding:utf-8 -*-
import unittest
from auto_test.page.page_callCenter import CallcenterPage
from selenium import webdriver
import time
from auto_test.drivers.excel import Excel
from auto_test.drivers.log import Logger
mylogger = Logger(logger='CaseCallCenterQC').getlog()
class CaseCallCenterQC(unittest.TestCase):
    """Call Center Qc 模块自动化测试"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.filepath = r'E:\python_web\mail\data\data.xlsx'
        self.sheetname = 'loginDate'
        self.dict_env = Excel(self.filepath, self.sheetname).next()
        self.driver.maximize_window()
        # 用例执行体
    def test_callcenter(self):
        """登录 Call Center QC 模块，进行测试"""
        mylogger.info(u'----------********登录 Call Center QC 模块********----------')
        mylogger.info(u'已获取dict_env属性:%s'%(self.dict_env))
        for env in self.dict_env:
            mylogger.info(u'启动谷歌浏览器\n 输入URL:%s\n判断TITLE:%s' % (env['URL'], env['TITLE']))
            test = CallcenterPage(self.driver, env['URL'], env['TITLE'])
            # forwordstep封装了LOGIN操作
            mylogger.info(u'调用用户名、密码输入组件:%s、%s' % (env['USER'], env['PWD']))
            test.forwordstep(env['USER'], env['PWD'])
            mylogger.info(u'显示功能模块菜单栏')
            test.display_tab_cs()
            mylogger.info(u'打开Call Center QC 功能模块')
            test.open_module()
            mylogger.info(u'隐藏功能模块菜单栏')
            test.close_tab_cd()
            mylogger.info(u'进入Iframe，进入Inner HTML')
            test.iframs_switch()
            title = test.need_follow_order_total()
            mylogger.info(u'获取数据报表字段名称%s'%(title))
            new_html = test.html()
            data_report = test.return_datereport(new_html)
            for m in data_report:
                if u'没有匹配数据' in data_report:
                    mylogger.info(u'获取需跟进订单总量页面数据:没有匹配数据')
                    break
                else:
                    mylogger.info(u'获取需跟进订单总量页面数据:\n%s\n------------'%(m))
            dispose_data = test.dispose_order_total()
            mylogger.info(u'获取处理订单总表数据:%s'%(dispose_data))
            product_data  = test.product_manager()
            mylogger.info(u'获取PM表数据:%s' % (product_data))

    def tearDown(self):
        #self.driver.get_screenshot_as_file(r'E:\python_web\mail\png\%s.png'%(u'MAIN_TEST'))
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()