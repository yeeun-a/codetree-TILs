# 변수 선언 및 입력
binary = list(map(int, list(input())))
length = len(binary)

# 십진수로 변환합니다.
num = 0
for i in range(length):
    num = num * 2 + binary[i]

# 십진수에 17을 곱합니다.
num *= 17

digits = []

# 이진수로 변환합니다.
while True:
    if num < 2:
        digits.append(num)
        break

    digits.append(num % 2)
    num //= 2

# 이진수를 출력 합니다.
# 뒤집은 다음에 출력해야 함에 유의합니다.
for digit in digits[::-1]:
    print(digit, end="")