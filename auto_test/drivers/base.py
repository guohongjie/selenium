#-*-coding:utf-8 -*-
"""
Project:基础类BasePage，封装所有页面都公用的方法，
定义open函数，重定义find_element，switch_frame，send_keys等函数。
在初始化方法中定义驱动driver，基本url，title
WebDriverWait提供了显式等待方式。
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from auto_test.drivers.excel import Excel
import time
class BasePage(object):
    """
    BasePage封装所有页面都公用的方法，例如driver, url ,FindElement等
    """
    # 初始化driver、url、pagetitle等
    # 实例化BasePage类时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参。
    # __init__方法不能有返回值，只能返回None
    # self只实例本身，相较于类Page而言。
    def __init__(self, selenium_driver, base_url, pagetitle):
        self.driver = selenium_driver
        self.base_url = base_url
        self.pagetitle = pagetitle
        #该JS 是用于显示隐藏的TAB页的
        self.js = """var elements = document.getElementsByClassName("dl-tab-item dl-collapse");
                for (var i=0;i<elements.length;i++)
                {elements[i].className="dl-tab-item";}
                """
        self.hidden_js = """var elements = document.getElementsByClassName("dl-tab-item");
                        for (var i=0;i<elements.length;i++)
                        {elements[i].className="dl-tab-item dl-collapse";}
                        """
    # 通过title断言进入的页面是否正确。
    # 使用title获取当前窗口title，检查输入的title是否在当前title中，返回比较结果（True 或 False）
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title
    # 打开页面，并校验页面链接是否加载正确
    # 以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的。
    def _open(self, url, pagetitle):
        # 使用get打开访问链接地址
        self.driver.get(url)
        self.driver.maximize_window()
        # 使用assert进行校验，打开的窗口title是否与配置的title一致。调用on_page()方法
        assert self.on_page(pagetitle), u"打开开页面失败 %s" % url
    # 定义open方法，调用_open()进行打开链接
    def open(self):
        self._open(self.base_url, self.pagetitle)
    # 重写元素定位方法
    def find_element(self, *loc):
        #        return self.driver.find_element(*loc)
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            # 注意：以下入参本身是元组，不需要加*
            time.sleep(1)
            WebDriverWait(self.driver, 15,1).until(EC.element_to_be_clickable(loc))
            self.log(u'查找元素：',loc[1],bool=True)
            return self.driver.find_element(*loc)
        except Exception as e:
            result = "Can not found %s element \n%s" % (loc[1], e)
            self.log(result,loc[1],bool=False)
            #raise e
    # 重写switch_frame方法
    def find_elements(self, *loc):
        try:
            web_element_list = self.driver.find_elements(*loc)
            return web_element_list
        except Exception as e:
            result = "Can not found %s element \n%s" % (loc, e)
            self.log(result, loc, bool=False)
            #raise e
    def switch_frame(self,loc):
        self.driver.switch_to_frame(loc)
    # 定义script方法，用于执行js脚本，范围执行结果
    def switch_to_default_content(self):
        self.driver.switch_to_default_content()
    def script(self, src):
        self.driver.execute_script(src)
    def explorer_title(self):
        """打印页面标题"""
        return self.driver.title
    def accept_alert(self,bool=True):
        """增加JS弹出框处理"""
        accepts = self.driver.switch_to_alert()
        if bool:
            accepts.accept()
        else:
            accepts.dismiss()
    def close(self):
        """关闭模块"""
        self.driver.close()
    def refresh(self):
        self.driver.refresh()
    def db_mysql(self):
        """预留"""
        pass
    def return_html(self):
        return self.driver.page_source
    def log(self, result, element ,bool = False):
        filePath = r'E:\python_web\mail\log'
        filename = filePath +"\\"+ time.strftime("%Y%m%d") + '.log'
        if bool:
            with open(filename, 'a+') as f:
                f.write('[' + time.strftime("%Y-%m-%d %H:%M:%S") + '] ' + element+'    '+ 'was enable! ' + '\n')
        else:
            imageName = self.screenShots()
            with open(filename, 'a+') as f:
                f.write('[' + time.strftime("%Y-%m-%d %H:%M:%S") + '] ' + imageName + ' '+ element + 'was error' + '\n')
    def screenShots(self):
        filepath = r'E:\python_web\mail\png'
        imageName = time.strftime("%Y%m%d-%H%M%S") + '.png'
        file ="%s"%(filepath+'\\'+imageName)
        self.driver.save_screenshot(file)
        return imageName
    def logininCase(self,user,passwd):
        #定义登录操作，因为每个模块都要先登录，写到PAGE 里 则产生大量登录代码，故封装至，驱动层
        self.open()
        self.driver.find_element_by_xpath("//input[@name='userId']").send_keys(user)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(passwd)
        #element = self.driver.find_element_by_xpath("//button[@type='submit']").get_attribute('disabled')
        #if element:
        #    time.sleep(30)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Ok']"))).click()
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='icon-login']"))).click()
        #moduleName = self.driver.find_element_by_class_name("dl-tab-item").text
        #self.driver.execute_script(self.hidden_js)
        #time.sleep(5)


