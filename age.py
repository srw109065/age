driving = input("請問你有開過車嗎? ")
if driving != "有" and driving != "沒有":
	print("只能回答有或者沒有")
	raise SystemExit
age = input("請問您的年齡? ")
age = int(age)

if driving == "有":
	if age >= 18:
		print("謝謝您，合法開車!")
	else:
		print("奇怪，為什麼你會開車呢?! ")
elif driving == "沒有":
	if age >= 18:
		print("你可以去考駕照囉 ")
	else:
		print("再過幾年就可以考駕照了! ")
