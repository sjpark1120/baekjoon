x, y, w, h =map(int, input().split())
shortway = x
if shortway > w-x:
    shortway = w-x
if shortway > y:
    shortway = y
if shortway > h- y:
    shortway =h -y
print(shortway)