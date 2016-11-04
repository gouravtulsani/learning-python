import re
for i in range int(raw_input()):
	number = raw_input()
	ph= re.compile("[7-9]\d{9}")
	if len(number)==10 and ph.match(number):
		print "yes"
	else:
		print "no"