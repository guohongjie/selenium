#-*-coding:utf-8 -*-
"""定位器，通过元素属性定位元素对象"""
from selenium.webdriver.common.by import By
class CallcenterElement(object):
    module_name = (By.XPATH, "//li[@data-id='CSRM003']")  # 新订单模块
    iframe = (By.XPATH, "//div[@class='tab-content']/iframe")
    btn_follow = (By.XPATH, "//button[@id='btn_follow']") #需跟进订单总量
    title_follow = (By.XPATH, "//th[@class='bui-grid-hd']") #获取标题
    btn_response = (By.XPATH, "//button[@id='btn_response']") #处理订单总表
    btn_go_response = (By.XPATH, "//button[@id='btn_go_response']") #GO 按钮
    no_data_display = (By.XPATH, "//h2[text()='没有匹配数据']") #没有数据显示
    btn_complaint = (By.XPATH, "//button[@id='btn_complaint']") # PM
    btn_go = (By.XPATH, "//button[@id='btn_go']")

