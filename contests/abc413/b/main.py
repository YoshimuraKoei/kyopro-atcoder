import sys

N = int(sys.stdin.readline())
S = sys.stdin.read().split()

ans_set = set()
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            ans_set.add(S[i] + S[j])

print(len(ans_set))
