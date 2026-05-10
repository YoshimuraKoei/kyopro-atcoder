A_1 = list(map(int, input().split()))
A_2 = list(map(int, input().split()))
A_3 = list(map(int, input().split()))

count = 0
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            syugo = set()
            syugo.update([A_1[i-1], A_2[j-1], A_3[k-1]])
            if syugo == {4, 5, 6}:
                count += 1

print(round(count / 216, 10))
