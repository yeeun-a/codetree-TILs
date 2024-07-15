import sys
r=sys.stdin.readline

n,m=map(int,r().split())
a=[]
for _ in range(n):
    a.append(int(r()))

end = n
for _ in range(n):
    last_idx = 0
    last_num = -1
    cnt = 0
    for i in range(end):
        if last_num == a[i]:
            cnt += 1
        else:
            last_num = a[i]
            last_idx = i
            cnt = 1
        if cnt == m:
            for k in range(last_idx, i+1):
                a[k] = 0
        elif cnt > m:
            a[i] = 0
    tmp = -1
    for i in range(end):
        if a[i] == 0:
            if tmp == -1: tmp = i
        elif tmp != -1:
            a[tmp] = a[i]
            a[i] = 0
            tmp += 1
    if tmp == -1: break
    end = tmp
        
print(end)
print(*a[:end], sep='\n')