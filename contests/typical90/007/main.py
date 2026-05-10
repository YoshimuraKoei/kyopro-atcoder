N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())

for q in range(Q):
    B_i = int(input())
    left = -1
    right = N
    mid = (left + right) // 2
    while right - left > 1:
        mid = (left + right) // 2
        if B_i >= A[mid]:
            left = mid
        else:
            right = mid
    
    arr = []
    if left >= 0:
        arr.append(abs(A[left] - B_i))
    if right < N:
        arr.append(abs(A[right] - B_i))

    print(min(arr))
