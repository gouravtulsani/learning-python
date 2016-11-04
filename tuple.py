import os
"""numbers = int(raw_input("enter the no."))
sum = 0
for i in range(1,numbers):
    sum = sum + i
    print sum

no = int(raw_input("enter a no."))
value = 1
for i in range(1,no):
    value=value*no
    no=no-1
print value """

grades = {'grv':'100','sam':'55','ram':86,'babu':'75'}
"""for key in grades.keys():
    print grades.keys()
    print grades.values()"""

files = os.popen('touch /home/grv/programs/python/mygrv.txt')
file = open('mygrv.txt','r+')


v= 'my name is khan and i am not a terrorist'
a=v.split(' ')
print v.upper()
print v.lower()
print a
for letter in a:
    touple=[(letter,len(letter))]
    print touple