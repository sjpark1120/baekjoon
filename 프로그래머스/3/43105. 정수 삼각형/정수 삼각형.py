def solution(triangle):
    triangle_dp = []
    for row in triangle:
        row_dp = []
        for j in range(len(row)):
            if len(row) == 1:
                row_dp.append(row[j])
            elif j == 0:
                row_dp.append(triangle_dp[-1][j] + row[j])
            elif  j == len(row)-1:
                row_dp.append(triangle_dp[-1][j-1]+ row[j])
            else:
                row_dp.append(max(triangle_dp[-1][j-1], triangle_dp[-1][j])+ row[j])
        triangle_dp.append(row_dp)
    return max(triangle_dp[-1])