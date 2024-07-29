# 변수 선언 및 입력
a, b, c, d = tuple(map(int, input().split()))

# 출력
print((c * 60 + d) - (a * 60 + b))