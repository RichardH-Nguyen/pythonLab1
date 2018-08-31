userString = input("Input text here!")
userSplit = userString.split(" ")
finalString = ""
low = ""
splitLength = len(userSplit)
for y in userSplit:
    low = y.lower()
    upperFirst = low.replace(low[0], low[0].upper())
    finalString += upperFirst

finalString = finalString.replace(finalString[0], finalString[0].lower())
print(finalString)