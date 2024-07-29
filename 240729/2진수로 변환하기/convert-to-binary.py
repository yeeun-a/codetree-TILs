# 변수 선언 및 입력
n = int(input())
digits = []

# 이진수로 변환합니다.
while True:
    if n < 2:
        digits.append(n)
        break

    digits.append(n % 2)
    n //= 2

# 이진수를 출력 합니다.
# 뒤집은 다음에 출력해야 함에 유의합니다.
for digit in digits[::-1]:
    print(digit, end="")