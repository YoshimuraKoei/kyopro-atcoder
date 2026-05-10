H, W = map(int, input().split())
S = []
for i in range(H):
    Si = input().split()
    S.append(Si)

counter = 0
for h1 in range(1, H+1):
    for h2 in range(1, H+1):
        for w1 in range(1, W+1):
            for w2 in range(1, W+1):
                flg = False
                dummy1 = 0
                dummy2 = 0
                for i in range(h1, h2+1):
                    for j in range(w1, w2+1):
                        dummy1 += 1
                        if 0 <= h1+h2-i-1 <= H-1 and 0 <= w1+w2-j-1 <= W-1:
                            mass1 = S[i-1][0][j-1]
                            mass2 = S[h1+h2-i-1][0][w1+w2-j-1]
                            if mass1 == mass2:
                                dummy2 += 1
                if dummy1 == dummy2 and dummy1 != 0:
                    counter += 1
print(counter)
