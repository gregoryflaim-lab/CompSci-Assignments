name = int(input("what year is it?"))

if name % 400 == 0:
	print("leap year")
elif name % 100 == 0:
	print("not a leap year")
elif name % 4 == 0:
	print("leap year")
else:
	print("not a leap year")



