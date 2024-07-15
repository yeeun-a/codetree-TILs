import sys
r=sys.stdin.readline

n,m=map(int,r().split())
a=[]
for _ in range(n):
    a.append(int(r()))

end = n
for _ in range(n):
    last_idx = 0
    cnt = 0
    flag = 0
    for i in range(end):
        if a[last_idx] == a[i]:
            cnt += 1
        else:
            if cnt >= m:
                for j in range(i, end):
                    a[last_idx] = a[j]
                    last_idx+=1
                end = last_idx
                flag = 1
                cnt = 0
                break
            last_idx = i
            cnt = 1
    if cnt >= m:
        end = last_idx
    if not flag: break
            
print(end)
print(*a[:end], sep='\n')