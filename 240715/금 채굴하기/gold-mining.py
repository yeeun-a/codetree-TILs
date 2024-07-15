import sys
r=sys.stdin.readline

n,m=map(int,r().split())
coin=[]
for y in range(n):
    temp = list(map(int,r().split()))
    for x in range(n):
        if temp[x] == 1:
            coin.append((y,x))

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n+1):
            cost = 0
            cost -= k*k + (k+1)*(k+1)
            res = 0
            for y,x in coin:
                if abs(y-i) + abs(x-j) <= k:
                    cost += m
                    res += 1
            if cost >= 0:
                ans = max(ans, res)
print(ans)