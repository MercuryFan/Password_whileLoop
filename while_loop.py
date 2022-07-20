#密碼重設程式
#先在程式碼中 password 等於 a123456
#讓使用者最多輸入三次密碼，不對的話就印出密碼錯誤!還有 _ 次機會
#對的話就印出 登入成功

password = "a123456"
i = 3
while i > 0:
	i = i-1
	pwd = input('請輸入您的密碼:')
	if pwd == password:
		print("登入成功!")
		break #逃出迴圈
	else:
		print('密碼輸入錯誤')
		if i > 0:
			print('還有', i, '次機會!')
		else:
			print('沒有機會了唷! 要鎖帳號了拉!')
	

