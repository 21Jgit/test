#main.py

from random import randint as r

a = r(1, 10)
g = input("Enter an int from 1 to 10")

while g != a:
	g = input("Enter an int from 1 to 10")

print("YOU DID IT!!!")
