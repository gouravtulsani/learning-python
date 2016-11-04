def square(number):
    return number*number
num = 2
sqnum = square(num)
print(sqnum)
sqnumber = square
sqnum = sqnumber(4)
print(sqnum)

numbers = [1,2,3,4,5]
numbersq = list(map(square,numbers))
print(numbersq)

gurav = lambda x,y :x*y
print(gurav(3,6))

gourav = lambda w : w**w
print(gourav(5))
