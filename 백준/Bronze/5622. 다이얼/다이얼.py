word = input()
word = list(word)
a = 0
for i in range(len(word)):
    if word[i] <= 'C':
        a += 3
    elif word[i] <= 'F':
        a += 4
    elif word[i] <= 'I':
        a += 5
    elif word[i] <= 'L':
        a += 6
    elif word[i] <= 'O':
        a += 7
    elif word[i] <= 'S':
        a += 8
    elif word[i] <= 'V':
        a += 9
    elif word[i] <= 'Z':
        a += 10
print(a)