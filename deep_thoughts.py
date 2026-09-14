name = input("what is the answer to the ultimate question of life, the universe, and anything?")

if "-" in name:
	name = name.replace("-", "")

name = name.strip()
name = name.lower()

if name == "fortytwo":
	name = name.replace("fortytwo", "42")


if name == "42":
	print("yes")
else:
	print("no")
