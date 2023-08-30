list_x = [0] * 4
list_y = [0] * 4
for i in range(3):
    list_x[i], list_y[i] = map(int, input().split())

if list_x[0] == list_x[1]:
    list_x[3] = list_x[2]
elif list_x[0] == list_x[2]:
    list_x[3] = list_x[1]
else:
    list_x[3] = list_x[0]

if list_y[0] == list_y[1]:
    list_y[3] = list_y[2]
elif list_y[0] == list_y[2]:
    list_y[3] = list_y[1]
else:
    list_y[3] = list_y[0]

print("{} {}".format(list_x[3], list_y[3]))