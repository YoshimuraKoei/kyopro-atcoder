K = int(input())

counter = 0
for i in range(1, round(K**(1/3)) + 1):
    if K % i == 0:
        a = i
        bc = K // i
        for j in range(a, round(bc**(1/2)) + 1):
            if bc % j == 0:
                b = j
                c = bc // j
                counter += 1

print(counter)

