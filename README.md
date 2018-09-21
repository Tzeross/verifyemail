# verifyemail Python3.6.5

Python在线验证邮箱真实性，支持批量验证，支持全部域名邮箱，支持全部域名邮箱，支持全部域名邮箱，支持全部域名邮箱


final_list = verify_istrue(['190758586@qq.com', '19075858666@qq.com'])  
print(final_list)  #{'190758586@qq.com': True, '19075858666@qq.com': False}  
    

#2018-09-21 18:42:35,017 - verifyemail.py [line:23] - INFO: 正在查找邮箱服务器  
#2018-09-21 18:42:35,030 - verifyemail.py [line:26] - INFO: 查找结果为：['mx3.qq.com', 'mx2.qq.com', 'mx1.qq.com']  
#2018-09-21 18:42:35,030 - verifyemail.py [line:52] - INFO: 正在连接服务器...：mx2.qq.com  
#2018-09-21 18:42:35,160 - verifyemail.py [line:56] - DEBUG: (250, b'newmx33.qq.com')  
#2018-09-21 18:42:35,218 - verifyemail.py [line:59] - DEBUG: (250, b'Ok')  
#2018-09-21 18:42:35,317 - verifyemail.py [line:62] - DEBUG: (250, b'Ok')  
#2018-09-21 18:42:35,357 - verifyemail.py [line:56] - DEBUG: (250, b'newmx33.qq.com')  
#2018-09-21 18:42:35,418 - verifyemail.py [line:59] - DEBUG: (250, b'Ok')  
#2018-09-21 18:42:35,460 - verifyemail.py [line:62] - DEBUG: (550, b'Mailbox not found. http://service.mail.qq.com/cgi-#bin/help?subtype=1&&id=20022&&no=1000728')  
