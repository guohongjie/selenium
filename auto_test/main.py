#-*-coding:utf-8 -*-
import socket
import sys
sys.path.append('..')
import HTMLTestRunnerCN
import unittest
from auto_test.drivers.sendmail import AutoSendMail
from auto_test.module import module_login
from auto_test.module import module_main
from auto_test.module import module_neworder
from auto_test.module import module_orderlist
from auto_test.module import module_callcenterQC
from auto_test.drivers.zip_file import addfile
from bs4 import BeautifulSoup
class Jiance(object):
    def __init__(self):
        self.testsuite = unittest.TestSuite()

    def testAll(self):
        self.testsuite.addTest(module_login.CaseLogin('test_login'))
        self.testsuite.addTest(module_main.CaseMain('test_main'))
        self.testsuite.addTest(module_neworder.CaseOrder('test_new_order'))
        self.testsuite.addTest(module_orderlist.CaseOrderList('test_orderlist'))
        self.testsuite.addTest(module_callcenterQC.CaseCallCenterQC('test_callcenter'))
        return self.testsuite

if __name__ == "__main__":
    localIP = socket.gethostbyname(socket.gethostname())#这个得到本地ip
    start = Jiance()
    fp = open(r'E:\python_web\mail\report\wc.html', 'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='测试报告', description='测试执行情况')
    runner.run(start.testAll())
    fp.close()
    subject = 'DMS3_WEB_UI自动化测试'
    # file = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/report/20170719-095357.html'
    file = r"wc.html"
    fn = r''
    MAIL_DRIVER = ''
    MAIL_HOST = ''
    MAIL_PORT = ''
    MAIL_USERNAME = r''
    MAIL_PASSWORD = ''
    MAIL_FROM_ADDRESS = r''
    file_object = open(file)
    content = file_object.read()
    soup = BeautifulSoup(content,'html.parser')
    fixed_html = soup.prettify()
    ul = soup.find('div',attrs={'class':'heading'})
    html ="""<html>
        <body>
        <P>Jenkins 地址  %s:8080 </P>
        <P>Jenkins 用户  %s </P>
        <P>Jenkins 密码  %s </P>
        <P>运行日志链接  %s </P>
        <p>详情请见附件(建议下载HTML后查看)</p>
        %s
        </body>
        </html>"""%(localIP,'','',r'\\GUOHONGJIE\mail',ul)
    file_object.close()
    zipfile = r''
    zipn = r''
    addfile(zipn,zipfile)
    mail = AutoSendMail(MAIL_USERNAME,MAIL_PASSWORD,MAIL_FROM_ADDRESS,file,fn,zipn,'result.zip')
    mail(MAIL_HOST, MAIL_PORT, html)
