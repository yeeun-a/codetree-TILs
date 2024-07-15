import sys
r=sys.stdin.readline

n,m=map(int,r().split())
a=[]
for _ in range(n):
    a.append(int(r()))

end = n-1
while 1:
    last_num = 0
    last_idx = -1
    cnt = 0
    flag = 0
    pre = end
    for i in range(len(a)):
        e = a[i]
        if flag:
            a[last_idx]=e
            if i == end:
                end = last_idx
            last_idx+=1
            continue
        if e == last_num:
            cnt += 1
        else:
            last_num = e
            cnt = 1
            last_idx = i
        if cnt >= m:
            flag=1
    if pre == end:
        break
print(end+1)
print(*a[:end+1], sep='\n')