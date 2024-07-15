import sys
r=sys.stdin.readline

n=int(r())
arr=[]
for _ in range(n):
    arr.append(int(r()))

s1, e1 = map(int,r().split())
s1-=1; e1-=1
s2, e2 = map(int,r().split())
s2-=1; e2-=1


last_idx = n-1
tmp = 0
for i in range(e1+1, last_idx+1):
    arr[s1+tmp] = arr[i]
    tmp+=1
last_idx = s1+tmp-1

tmp = 0
for i in range(e2+1, last_idx+1):
    arr[s2+tmp] = arr[i]
    tmp+=1
last_idx = s2+tmp-1

print(last_idx+1)
print(*arr[:last_idx+1], sep='\n')