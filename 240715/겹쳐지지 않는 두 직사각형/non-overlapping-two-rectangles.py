import sys
r=sys.stdin.readline

n,m=map(int,r().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,r().split())))

def inRange(y, x):
    return 0 <= y < n and 0 <= x < m

def getRectangle(y, x, height, width):
    res=set()
    for i in range(height):
        for j in range(width):
            res.add((y+i, x+j))
    return res

ans = -1000*n*m
for y1 in range(n):
    for x1 in range(m):

        for h1 in range(1, n+1):
            for w1 in range(1, m+1):
                if not inRange(y1+h1-1, x1+w1-1): break
                res =  getRectangle(y1, x1, h1, w1)

                for y2 in range(n):
                    for x2 in range(m):
                        for h2 in range(1, n+1):
                            for w2 in range(1, m+1):
                                if not inRange(y2+h2-1, x2+w2-1): break
                                res2 = getRectangle(y2, x2, h2, w2)
                                if len(res | res2) == len(res) + len(res2):
                                    result = 0
                                    for y, x in res | res2:
                                        result += graph[y][x]
                                    ans = max(ans, result)
print(ans)