S = input()
MOD = 998244353

ans = 0
lg = 0
for i, char in enumerate(S):
    if i > 0 and S[i - 1] == char:
        lg = 1
    else:
        lg += 1

    ans += lg

print(ans % MOD)
