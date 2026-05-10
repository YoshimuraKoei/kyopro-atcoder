N = int(input())

A = []
for n in range(N):
  data = list(map(int, input().split()))
  Li = data[0]
  A.append(data[1:])

X, Y = map(int, input().split())
print(A[X-1][Y-1])
