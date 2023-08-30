mo = [ 'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
while True:
    a = input()
    x = 0
    if a == "#":
        break
    for i in a:
        if i in mo:
            x += 1
    print(x)