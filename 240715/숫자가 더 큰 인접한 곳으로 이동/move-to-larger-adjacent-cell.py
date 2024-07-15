import sys
r=sys.stdin.readline

n,y,x=map(int,r().split())
graph=[]    
for _ in range(n):
    graph.append(list(map(int,r().split())))
y-=1
x-=1
dx=[0,0,-1,1]
dy=[-1,1,0,0]
while 1:
    last_y, last_x = y,x
    print(graph[y][x], end=' ')
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not (0 <= ny < n and 0 <= nx < n): continue
        if graph[y][x] >= graph[ny][nx]: continue
        y = ny
        x = nx
        break
    if y == last_y and x == last_x:
        break