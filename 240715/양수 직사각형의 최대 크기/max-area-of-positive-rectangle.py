import sys
r=sys.stdin.readline

n,m=map(int,r().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,r().split())))

ans=-1
for y in range(n):
    for x in range(m):
        for h in range(n):
            if y+h >= n: break
            flag = 1
            for w in range(m):
                if w+x >= m: break
                if graph[y+h][x+w] < 0: 
                    flag = 0
                    break
            if flag:
                ans = max(ans, (w+1)*(h+1))
print(ans)