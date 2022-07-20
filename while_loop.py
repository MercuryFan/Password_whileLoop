#密碼重設程式
#先在程式碼中 password 等於 a123456
#讓使用者最多輸入三次密碼，不對的話就印出密碼錯誤!還有 _ 次機會
#對的話就印出 登入成功

password = "a123456"
i = 3
while i>0:
	pwd = input('請輸入您的密碼:')
	if pwd == password:
		print("登入成功!")
		break
	else:
		i = i-1
		print('密碼輸入錯誤,還有', i, "次機會")
		if i == 0:
			break
	

