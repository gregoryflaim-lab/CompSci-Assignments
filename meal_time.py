time = input("what's the time?")
def convert(x):
	x, y = x.split(":")
	x = float(x)
	y = float(y)
	y = (y / 60)
	x = (x + y)
	if x >= 7 and x <= 8:
		print("breakfast time")
	elif x >= 12 and x <= 13:
		print("lunch time")
	elif x >= 18 and x <= 19:
		print("dinner time")
	else:
		print("not meal time")
convert(time)

