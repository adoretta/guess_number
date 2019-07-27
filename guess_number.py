import random
start = int(input('請決定隨機數字開始值: '))
end = int(input('請決定隨機數字結束值: '))
r =random.randint(start, end)
count = 0
while True:
	count += 1
	number = int(input('請輸入數字: '))
	if number == r:
		print('終於猜對了')
		print('這是你猜的第', count, '次')
		break
	elif number > r :
		print('比答案大')
	elif number < r :
		print('比答案小')
	print('這是你猜的第', count, '次')