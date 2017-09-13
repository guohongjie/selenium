#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from auto_test.drivers.base import BasePage
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from auto_test.element.element_neworder import NeworderElement
class NewOrderPage(BasePage,NeworderElement):
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
    def soso_name(self,TelPhone_NUM):
    # 定位"搜索电话号码  / 客人姓名 / 电子邮箱"输入框，并输入文本内容
        self.find_element(*self.customer_name).send_keys(TelPhone_NUM)
        self.find_element(*self.customer_name).send_keys(Keys.ENTER)
    #点击搜索按钮
    def click_sosuo_button(self,telPhone):
        time.sleep(5)
        elements = self.find_elements(*self.nobody_alert_tab)#判断是否有提示窗口
        if len(elements) != 0:
            self.__nobody_exist(telPhone)
    def __nobody_exist(self,telPhone):
    #当用户不存在，系统弹出提示窗口
        elements = self.find_elements(*self.nobody_alert_choice)
        button_text = ['Try Another Number']  # 这里暂且把一个按钮增加进去，后续为单独创建分支
        element = [e for e in elements if e.text in button_text]
        for m in element:
            m.click()
        self.soso_name(telPhone)
    # def __body_exist(self):
    #     #返回Customer TAB 页，从头操作
    #     self.find_element(*self.customer_tab).click()
    #     #self.find_element(*self.customer_tab).click()
    # def customer_message(self):
    #     #点击ORDER按钮，进入Restaurant界面
    #     time.sleep(5)
    #     self.find_element(*self.customer_order).click()
    def ifUnpay(self):
        elements = self.find_elements(*self.unpayment_alert)
        if elements:
            time.sleep(2)
            self.find_element(*self.payToday).click()
            return u'用户未收款金额已选择随订单支付'
        else:
            return u'用户未存在未收款金额'
    def restaurant_search(self,rest_name):
        #餐厅界面，输入、查询
        time.sleep(2)
        self.find_element(*self.search_input).send_keys(rest_name)
        self.find_element(*self.search_input).send_keys(Keys.ENTER)
       # self.find_element(*self.search_go).click()
    def restaurant_choice(self,rest_name):
        #选择餐厅，获取所有餐厅信息
        time.sleep(5)
        elements = self.find_elements(*self.rest_choice)
        for m in elements:
            if m.text != rest_name:
                time.sleep(5)
            else:#打开分店信息
                #time.sleep(1)
                #self.find_element(*self.bui_icon).click() #这次点击关闭了左侧的菜单页
                time.sleep(30)
                #self.find_element(*self.orderLink).click()
                #因为点击分组 总是出现元素不可被点击
                element_click = self.find_elements(*self.bui_icon)
                for bui in element_click:
                    bui.click()
                #m.click()
    def click_rest_order(self,Branch_name):
        #点击总餐厅的ORDER，细分选择分店,生成字典 key:餐厅名称 value:order
        rest_name = []
        time.sleep(5)
        rest_key = self.find_elements(*self.BranchCn)
        for m in rest_key:
            rest_name.append(m.text)
        rest_value = self.find_elements(*self.rest_order)
        rest_order = []
        for m in rest_value:
            rest_order.append(m)
        restaurent_dict = dict(zip(rest_name,rest_order))
      #  print restaurent_dict
        restaurent_dict[Branch_name].click()
    def alert_warning(self):
        #针对与选择餐厅后系统提示出warning
        time.sleep(5)
        elements = self.find_elements(*self.warning)
        if elements:
            self.find_element(*self.jixu).click()
    def alert_attention(self):
        """点击ORDER后，根据餐厅设置，偶会提示attention)窗口，提示后点击MAKE ORDER继续点餐"""
        time.sleep(1)
        elements = self.find_elements(*self.attention)
        if elements:
            self.find_element(*self.ordernow).click()
    def search_item(self,item_name):
        #点击菜品查询按钮，显示菜品
        time.sleep(5)
        self.find_element(*self.search_item_input).send_keys(item_name)
        self.find_element(*self.search_item_input).send_keys(Keys.ENTER)
    def make_dict_item(self,item_name):
        """生成菜品：ORDER 字典，进行点餐，并SAVE，SEND TO RESTAURANT"""
        time.sleep(5)
        list_cpmc = []
        for item in self.find_elements(*self.nameCh):
            list_cpmc.append(item.text)
        list_order = []
        for item_order in self.find_elements(*self.order_item):
            list_order.append(item_order)
        dict_orders = dict(zip(list_cpmc, list_order))
        dict_orders[item_name].click()
        # 该饭可能需要子菜品配置，故判断操作，如有 则操作弹出框
        elements = self.find_elements(*self.maybe_alert_dailog)
        if len(elements) == 0:
            # 如果没有弹出框，
            print 'no alert'
        else:
            time.sleep(2)
            self.find_element(*self.must_choose).click()
            self.find_element(*self.click_OK).click()
            time.sleep(2)
            self.find_element(*self.view_order).click()
            self.savetoRest()
            self.send_to_restaurant()
    def savetoRest(self):
            time.sleep(2)
            self.find_element(*self.save).click()
            time.sleep(5)
            elements_cannot_order = self.find_elements(*self.cannot_order)
            if elements_cannot_order:
                for m in elements_cannot_order:
                    if u"现在无法接单，您是否需要换成别的餐厅？" in m.text:
                        self.find_element(*self.footer_button).click()
            elements_parden_order = self.find_elements(*self.parden_order)
            if elements_parden_order:
                for m in elements_parden_order:
                    if m.text == u"请与客人确认是否重单？":
                        self.find_element(*self.footer_button).click()

            time.sleep(5)
            elements_click_save = self.find_elements(*self.save_ok)
            if elements_click_save:
                for m in elements_click_save:
                    if m.is_displayed():
                     #   print m.text
                        m.click()
            time.sleep(5)
    def send_to_restaurant(self):
            self.find_element(*self.send_restaurant).click()
            time.sleep(5)
    def orderNum_page(self):
        """返回新订单产生的订单号码"""
        return self.find_element(*self.orderNo).text

    def close_tab(self):
        """关闭新订单界面"""
        self.switch_to_default_content()
        time.sleep(1)
        self.find_element(*self.close_moduletab).click()
        time.sleep(1)






if __name__ == "__main__":
    driver = webdriver.Chrome()
    base_url = r'http://192.168.98.22:8013/sherpa-dms3/login'
    pagetitle = "Sherpa's Login"
    a = NewOrderPage(driver, base_url, pagetitle)
    a.forwordstep('yumi','111111')
    a.open_module()
    a.close_tab_cd()
    a.iframs_switch()
    a.soso_name('1231231999')
    a.click_sosuo_button()
    #a.customer_message()
    a.restaurant_search()
    a.restaurant_choice()
    a.click_rest_order()
    a.alert_warning()
    a.alert_attention()
    a.search_item()
    a.make_dict_item()

