name = float(input("what's the temperature?"))

if 140 > name >= 60:
	print("you don't need a sweater")
elif name < 60:
	print("you need a sweater")

else:
	print("Invalid input")
