import random

secret = random.randint(1,100)
x = 0
y = 0

print("Ahoy! I have a secret!")
while x != secret and y < 6:
	x = int(input("What's your guess"))
	if x < secret:
		print ("too low!")
	elif x > secret:
		print ("too high!")
	y = y + 1

if x == secret:
	print ("You are right!")
else:
	print ("Better luck next time!")
	print ("the secret number was", secret)
	
