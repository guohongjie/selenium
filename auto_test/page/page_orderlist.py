#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from auto_test.drivers.base import BasePage
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from auto_test.element.element_orderlist import OrderListElement
from page_neworder import NewOrderPage as new
class OrderListPage(BasePage,OrderListElement):
    def forwordstep(self,user,passwd):
        #封装登录操作
        self.logininCase(user,passwd)
    def display_tab(self):
        self.script(self.js)
    def open_module(self):
        self.find_element(*self.module_name).click()
    def close_tab_cd(self):
        # 关闭菜单页，进行模块操作
        self.script(self.hidden_js)
    def iframs_switch(self):
        # 进入模块内嵌HTML
        s = self.find_element(*self.iframe)
        self.switch_frame(s)
        time.sleep(2)
    def choice_time(self):
        time.sleep(2)
        self.find_element(*self.data_name).click()
        time.sleep(1)
        element = [self.today,self.data_checkbox,self.to_data_name,self.to_today]
        map(lambda x:self.find_element(*x).click(),element)
        time.sleep(1)
        self.find_element(*self.query_order).click()
        time.sleep(1)
    def data_order(self):
        s ={}
        my_order = self.find_element(*self.my_order_no)
        s['My Order'] = my_order.text
        if my_order.text:
            my_order.click()
        time.sleep(1)
        dispath_number = self.find_element(*self.dispatch_no)
        s['Dispath Number'] = dispath_number.text
        if dispath_number.text:
            dispath_number.click()
        time.sleep(1)
        need_send_to_restaurant = self.find_element(*self.need_send_to_rest_no)
        s['Need send to Restaurant Number'] = need_send_to_restaurant.text
        if need_send_to_restaurant.text:
            need_send_to_restaurant.click()
        time.sleep(1)
        delay_order = self.find_element(*self.delay_no)
        s['Delay Order'] = delay_order.text
        if delay_order.text:
            delay_order.click()
        time.sleep(1)
        locked_number = self.find_element(*self.locked_no)
        s['Locked Number'] = locked_number.text
        if locked_number.text:
            locked_number.click()
        time.sleep(5)
        un_f_c_order = self.find_element(*self.un_finished_Complain_order)
        s['Un-finished Complain Order'] = un_f_c_order.text
        if un_f_c_order.text:
            un_f_c_order.click()
        time.sleep(5)
        return s
    def total_order(self):
        total = []
        self.list_element = [self.web_order_check,self.phone_order_check,self.app_order_check,self.un_approved_web_order]
        map(lambda x:self.find_element(*x).click(),self.list_element)
        for m in range(len(self.list_element)):
            if m != 0:
                self.find_element(*self.list_element[m-1]).click()
            self.find_element(*self.list_element[m]).click()
            if m == (len(self.list_element)-1):
                self.find_element(*self.list_element[m]).click()
            time.sleep(2)
            self.find_element(*self.total_query).click()
            number,rest_total,order_total = self.find_element(*self.readonlyNumber).get_attribute('placeholder'),self.find_element(*self.readonlyRestTotal).get_attribute('placeholder'),self.find_element(*self.readonlyOrderTotal).get_attribute('placeholder')
            total.append([number,rest_total,order_total])
        map(lambda x: self.find_element(*x).click(), self.list_element)
        return total
    def inputOrder_query(self):
        """点击查询类型选项框，并选择ORDER_ID 类型，输入错误的订单号，点击查询"""
        self.find_element(*self.search_type).click()
        self.find_element(*self.order_id).click()
        self.find_element(*self.search_number).send_keys('123')
        self.find_element(*self.searchOthers).click()
        self.find_element(*self.order_status).click()
    def click_go(self):
        self.find_element(*self.go_button).click()
    def query_noFinished(self):
        time.sleep(5)
        self.find_element(*self.query_not_finished).click()
        time.sleep(2)
    def read_orderId(self):
        with open(r'E:\python_web\mail\data\order_id.txt','r') as f:
            orderID = f.read()
        return orderID
    def choice_order(self):
        self.find_element(*self.search_number).clear()
        self.find_element(*self.search_number).send_keys(self.read_orderId())
        self.click_go()
        self.find_element(*self.choiceFirstOrder).click()
        return self.read_orderId()
    def editORview(self):
        """点击edit&view 按钮，进行订单修改"""
        self.find_element(*self.editview).click()
        time.sleep(2)
        self.find_element(*self.save_as).click()
        time.sleep(5)
        self.find_element(*self.csr000807_btn_processing).click()
        element = self.find_element(*self.viewprocessing)
        if element:
            self.find_element(*self.x).click()
    def editAddressInfo(self):
        time.sleep(10)
        self.find_element(*self.editAddress).click()
        time.sleep(5)
       # self.find_element(*self.text_phone_error).click()
       # time.sleep(5)
       # self.find_element(*self.text_user_addrInfo).click()
       # time.sleep(5)
        self.find_element(*self.close_addrInfo_tab).click()
        time.sleep(5)
    def change_branch_information(self):
        element = [self.change_branch_info,self.next_button]
        map(lambda x:self.find_element(*x).click(),element)
        time.sleep(2)
    def RestBusinessHoursChange(self):
        """目前只编写餐厅营业时间变更按钮操作流程"""
        element =[self.btn_RestBusinessHoursChange,self.reason,self.reason_value,self.detailList,self.detailList_value]
        map(lambda x: self.find_element(*x).click(),element)
        self.find_element(*self.contactPerson).send_keys(u'测试')
        self.find_element(*self.btnCancel_CSR00060101).click()
        time.sleep(5)
        self.find_element(*self.x).click()
    def unlock_click(self):
        elements = self.find_elements(*self.unlock)
        elements[1].click()
        text = self.find_element(*self.unlock_text).text
        self.find_element(*self.ok_click).click()
        time.sleep(5)
        text_succeed = self.find_element(*self.unlock_succeed).text
        self.find_element(*self.ok_click).click()
        time.sleep(2)
        #self.find_element(*self.go_back).click()
        return text,text_succeed
    def click_order_infomation(self):
        time.sleep(2)
        elements = self.find_elements(*self.Edit_Order_Information)
        elements[1].click()
        time.sleep(5)
        self.find_element(*self.view_order).click()
        time.sleep(3)
    def unpayment_click(self):
        self.find_element(*self.btn_unpayment).click()
        time.sleep(3)
        self.find_element(*self.money_unpay).clear()
        self.find_element(*self.money_unpay).send_keys('1')
        self.find_element(*self.money_unpay_ok).click()
    def save_order(self):
        time.sleep(2)
        self.find_element(*self.save).click()
        time.sleep(5)
    def ifCannotOrder(self):
        elements_cannot_order = self.find_elements(*self.cannot_order)
        if elements_cannot_order:
            for m in elements_cannot_order:
                if u"现在无法接单，您是否需要换成别的餐厅？" in m.text:
                    self.find_element(*self.footer_button).click()
                    return m.text
    def ifPardenOrder(self):
        elements_parden_order = self.find_elements(*self.parden_order)
        if elements_parden_order:
            for m in elements_parden_order:
                if m.text == u"请与客人确认是否重单？":
                    self.find_element(*self.footer_button).click()
                    return m.text
    def click_save_ok(self):
        time.sleep(5)
        elements_click_save = self.find_elements(*self.save_ok)
        if elements_click_save:
            for m in elements_click_save:
                if m.is_displayed():
                    #   print m.text
                    m.click()
        time.sleep(5)
    def click_dispose(self):
        time.sleep(2)
        self.find_element(*self.dispose_complete).click()
        time.sleep(2)
        self.find_element(*self.ok_click).click()
        time.sleep(5)
        elements = self.find_elements(*self.textarea)
        if elements:
            elements[0].clear()
            self.find_element(*self.textarea).send_keys(u'测试')
            self.find_element(*self.add).click()
            time.sleep(2)
        elements = self.find_elements(*self.save_alert)
        w = elements[0].text
        if elements and w == u'订单解锁成功。':
            self.find_element(*self.ok_click).click()
            time.sleep(2)
            return w
        else:
            self.find_element(*self.ok_click).click()
            time.sleep(2)
            return w
    def send_to_restaurant(self):
        self.find_element(*self.btn_sent_to_restaurant).click()
        time.sleep(5)
        return u"发送餐厅成功，测试完毕"

    # def complaint(self):
    #     elements = self.find_elements(*self.edit_inner_complaint)
    #     elements[1].click()
    #     time.sleep(5)
    #     self.find_element(*self.x).click()
    # def un_payment(self):
    #     elements = self.find_elements(*self.Unpayment)
    #     elements[1].click()
    #     time.sleep(5)
    #     self.find_element(*self.x).click()
    # def change_item_infomation(self):
    #     elements = self.find_elements(*self.change_item_information)
    #     elements[1].click()
    #     time.sleep(5)
    #     self.find_element(*self.x).click()
    # def sold_out(self):
    #     elements = self.find_elements(*self.Sold_Out)
    #     elements[1].click()
    #     time.sleep(5)
    #     self.find_element(*self.x).click()
    # def edit_order_infomation(self):
    #     elements = self.find_elements(*self.Edit_Order_Information)
    #     elements[1].click()
    #     time.sleep(5)
    #     self.find_element(*self.x).click()
    def html(self):
        return self.return_html()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    base_url = r'http://192.168.98.22:8013/sherpa-dms3/login'
    pagetitle = "Sherpa's Login"
    a = OrderListPage(driver, base_url, pagetitle)
    a.forwordstep('yumi','111111')
    a.display_tab()
    a.open_module()
    a.close_tab_cd()
    a.iframs_switch()
   # a.choice_time()
    #a.data_order()
    #a.total_order()
    #a.inputOrder_query()
   # a.click_go()
   # a.query_noFinished()
   # wc = a.html()
    a.choice_order()
    a.editORview()
   # a.editAddressInfo()
   # a.change_branch_information()
   # a.RestBusinessHoursChange()
    a.unlock_click()
    a.click_order_infomation()
    a.unpayment_click()
    a.save_order()
    a.ifCannotOrder()
    a.ifPardenOrder()
    a.click_save_ok()
    a.click_dispose()
    a.send_to_restaurant()




    # from bs4 import BeautifulSoup
    # import re
    # with open('date.html','r') as f:
    #     html = f.read()
    # soup = BeautifulSoup(html,'html.parser')
    # list_attr = soup.find_all('tr',attrs={'class':re.compile('bui-grid-row bui-grid-row-\w.[a-z]\w')})
    # new_html = """<html>
    # <body>
    # %s
    # </body></html>"""%(list_attr)
    # soup = BeautifulSoup(new_html,'html.parser')
    # la = soup.find_all('span',attrs={'class':"bui-grid-cell-text "})
    # for m in la:
    #     print m
