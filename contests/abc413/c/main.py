from collections import deque

Q = int(input())

A = deque()
for q in range(Q):
    query = input().split()
    if query[0] == "1":
        c = int(query[1])
        x = int(query[2])
        A.append((c, x))

    else:
        k = int(query[1])
        ans = 0

        while k > 0:
            c, x = A.popleft()
            if k >= c:
                ans += c * x
                k -= c
            else:
                ans += k * x
                A.appendleft((c-k, x))
                k = 0
        print(ans)
