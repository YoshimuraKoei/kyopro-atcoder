N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(X): # 最小値をX以上にできるか
  counter = 0
  for i, a in enumerate(A):
    if a < X:
      add = i + 1
      counter += (X - a + add - 1) // add
      
      if counter > K:
        return False
  
  return counter <= K

left = min(A) - 1
right = 10 ** 24
while right - left > 1:
  mid = (left + right) // 2
  if check(mid):
    left = mid
  else:
    right = mid
    
print(left)
