import sys
r=sys.stdin.readline

n,t=map(int,r().split())
a=list(map(int,r().split()))
b=list(map(int,r().split()))

for i in range(t):
    a_last = a[-1]
    b_last = b[-1]
    
    for i in range(n-1, -1, -1):
        a[i] = a[i-1]
        b[i] = b[i-1]

    b[0] = a_last
    a[0]  = b_last

print(*a)
print(*b)