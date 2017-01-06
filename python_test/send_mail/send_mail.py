
# -*- coding: utf-8 -*-  
import smtplib, os.path, mimetypes
import email.MIMEMultipart, email.MIMEText, email.MIMEBase
def send_mail(file_name):

	# 构造MIMEMultipart对象做为根容器  
	main_msg = email.MIMEMultipart.MIMEMultipart() 

	# 设置根容器属性 
	From = "a136332462@126.com"  
	To = "136332462@qq.com"  
	main_msg['From'] = From  
	main_msg['To'] = To  
	main_msg['Subject'] = u"自动化测试报告"  
	main_msg['Date'] = email.Utils.formatdate( )  
	server = smtplib.SMTP("smtp.126.com")  
	server.login("a136332462@126.com","meilei99") #仅smtp服务器需要验证时  
	  	  
	# 构造MIMEText对象做为邮件显示内容并附加到根容器  
	#定义正文
	f = open(file_name, 'rb')
	mail_body = f.read()
	f.close()
	text_msg=email.MIMEText.MIMEText(mail_body,_subtype='html',_charset='utf-8') 
	main_msg.attach(text_msg)  
	  
	# 构造MIMEBase对象做为文件附件内容并附加到根容器  
	  
	# 读入文件内容并格式化
	data = open(file_name, 'rb')  
	ctype,encoding = mimetypes.guess_type(file_name)  
	if ctype is None or encoding is not None:  
	    ctype = 'application/octet-stream'  
	maintype,subtype = ctype.split('/',1)  
	file_msg = email.MIMEBase.MIMEBase(maintype, subtype)  
	file_msg.set_payload(data.read())  
	data.close( )  
	email.Encoders.encode_base64(file_msg)#把附件编码  
	 
	# 设置附件头  
	basename = os.path.basename(file_name)  
	file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头  
	main_msg.attach(file_msg)  
	  
	# 得到格式化后的完整文本  
	fullText = main_msg.as_string( )  
	  
	# 用smtp发送邮件  
	server.sendmail(From, To, fullText)
