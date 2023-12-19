import sys
# sys.stdin = open("6.다이나믹프로그래밍/input.txt")

n = int(sys.stdin.readline())

dp = [0] * (1000001)
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    if i % 3==0:
        if i%2==0:
            dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
        else:
            dp[i] = min(dp[i//3], dp[i-1]) +1
    elif i % 2==0: 
        dp[i] = min(dp[i//2], dp[i-1]) +1
    else :
        dp[i] = dp[i-1] +1
print(dp[n])