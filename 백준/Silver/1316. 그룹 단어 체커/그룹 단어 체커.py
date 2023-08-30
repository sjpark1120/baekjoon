n = int(input())
gruopword = 0
for i in range(n):
    word = input()
    word = list(word)
    ap = [0] * 26
    nogw = 0
    for j in range(len(word)):
        if ap[ord(word[j])-97] > 0 and word[j-1] != word[j]:
            nogw = 1
        ap[ord(word[j]) - 97] += 1
    if nogw == 0:
        gruopword += 1
print(gruopword)