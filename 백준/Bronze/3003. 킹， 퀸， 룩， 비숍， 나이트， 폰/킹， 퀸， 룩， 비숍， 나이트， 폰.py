king, queen, rook, bishop, knight, pawn = map(int, input().split())
print("{} {} {} {} {} {}".format(1-king, 1-queen, 2-rook, 2-bishop, 2-knight, 8-pawn))