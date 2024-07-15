import sys
r=sys.stdin.readline

n,m=map(int,r().split())

shape = [
    [(0,0), (1,0), (1,1)],
    [(0,1), (1,0), (1,1)],
    [(0,0), (0,1), (1,1)],
    [(0,0), (1,0), (0,1)],
    [(0,0), (1,0), (2,0)],
    [(0,0), (0,1), (0,2)],
]

graph=[]
for _ in range(n):
    graph.append(list(map(int,r().split())))

ans = 0
for i in range(n):
    for j in range(n):
        for cord in shape:
            flag = 1
            res = 0
            for y, x in cord:
                if i+y >= n or j+x >= m:
                    flag = 0
                    break
                res += graph[i+y][j+x]
            if not flag:
                continue
            ans = max(ans, res)
print(ans)