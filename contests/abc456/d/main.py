S = input()
MOD = 998244353

n = len(S)
DP = [0] * n
DP[0] = 1

dp = {"a": 0, "b": 0, "c": 0}

for char in S:
    if char == "a":
        dp[char] += 1 + dp["b"] + dp["c"]
    elif char == "b":
        dp[char] += 1 + dp["c"] + dp["a"]
    else:
        dp[char] += 1 + dp["a"] + dp["b"]

print((dp["a"] + dp["b"] + dp["c"]) % MOD)

