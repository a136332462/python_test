#coding:utf-8
import time, os
import unittest
import HTMLTestRunner
from public import send_mail
import sys
reload(sys)
sys.setdefaultencoding('utf8')


#查找测试报告，调用发邮件功能 
def sendreport():
	result_dir =  (os.getcwd() + '/all_script/test_data/result/')
	lists = os.listdir(result_dir)
	lists.sort(key = lambda fn: os.path.getmtime(result_dir + '/' + fn)
		if not os.path.isdir(result_dir + '/' + fn) else 0)
	print(u'最新测试生成的报告:' + lists[-1])
	#找到最新生成的文件
	file_new = os.path.join(result_dir, lists[-1])
	print file_new
	#调用发邮件模块
	send_mail.send_mail(file_new)

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
	sendreport()
	

