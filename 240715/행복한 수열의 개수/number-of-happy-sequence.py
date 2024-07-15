import sys
r=sys.stdin.readline

n,m=map(int,r().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,r().split())))

ans=0
for i in range(n):
    last_num=-1
    res=0
    for j in range(n):
        if last_num==graph[i][j]:
            res+=1
        else:
            res=1
            last_num=graph[i][j]
        if res >= m:
            ans+=1
            break

for i in range(n):
    last_num=-1
    res=0
    for j in range(n):
        if last_num==graph[j][i]:
            res+=1
        else:
            res=1
            last_num=graph[j][i]
        if res >= m:
            ans+=1
            break
print(ans)