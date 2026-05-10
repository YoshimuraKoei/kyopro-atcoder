import sys
from itertools import product

data = list(map(int, sys.stdin.read().split()))
H = data[0]
W = data[1]

A = []
idx = 2

row_sum = []
column_sum = [0] * W
for i in range(H):
    row = data[idx:idx+W]
    A.append(row)
    idx += W 
    row_sum.append(sum(row))
    for j in range(W):
        column_sum[j] += row[j]


ans_matrix = [ [0] * W for _ in range(H)] 
for i, j in product(range(H), range(W)):
    ans_matrix[i][j] += row_sum[i] + column_sum[j] - A[i][j]

for i in range(H):
    print(*ans_matrix[i])

    
