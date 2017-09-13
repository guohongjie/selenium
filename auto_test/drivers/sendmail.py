#-*- coding:utf:8 -*-
import smtplib
from email.mime import multipart,text
import email
import time
from email.mime.text import MIMEText
import string
import time
class AutoSendMail(object):
    def __init__(self,fromUser,fromPwd,toUser,filePath,fileName,zipPath,zipName):
        self.user_data = {'fromuser':fromUser,'frompwd':fromPwd,'touser':toUser,
                          'filepath':filePath,'filename':fileName,
                          'zippath':zipPath,'zipname':zipName}
    def __call__(self,smtp_server,port_num,connect):
        self.msg = multipart.MIMEMultipart()
        self.msg['Subject'] = '%s %s' % (u'DMS3_WEB_UI自动化测试',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        self.msg['From'] = self.user_data['fromuser']
        self.msg['To'] = self.user_data['touser']
        self.__addContent(connect)
        self.__attachFile(self.user_data['filepath'],self.user_data['filename'])
        self.__attachZip(self.user_data['zippath'],self.user_data['zipname'])
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server,port_num)
        smtp.login(self.user_data['fromuser'], self.user_data['frompwd'])
        smtp.sendmail(self.user_data['fromuser'], self.user_data['touser'], self.msg.as_string())
        smtp.quit()
        print('邮件发送成功 \n email has send out !')
    def __addContent(self, content):
        # 构造文本内容，添加内容
        txt = MIMEText(content, 'html', 'utf-8')
        self.msg.attach(txt)
    def __attachFile(self, filePath, fileName):
        # 构造附件，传送文件
        att = MIMEText(open('%s' % (filePath), 'rb').read())
        att["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att["Content-Disposition"] = 'attachment; filename="%s"' % (fileName)
        self.msg.attach(att)


    def __attachZip(self,zipPath,zipName):
        # 构造附件，传送文件
        att = MIMEText(open('%s' % (zipPath), 'rb').read())
        att["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att["Content-Disposition"] = 'attachment; filename="%s"' % (zipName)
        self.msg.attach(att)

if __name__ == '__main__':
    subject = 'DMS3_WEB_UI自动化测试'
    # file = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/report/20170719-095357.html'
    file = r"E:\python_web\mail\report\wc.html"
    fn = r'WebAutoTest.html'
    MAIL_DRIVER = 'smtp'
    MAIL_HOST = 'smtp.263.net'
    MAIL_PORT = '25'
    MAIL_USERNAME = r'qa-report@daojia.com.cn'
    MAIL_PASSWORD = 'Djia2017'
    MAIL_FROM_ADDRESS = r'qa-report@daojia.com.cn'
    zipf = r'E:\python_web\mail\result.zip'
    zipn = r'result.zip'
    file_object = open(file)
    try:
        content = file_object.read()
    finally:
        file_object.close()
    mail = AutoSendMail(MAIL_USERNAME,MAIL_PASSWORD,MAIL_FROM_ADDRESS,file,fn,zipf,zipn)
    mail(MAIL_HOST,MAIL_PORT,content)