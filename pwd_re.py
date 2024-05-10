password = 'a123456'
count = 0
while count < 3:
	in_pwd = input('請輸入您的密碼: ')
	if in_pwd == password:
		print('登入成功')
		break

	else:
		count = count + 1
		print('密碼錯誤! 還有', (3-count), '次機會')	