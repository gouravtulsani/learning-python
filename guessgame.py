import random

while True:
	num = random.randint(1, 50)
	count = 0
	user = int(raw_input("Guess a no. from 1-50: "))
	while True:
		
		if num > user:
			print("you are wrong")
			user = int(raw_input("Guess Larger no."))
			count +=1
		elif num < user:
			print("you are wrong")
			user = int(raw_input("Guess Smaller no."))
			count +=1
		else:
			print("Correct Guess " + str(count) +" attempts")
			break
	again = str(raw_input("wanna play again (y/n): "))
	if again == "n":
		break