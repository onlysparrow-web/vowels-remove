name = input("Enter The Text")
length = len(name)
noVow = []
vow = []
b = ""
vowels = ["a", "e", "i", "o", "u", " "]
for x in range(length):
    if (name[x] not in vowels):
        noVow.append(name[x])
    else:
        vow.append(name[x])


print(b)
print(noVow)
print(vow)
