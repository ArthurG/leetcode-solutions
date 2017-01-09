def findTheDifference(s, t):
    newLetters = {}
    for letter in t:
        newLetters[letter] = newLetters.get(letter, 0) + 1
    for letter in s:
        newLetters[letter] = newLetters.get(letter, 0) - 1
    for letter in newLetters:
        if newLetters[letter]:
            return str(letter)

print(findTheDifference("a", "aa")) #a
print(findTheDifference("aa", "aba")) #b
print(findTheDifference("", "b")) #b

