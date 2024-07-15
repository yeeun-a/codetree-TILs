import sys
r=sys.stdin.readline

n=int(r())
graph=[]
for _ in range(n):
    graph.append(list(map(int,r().split())))

ans=0
for i in range(n-2):
    for j in range(n-2):
        res=0
        for p in range(3):
            for q in range(3):
                if graph[i+p][j+q]==1: res+=1
        ans = max(res, ans)
print(ans)