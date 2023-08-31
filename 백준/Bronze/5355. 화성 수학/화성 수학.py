t = int(input())
for i in range(t):
    case = list(input().split())
    anwser = 0
    for j in case:
        if(j == case[0]):
            anwser += float(j)
        elif(j == "@"):
            anwser *= 3
        elif(j == "%"):
            anwser += 5
        elif(j == "#"):
            anwser -= 7
    print("{:.2f}".format(anwser))