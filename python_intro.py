print("Hello, Django ladee!")

if 5 > 2:
	print("5 IS greater than 2")
else:
	print("5 is not greater than 2")

name = "jonell"

if name == "jamil":
	print("Hey jamil")
elif name == "Nick":
	print("Hey nick")
elif name == "Ben":
	print("Hey ben")
elif name == "jonell":
	print("You're Awesome!")
else:
	print("Hey anonymous!")

def hi(name):
	# if name == 'Jonell':
	# 	print("hi Jonell")
	# elif name == "Jamil":
	# 	print("hi Jamil")
	# else:
	# 	print("Hi annoymous")
	print("Hi " + name +"!") 



girls = ['jonell', 'rachel', 'you', 'misty', 'kristen']

for name in girls:
	hi(name)
	print('Next girl')

for i in range(1, 6):
	print(i)

