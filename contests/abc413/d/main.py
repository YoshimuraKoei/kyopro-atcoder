import sys

input = sys.stdin.readline

T = int(input())

idx = 0
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    ans = "Yes"

    A_ord = sorted(A, key=abs)
    if len(set(abs(i) for i in A_ord)) == 1:
        num_p = sum(1 for i in A if i > 0)
        num_f = sum(1 for i in A if i < 0)
        if num_p == 0 or num_f == 0:
            ans = "Yes"
        elif abs(num_p - num_f) <= 1:
            ans = "Yes"
        else:
            ans = "No"
    else:
        for i in range(1, N-1):
            if A_ord[i+1] * A_ord[0] != A_ord[i] * A_ord[1]:
                ans = "No"
                break

    print(ans)
