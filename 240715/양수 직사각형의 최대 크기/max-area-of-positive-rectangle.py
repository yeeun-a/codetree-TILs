import sys
r=sys.stdin.readline

n,m=map(int,r().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,r().split())))

ans=-1
for y in range(n):
    for x in range(m):
        for h in range(1, n+1):
            if y+h-1>=n: break
            for w in range(1, m+1):
                if x+w-1>=m: break
                flag = 1
                for i in range(h):
                    for j in range(w):
                        if graph[y+i][x+j] <= 0:
                            flag = 0
                            break
                    if not flag:
                        break
                if flag:
                    ans = max(ans, w*h)
print(ans)