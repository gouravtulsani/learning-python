def square(num):
    return num*num
def vowels(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        if string[i] =="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u" :
           count=count+1
    return count

def ctof(temp):
    return temp*(9/5)+32
def ftoc(temp):
    return (temp-32)*(5/9)
def convert(temp,toscale):
    if toscale.lower() == "c":
        return ftoc(temp)
    else:
        return ctof(temp)
temp = int(raw_input("enter the temp: "))
scale = raw_input("enter the scale to convart: ")
contemp = convert(temp,scale)
print temp," convarted temp ",  contemp,scale