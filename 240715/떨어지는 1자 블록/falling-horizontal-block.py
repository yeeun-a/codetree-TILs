import sys
r=sys.stdin.readline

n,m,k=map(int,r().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,r().split())))

k-=1
y=0
while 1:
    flag = 1
    y+=1
    if y >= n: break
    for x in range(m):
        if graph[y][k+x] == 1:
            flag = 0
            break
    if not flag:
        break
for x in range(m):
    graph[y-1][k+x] = 1
for e in graph:
    print(*e)