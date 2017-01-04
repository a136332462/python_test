#coding:utf-8
import time, os
import unittest
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#========================定义发送邮件========================
# def send_mail(file_new):
# 	mail_from = 'my126sw@126.com'  #发信邮箱
# 	mail_to = 'my126sw@126.com'   #收信邮箱
# 	#定义正文
# 	f = open(file_new, 'rb')
# 	mail_body = f.read()
# 	f.close()
# 	msg = MIMEText(mail_body, _subtype = 'html', _charset = 'utf-8')
# 	#定义标题






















#========================将测试用例添加到测试套件========================
def creatsuite():
	testunit = unittest.TestSuite()
	#定义测试文件查找的目录
	test_dir = (os.getcwd() + '/all_script/')
	#定义 discover 方法的参数
	discover = unittest.defaultTestLoader.discover(
		test_dir,
		pattern = 'start_*.py',
		top_level_dir = None)
	#discover 方法筛选出来的用例，循环添加到测试套件中
	for test_case in discover:
		testunit.addTests(test_case)
	return testunit

now_time = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
filename = (os.getcwd() + '/all_script/test_data/result/') + now_time + "result.html" #测试用例结果存放位置
fp = file(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
	stream = fp,
	title = '测试用例报告',
	description = u'用例执行情况'
	)

if __name__ == '__main__':
	alltestnames = creatsuite()
	runner.run(alltestnames)
	fp.close()

