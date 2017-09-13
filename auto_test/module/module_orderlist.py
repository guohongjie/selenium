#-*-coding:utf-8 -*-
import unittest
from auto_test.page.page_orderlist import OrderListPage
from selenium import webdriver
import time
from auto_test.drivers.excel import Excel
from auto_test.drivers.log import Logger
mylogger = Logger(logger='CaseOrderList').getlog()
class CaseOrderList(unittest.TestCase):
    """订单列表模块自动化测试"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.filepath = r'E:\python_web\mail\data\data.xlsx'
        self.sheetname = 'loginDate'
        self.dict_env = Excel(self.filepath, self.sheetname).next()
        self.driver.maximize_window()
        # 用例执行体
    def test_orderlist(self):
        """登录订单列表模块，进行测试"""
        mylogger.info(u'----------********登录订单列表模块********----------')
        mylogger.info(u'已获取dict_env属性:%s'%(self.dict_env))
        for env in self.dict_env:
            mylogger.info(u'启动谷歌浏览器\n 输入URL:%s\n判断TITLE:%s' % (env['URL'], env['TITLE']))
            test = OrderListPage(self.driver, env['URL'], env['TITLE'])
            # forwordstep封装了LOGIN操作
            mylogger.info(u'调用用户名、密码输入组件:%s、%s' % (env['USER'], env['PWD']))
            test.forwordstep(env['USER'], env['PWD'])
            mylogger.info(u'显示功能模块菜单栏')
            test.display_tab()
            mylogger.info(u'打开OrderList功能模块')
            test.open_module()
            mylogger.info(u'隐藏功能模块菜单栏')
            test.close_tab_cd()
            mylogger.info(u'进入Iframe，进入Inner HTML')
            test.iframs_switch()
            mylogger.info(u'选择查询起止时间段')
            test.choice_time()
            num = test.data_order()
            mylogger.info(u'查询当日订单总量%s'%(num))
            time.sleep(1)

            list_order = ['Web Order','Phone Order','App Order','Un-Approved Web Order']
            total = test.total_order()
            dict_order =dict(zip(list_order,total))
            for key,value in dict_order.items():
                mylogger.info(u'%s 订单总量：%s'%(key,value))
            mylogger.info(u'操作选择框类型，输入错误的订单号')
            test.inputOrder_query()
            mylogger.info(u'点击GO查询按钮，查询订单数据')
            test.click_go()
            mylogger.info(u'点击Query (Not Finished)按钮')
            test.query_noFinished()
            order_id = test.choice_order()
            mylogger.info(u'输入正确的订单编号:%s，并选择该订单'%(order_id))
            mylogger.info(u'点击edit&view 按钮，进行订单修改')
            test.editORview()
            mylogger.info(u'点击editAddressInfo 按钮')
            test.editAddressInfo()
            mylogger.info(u'点击修改分餐厅配置信息')
            test.change_branch_information()
            mylogger.info(u'进入餐厅营业时间变更选项')
            test.RestBusinessHoursChange()
            mylogger.info(u'餐厅营业时间变更选项操作完成，返回修改界面')
            alert_text = test.unlock_click()
            mylogger.info(u'点击解锁订单，系统提示:%s'%(alert_text[0]))
            mylogger.info(u'已点击OK 按钮，系统返回解锁返回值:%s'%(alert_text[1]))
            test.click_order_infomation()
            mylogger.info(u'点击 EDIT ORDER INFOMATION 按钮,跳转结算界面')
            test.unpayment_click()
            mylogger.info(u'点击 Unpayment 按钮,弹出 未收款金额 框，输入未收款金额：1元，点击 OK 按钮')
            test.save_order()
            mylogger.info(u'点击 SAVE 按钮')
            cannot_order = test.ifCannotOrder()
            mylogger.info(u'如果提示商家无法接单，则系统提示:%s'%cannot_order)
            parder_order = test.ifPardenOrder()
            mylogger.info(u'如果提示订单重复，则系统提示:%s'%parder_order)
            test.click_save_ok()
            mylogger.info(u'点击 OK 按钮')
            mylogger.info(u'点击 处理完成 按钮，并输入原因为：测试')
            dispose_alert = test.click_dispose()
            mylogger.info(u'点击 OK 按钮，系统提示:%s'%(dispose_alert))
            test_complete = test.send_to_restaurant()
            mylogger.info(u'关闭提示窗口，并返回订单列表主界面%s'%(test_complete))
    def tearDown(self):
        #self.driver.get_screenshot_as_file(r'E:\python_web\mail\png\%s.png'%(u'MAIN_TEST'))
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()