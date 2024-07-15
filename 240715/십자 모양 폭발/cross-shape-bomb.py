import sys
r=sys.stdin.readline

n=int(r())
graph=[]
for _ in range(n):
    graph.append(list(map(int,r().split())))
p,q=map(int, r().split())
p-=1; q-=1

bomb = graph[p][q]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for i in range(4):
    for j in range(bomb):
        ny = p + dy[i]*j
        nx = q + dx[i]*j
        if not (0 <= ny < n and 0 <= nx < n): break
        graph[ny][nx] = 0

for x in range(n):
    tmp = -1
    for y in range(n):
        if graph[n-1-y][x] == 0:
            if tmp == -1: tmp = n-1-y
        else:
            if tmp == -1: continue
            graph[tmp][x] = graph[n-1-y][x]
            graph[n-1-y][x] = 0
            tmp -= 1

for e in graph:
    print(*e)