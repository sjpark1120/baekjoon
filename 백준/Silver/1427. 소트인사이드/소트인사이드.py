n = input()
list_n = list(n)
list_n.sort(reverse=True)
for i in range(len(list_n)):
    print(list_n[i], end='')