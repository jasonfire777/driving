country = input('請輸入國藉：')
age = input('請輸入年齡：')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照了')
	else:
		print('你還不能考駕照哦')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照了')
	else:
		print('你還不能考駕照哦')
else:
	print('你只能輸入台灣/美國')