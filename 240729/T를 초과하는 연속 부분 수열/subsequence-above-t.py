def max_subsequence_length(arr, t):
    max_length = 0
    current_length = 0
    
    for num in arr:
        if num > t:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
    
    # 마지막 부분 수열 체크
    if current_length > max_length:
        max_length = current_length
    
    return max_length

# 입력 받기
n, t = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

# 결과 계산
result = max_subsequence_length(arr, t)

# 결과 출력
print(result)