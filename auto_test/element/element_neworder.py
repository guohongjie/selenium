#-*-coding:utf-8 -*-
from selenium.webdriver.common.by import By
class NeworderElement(object):
    module_name = (By.XPATH, "//li[@data-id='CSRM001']")  # 新订单模块
    iframe = (By.XPATH, "//div[@class='tab-content']/iframe")  # 进入页面IFRAME
    customer_name = (By.XPATH, "//input[@type='text' and @name='conditions']")  # 用户信息输入栏
    # sosuo_button = (By.XPATH, "//span[@class='icon-search']")
    nobody_alert_tab = (By.XPATH, "//div[@class='bui-message bui-dialog bui-overlay bui-ext-position x-align-cc-cc']")
    # nobody_alert_tab为该用户不存在的提示窗口
    nobody_alert_choice = (By.XPATH, "//button[@class='button button-warning']")
    # customer_tab = (By.XPATH, "//li[@data-pgid='CSR0004']")
    # customer_order = (By.XPATH, "//form[@id='addressEidtForm']/div[10]/div/div/button[6]")
    search_input = (By.ID, "r_i_search")  # 餐厅输入栏
    # search_go = (By.ID, "btn_go")
    rest_choice = (By.XPATH, "//td[@class='  bui-grid-cell grid-td-RestNameCn']")  # 餐厅选择元素
    BranchCn = (By.XPATH, "//td[@data-column-id='BranchCn']")  # 分店餐厅名称
    rest_order = (By.XPATH, "//span[@class='grid-command orderLink']")  # 分店餐厅对应的ORDER链接
    bui_icon = (By.XPATH, "//i[@class='bui-grid-cascade-icon']")  # 折叠田图标元素
    orderLink = (By.XPATH, "//td[@data-column-id='orderLink']")
    warning = (By.XPATH, "//div[text()='Warning']")  # 选择餐厅后有可能会弹出WARING窗口，告知该餐厅还未营业
    jixu = (By.XPATH, "//button[text()='%s']" % (u'继续'))
    attention = (By.XPATH, "//div[text()='Attention']")  # 选择餐厅后有可能会弹出Attention窗口，告知延时
    ordernow = (By.ID, 'OrderNow')  # 如果有attention，点击OrderNow按钮
    search_item_input = (By.XPATH, "//input[@name='searchValue']")  # 菜品输入栏
    nameCh = (By.XPATH, "//td[@data-column-id='nameCh']")  # 菜品名称
    order_item = (By.XPATH, "//a[@href='####']")  # 菜品名称对应的ORDER
    maybe_alert_dailog = (
    By.XPATH, "//div[@class='bui-dialog bui-overlay bui-ext-position custom-dialog x-align-tc-tc']")
    # 选择菜品后，弹出的子菜品弹出框标头
    must_choose = (By.XPATH, "//ul[@id='mustChooseTree10465018_1_ul']/li[1]/span[2]")  # 必选子菜品
    click_OK = (By.ID, 'btnOk_CSR000606')  # 点击OK按钮
    view_order = (By.ID, "btn_viewOrder")  # VIEW_ORDER按钮
    save = (By.ID, "btn_save")  # 点击SAVE按钮，完成订单保存
    save_ok = (By.XPATH, "//button[text()='Ok']")  # 保存成功弹出框
    parden_order = (By.XPATH, "//div[@class='bui-message-content']/p[3]")  # 是否弹出订单重复提醒的标头
    footer_button = (By.XPATH, "//div[@class='bui-stdmod-footer']/button[2]")  # 点击确定订单重复的SAVE按钮
    send_restaurant = (By.ID, "btn_sent_to_restaurant")  # 发送餐厅按钮
    cannot_order = (By.XPATH, "//div[@class='bui-message-content']/p[1]") #定位无法接单弹出框
    close_moduletab = (By.XPATH, "//s[@class='tab-item-close']")
    orderNo = (By.XPATH, "//td[@data-column-field='orderNo']")
    unpayment_alert = (By.XPATH, "//div[text()='未收款提醒']")
    payToday = (By.XPATH, "//button[@id='btn_pay_today']")