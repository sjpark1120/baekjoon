word =input()
fr = [0]*26
word = word.lower()
wordlist = list(word)
for i in range(len(word)):
    fr[(ord(wordlist[i]))-97] += 1
bignum = 0
bignumindex = 0
a = 0
for i in range(26):
    if bignum < fr[i]:
        bignum = fr[i]
        bignumindex = i
for i in range(26):
    if i != bignumindex and bignum == fr[i]:
        a = 1
        print("?")
        break
if a==0:
    print(chr(bignumindex+65))
