#coding = utf-8
from selenium import webdriver


def findId(driver, id):
	f = driver.find_element_by_id(id)
	return f

def findName(driver, name):
	f = driver.find_element_by_name(name)
	return f

def findClassName(driver, name):
	f = driver.find_element_by_class_name(name)
	return f 

def findTagName(driver, name):
	f = driver.find_element_by_tag_name(name)
	return f 

def findLinkText(driver, text):
	f = driver.find_element_link_text(text)
	return f 

def findPLinkText(driver, text):
	f = driver.find_element_partial_link_text(text)
	return f 

def findXpath(driver, xpath):
	f = driver.find_element_by_xpath(xpath)
	return f 

def findCssSelector(driver, css):
	f = driver.find_element_by_css_selector(css)
	return f 




def findsId(driver, id):
	f = driver.find_elements_by_id(id)
	return f 

def findsName(driver, name):
	f = driver.find_elements_by_name(name)
	return f 

def findsClassName(driver, name):
	f = driver.find_elements_by_class_name(name)
	return f 

def findsTagName(driver, name):
	f = driver.find_elements_by_tag_name(name)
	return f 

def findsLinkText(driver, text):
	f = driver.find_elements_link_text(text)
	return f 

def findsPLinkText(driver, text):
	f = driver.find_elements_partial_link_text(text)
	return f 

def findsXpath(driver, xpath):
	f = dirver.find_elements_by_xpath(xpath)
	return f 

def findsCssSelector(driver, css):
	f = driver.find_elements_by_css_Selector(css)
	return f