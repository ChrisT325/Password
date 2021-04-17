i = 3
while True: 
	i = i - 1
	password = input('請輸入密碼:')
	if password == 'a123456':
		print('登入成功!')
		break
	else:
		if i == 0:
			print('帳號已鎖定!')
			break
		else:
			print('密碼錯誤!你還有',i,'次機會')
		

