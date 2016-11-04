def fact(number):
    if number<=1:
        return 1
    else:
        return number*fact(number-1)

print(fact(int(input("enter a no.:"))))

def explode(word):
    if len(word) <= 1 :
        return word
    else:
        return word[0] + ' ' + explode(word[1:])

#print(explode(input("enter a word3")))

def remdup(word):
    if len(word)<=1:
        return word
    elif word[0] == word[1]:
        return remdup(word[1:])
    else:
        return word[0] + remdup(word[1:])

print(remdup("aabbccddeeffgghhiijjkkllmmnnoopp"))