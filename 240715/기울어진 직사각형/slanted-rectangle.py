import sys
r=sys.stdin.readline

n=int(r())
graph=[]
for _ in range(n):
    graph.append(list(map(int,r().split())))

def inRange(y,x):
    return 0 <= y < n and 0 <= x < n

ans = 0
for y in range(n):
    for x in range(n):

        res1 = 0
        for n1 in range(1,n+1):
            i1 = y - n1
            j1 = x + n1
            if not inRange(i1, j1): break
            res1 += graph[i1][j1]

            res2 = 0
            for n2 in range(1,n+1):
                i2 = i1 - n2
                j2 = j1 - n2
                if not inRange(i2, j2): break
                res2 += graph[i2][j2]
                
                flag = 1
                res3 = 0
                for n3 in range(1, n1+1):
                    i3 = i2 + n3
                    j3 = j2 - n3
                    if not inRange(i3, j3): 
                        flag = 0
                        break
                    res3 += graph[i3][j3]
                if not flag: continue

                res4 = 0
                for n4 in range(1, n2+1):
                    i4 = i3 + n4
                    j4 = j3 + n4
                    if not inRange(i4, j4): 
                        flag = 0
                        break
                    res4 += graph[i4][j4]

                if not flag: continue
                ans = max(ans, res1+res2+res3+res4)
print(ans)