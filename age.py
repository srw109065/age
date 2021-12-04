drive = input("你有沒有開過車: ")

if drive == "有":
	age = input("請問你的年齡: ")
	if int(age) < 18:
		print("你怎麼會開過車")
	else:
		print("你合格了")
elif drive == "沒有":
	age = input("請問你的年齡: ")
	if int(age) < 18:
		print("等妳長大了，再去考駕照")
	else:
		print("你可以考駕照囉")
else:
	print("只能輸日 有 or 沒有")