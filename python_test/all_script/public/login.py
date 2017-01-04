#coding=utf-8
from selenium import webdriver

'''登录模块'''
def login(driver):
	driver.maximize_window()
	driver.find_element_by_id('userid').clear()
	driver.find_element_by_id('userid').send_keys('a12362')
	driver.find_element_by_id('password').clear()
	driver.find_element_by_id('password').send_keys('123456.')
	driver.find_element_by_xpath("/html/body/div[3]/div/form/div[2]/p/button").click()

def login_parameter(driver, uname, pword):
	driver.maximize_window()
	driver.find_element_by_id('userid').clear()
	driver.find_element_by_id('userid').send_keys(uname)
	driver.find_element_by_id('password').clear()
	driver.find_element_by_id('password').send_keys(pword)
	driver.find_element_by_xpath("/html/body/div[3]/div/form/div[2]/p/button").click()
	