import random
capsletter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallleter="abcdefghijklmnopqrstuvwxyz"
number="1234567890"
specialchar="!@#$%^&*"
pass_generated=[]
pass_generated.append(random.choice(capsletter))
pass_generated.append(random.choice(smallleter))
pass_generated.append(random.choice(specialchar))
pass_generated.append(random.choice(number))

all_letters=list(capsletter)+list(smallleter)+list(number)+list(specialchar)

#should be greter than 4
lenpasswd = int(input("Enter length of the password(min length is 4): "))
if lenpasswd > 4:
	for i in range(4,lenpasswd):
		pass_generated.append(random.choice(all_letters))

password = ''.join(str(x) for x in pass_generated)
print(password)