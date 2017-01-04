#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time, re, sys, unittest
sys.path.append("..")
from public import *
reload(sys)
sys.setdefaultencoding('utf-8')

class Baidu(unittest.TestCase):

	def setUp(self):
		#参数设置
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.login_url = linkadress.link()
		self.verificationErrors = []
		self.accept_alert_next = True

	def test_baidu(self):
		'''百度测试'''
		driver = self.driver
		driver.get(self.login_url)
		location.findId(driver, 'userid').clear()
		location.findId(driver, 'userid').send_keys('a12406')
		location.findId(driver, 'password').clear()
		location.findId(driver, 'password').send_keys('123456.')
		location.findId(driver, 'signIn').click()

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
	unittest.main()
