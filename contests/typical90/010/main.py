N = int(input())

C = []
P = []
arr1 = [0] * (N+1)
arr2 = [0] * (N+1)
sum1 = 0
sum2 = 0
for i in range(1, N+1):
    Ci, Pi = map(int, input().split())
    C.append(Ci)
    P.append(Pi)
    if Ci == 1:
        sum1 += Pi
        arr1[i] = sum1
        arr2[i] = sum2
    else:
        sum2 += Pi
        arr1[i] = sum1
        arr2[i] = sum2

Q = int(input())
for i in range(Q):
    Li, Ri = map(int, input().split())
    A = arr1[Ri] - arr1[Li-1]
    B = arr2[Ri] - arr2[Li-1]
    print(A, B)
  
