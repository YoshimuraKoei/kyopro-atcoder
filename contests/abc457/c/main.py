N, K = map(int, input().split())

A = []
L = []
B = []
for n in range(N):
  data = list(map(int, input().split()))
  Li = data[0]
  Ai = data[1:]
  L.append(Li)
  A.append(Ai)

C = list(map(int, input().split()))

idx = 0
s = 0
while K > s:
  plus = L[idx] * C[idx]
  if K <= s + plus:
    break
  idx += 1
  s += plus

res = (K-1-s) % L[idx]
ans = A[idx][res]
print(ans)
