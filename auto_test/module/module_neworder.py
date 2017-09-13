#-*-coding:utf-8 -*-
import unittest
from auto_test.page.page_neworder import NewOrderPage
from selenium import webdriver
from auto_test.drivers.excel import Excel
import time
from auto_test.drivers.log import Logger
mylogger = Logger(logger='CaseOrder').getlog()
class CaseOrder(unittest.TestCase):
    """新订单模块自动化测试"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.filepath =r'E:\python_web\mail\data\data.xlsx'
        self.sheetname = 'loginDate'
        self.neworder = 'newOrder'
        self.dict_env = Excel(self.filepath,self.sheetname).next()
        self.dict_newrder = Excel(self.filepath,self.neworder).next()
    def test_new_order(self):
        """新订单模块下单测试"""
        mylogger.info(u'----------********新订单模块下单测试********----------')
        mylogger.info(u'已获取dict_env属性:%s' % (self.dict_env))
        for env in self.dict_env:
            mylogger.info(u'启动谷歌浏览器\n 输入URL:%s\n判断TITLE:%s'%(env['URL'], env['TITLE']))
            test = NewOrderPage(self.driver, env['URL'], env['TITLE'])
            # forwordstep封装了LOGIN操作
            mylogger.info(u'调用用户名、密码输入组件:%s、%s' % (env['USER'], env['PWD']))
            test.forwordstep(env['USER'], env['PWD'])
            mylogger.info(u'已获取dict_newrder属性:%s'%(self.dict_newrder))
            for user_csr in self.dict_newrder:
                mylogger.info(u'执行JS显示菜单功能栏')
                test.display_tab_cs()
                mylogger.info(u'打开新订单功能模块')
                test.open_module()#打开功能模块
                mylogger.info(u'执行JS隐藏菜单功能栏')
                test.close_tab_cd()#隐藏模块菜单栏
                mylogger.info(u'进入新订单模块，切入iframe内')
                test.iframs_switch()#进入模块页
                mylogger.info(u'输入订单业务用户电话:%s'%(user_csr['TelPhone_Num']))
                test.soso_name(user_csr['TelPhone_Num'])#输入用户信息
                mylogger.info(u'点击搜索按钮，如果之前输入的电话不存在，则输入新电话%s'%(user_csr['TelPhone_new']))
                test.click_sosuo_button(user_csr['TelPhone_new'])#点击搜索按钮
                unpay_text = test.ifUnpay()
                mylogger.info(u'验证用户是否存在未收款项:--- %s'%(unpay_text))
                mylogger.info(u'输入餐厅名称:%s'%(user_csr['Rest_name']))
                test.restaurant_search(user_csr['Rest_name'])#输入餐厅信息
                mylogger.info(u'选择餐厅，展开餐厅分组')
                test.restaurant_choice(user_csr['Rest_name'])#选择餐厅
                mylogger.info(u'选择餐厅分店:%s,并点击ORDER 按钮'%(user_csr['Branch']))
                test.click_rest_order(user_csr['Branch'])#选择分店，并下单
                mylogger.info(u'如果点击ORDER按钮后，系统产生订单警告提示，则点击继续按钮')
                test.alert_warning()#如果程序有警告提示，则点击继续
                mylogger.info(u'如果点击ORDER按钮后，系统产生订单延时提示，则点击保存后继续操作')
                test.alert_attention()#如果有attention提示，则点击保存
                mylogger.info(u'输入菜品信息:%s，点击查询按钮'%(user_csr['Item']))
                test.search_item(user_csr['Item'])#输入菜品，点击查询
                mylogger.info(u'选择菜品后，点击VIEW ORDER 按钮，并进入结算界面\n 点击 SAVE按钮、SEND_TO_RESTAURANT按钮')
                test.make_dict_item(user_csr['Item'])##选择菜名后，点击VIEW ORDER按钮，进入下一界面后点击保存并发送给餐厅
                mylogger.info(u'完成订单，进入ORDER LIST 界面，等待5S后，写入订单号到order_id.txt文件')
                orderId = test.orderNum_page()
                self.__re_orderNum(orderId)
                mylogger.info(u'完成订单测试，业务订单号:%s\n 关闭当前新订单界面'%(orderId))
                test.close_tab()
                time.sleep(5)
                mylogger.info(u'新订单模块测试完毕')
    def __re_orderNum(self,s):
        """返回ORDER_ID 后续OrderList使用"""
        with open(r'E:\python_web\mail\data\order_id.txt','w') as f:
            f.write(s)
    def tearDown(self):
       # self.driver.get_screenshot_as_file(r'E:\python_web\mail\png\%s.png'%(u'neworder'))
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()