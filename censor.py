def censor(text,word):
    x = len(word)
    a = "*" * len(word)
    texta = text.split(" ")
    for items in texta:
        if items == word:
            items = a
        return items,

print censor("hey!! , this is gourav","gourav")
