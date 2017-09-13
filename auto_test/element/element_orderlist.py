#-*-coding:utf-8 -*-
from selenium.webdriver.common.by import By
class OrderListElement(object):
    module_name = (By.XPATH, "//li[@data-id='CSRM002']")  # 新订单模块
    iframe = (By.XPATH, "//div[@class='tab-content']/iframe")  # 进入页面IFRAME
    data_name = (By.XPATH, "//input[@name='searchFromDate']") #选择日期输入框
    today = (By.XPATH, "//ul[@id='bar5']/li[1]/button")
    to_today = (By.XPATH, "//ul[@id='bar7']/li[1]/button")
    data_checkbox =(By.XPATH, "//input[@id='chkSearchToDate']") #口to 选择框
    to_data_name = (By.XPATH, "//input[@name='searchToDate']") #结束日期选择框
    query_order = (By.XPATH, "//button[@id='csr0008_btn_queryCount']") #查询按钮
    my_order_no = (By.XPATH, "//span[@id='csr0008MyOrder']")#d定位查找到的订单数量
    dispatch_no = (By.XPATH, "//span[@id='csr0008Dispatch']")
    need_send_to_rest_no = (By.XPATH, "//span[@id='csr0008NeedSendToRest']")
    delay_no = (By.XPATH, "//span[@id='csr0008DelayOrder']")
    delay_order = (By.XPATH, "//span[@id='csr0008DelayOrder']")
    locked_no = (By.XPATH, "//span[@id='csr0008Locked']")
    un_finished_Complain_order = (By.XPATH, "//span[@id='csr0008UfcOrder']")
    button_show = (By.XPATH, "//button[@id='csr0008_btn_buttonShow']")
    total_query = (By.XPATH, "//button[@id='csr0008_btn_queryListCount']") #统计查询按钮
    web_order_check = (By.XPATH, "//input[@name='chkWebOrder']")
    phone_order_check = (By.XPATH, "//input[@name='chkPhoneOrder']")
    app_order_check = (By.XPATH, "//input[@name='chkAppOrder']")
    un_approved_web_order = (By.XPATH, "//input[@name='chkUnApprovedWebOrder']")
    readonlyNumber = (By.XPATH,  "//input[@id='readonlyNumber']")
    readonlyRestTotal = (By.XPATH,  "//input[@id='readonlyRestTotal']")
    readonlyOrderTotal = (By.XPATH,  "//input[@id='readonlyOrderTotal']")
    search_type = (By.XPATH, "//select[@id='searchNumberType']")
    order_id = (By.XPATH, "//option[text()='Order ID']")
    search_number = (By.XPATH, "//input[@id='searchNumber']")
    searchOthersType = (By.XPATH, "//select[@id='searchOthersType']")
    searchOthers = (By.XPATH, "//input[@id='searchOthers']") #点击路名选择框
    searchTime = (By.XPATH, "//input[@id='searchTime']")# 点击时间选择框
    go_button = (By.XPATH, "//button[@id='csr0008_btn_go']")
    order_status = (By.XPATH, "//select[@id='searchOrderStatus']")
    searchInResult = (By.XPATH, "//button[@id='csr0008_btn_searchInResult']")
    trash_button = (By.XPATH, "//button[@id='csr0008_btn_trash']")
    fapiao_delivery = (By.XPATH,"//button[@id='csr0008_btn_fapiaoDelivery']")
    query_not_finished = (By.XPATH, "//button[@id='csr0008_btn_querynotfinished']")
    editview = (By.XPATH, "//button[@id='csr0008_btn_editview']") #点击修改按钮
    viewProcessing = (By.XPATH, "//button[@id='csr0008_btn_viewProcessing']")
    complaint_button = (By.XPATH, "//button[@id='csr0008_btn_complaint']")
    send_email = (By.XPATH, "//button[@id='csr0008_btn_sendEmail']")
    send_EMS = (By.XPATH, "//button[@id='csr0008_btn_sendSMS']")
    feetback = (By.XPATH, "//button[@id='csr0008_btn_feedback']")
    trash_box = (By.XPATH, "//button[@id='csr0008_btn_trashBox']")
    cpcPhone = (By.XPATH, "//button[@id='csr0008_btn_copyCourierPhone']")
    orderdispath = (By.XPATH, "//button[@id='csr0008_btn_orderDispatch']")
    copyRestaurantPhone = (By.XPATH, "//button[@id='csr0008_btn_copyRestaurantPhone']")
    openDoorPhone = (By.XPATH, "//button[@id='csr0008_btn_openDoorPhone']")
    choiceFirstOrder = (By.XPATH, "//td[@data-column-id='col1']")
    save_as =(By.XPATH, "//button[@id='csr000807_btn_saveAs']")
    csr000807_btn_processing = (By.XPATH, "//button[@id='csr000807_btn_processing']")
    viewprocessing = (By.XPATH, "//div[@class='bui-stdmod-header']")
    x = (By.XPATH, "//span[@class='bui-ext-close-x x-icon x-icon-normal']")
    editAddress = (By.XPATH,"//button[@id='csr000807_btn_editAddress']")
    text_phone_error = (By.XPATH,"//div[id='CSR000808TAB']/ul[1]/li[2]")
    text_user_addrInfo = (By.XPATH, "//div[id='CSR000808TAB']/ul[1]/li[3]")
    close_addrInfo_tab = (By.XPATH, "//span[@class='bui-ext-close-x x-icon x-icon-normal']")
    change_branch_info = (By.XPATH, "//div[@id='orderItemView0']/div[2]/div[3]/div[2]/button")
    next_button = (By.XPATH, "//button[text()='Next']")
    btn_RestBusinessHoursChange = (By.XPATH, "//button[@id='btn_RestBusinessHoursChange']")#餐厅营业时间变更
    reason = (By.XPATH, "//select[@name='reason']")#Reason
    reason_value = (By.XPATH, "//select[@name='reason']/option[2]")#节假日
    detailList = (By.XPATH, "//select[@id='detailList']")
    detailList_value = (By.XPATH, "//select[@id='detailList']/option[2]")#Labor's day/劳动节
    contactPerson = (By.XPATH, "//input[@id='contactPerson']") #contactPerson
    btnCancel_CSR00060101 = (By.XPATH, "//button[@id='btnCancel_CSR00060101']") #Cancel
    btn_RestaurantBackToNormal = (By.XPATH, "//button[@id='btn_RestaurantBackToNormal']")
    unlock = (By.XPATH, "//div[@class='control-group span14 text-right csr000807OrderButtonItem']/button[1]")
    unlock_text = (By.XPATH, "//div[@class='bui-message-content']")
    ok_click = (By.XPATH, "//button[text()='Ok']")
    unlock_succeed = (By.XPATH, "//div[@class='bui-message-content']")
    # edit_inner_complaint = (By.XPATH, "//div[@class='control-group span14 text-right csr000807OrderButtonItem']/button[2]")
    # Unpayment = (By.XPATH, "//div[@class='control-group span14 text-right csr000807OrderButtonItem']/button[3]")
    # change_item_information = (By.XPATH, "//div[@class='control-group span14 text-right csr000807OrderButtonItem']/button[4]")
    # Sold_Out = (By.XPATH, "//div[@class='control-group span14 text-right csr000807OrderButtonItem']/button[5]")
    Edit_Order_Information = (By.XPATH, "//button[@class='button button-primary csr000807_btn_editOrderInfomation']")
    #go_back = (By.XPATH, "//button[text()='返回']")
    view_order = (By.XPATH, "//button[@id='btn_viewOrder']")#点击VIEW ORDER按钮
    btn_unpayment =(By.XPATH, "//button[@id='btn_unpayment']")#点击UNPAYMENT 按钮
    money_unpay = (By.XPATH, "//input[@name='amount']") #未收款的金额
    money_unpay_ok = (By.XPATH, "//button[@id='CSR000804btnOk']")
    save = (By.ID, "btn_save")  # 点击SAVE按钮，完成订单保存
    cannot_order = (By.XPATH, "//div[@class='bui-message-content']/p[1]") #定位无法接单弹出框
    footer_button = (By.XPATH, "//div[@class='bui-stdmod-footer']/button[2]")  # 点击确定订单重复的SAVE按钮
    parden_order = (By.XPATH, "//div[@class='bui-message-content']/p[3]")  # 是否弹出订单重复提醒的标头
    save_ok = (By.XPATH, "//button[text()='Ok']")  # 保存成功弹出框

    save_alert = (By.XPATH, "//div[@class='bui-message-content']")
    dispose_complete = (By.XPATH, "//button[@id='btn_processing']") #处理完成按钮
    textarea = (By.XPATH, "//textarea[@name='problemDetail']") #输入原因
    add = (By.XPATH, "//button[text()='ADD']")
    btn_sent_to_restaurant = (By.XPATH, "//button[@id='btn_sent_to_restaurant']")
