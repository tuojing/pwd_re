password = 'a123456'
count = 0
while count < 3:
	count = count + 1
	in_pwd = input('請輸入您的密碼: ')
	if in_pwd == password:
		print('登入成功')
		break

	else:
		print('密碼錯誤!') 
		if (3-count) > 0 :
			print('還有', (3-count), '次機會')
		else:
			print('沒機會嘗試了! 要鎖帳號了啦!')	