from datetime import datetime, timedelta

def count_specific_weekday(m1, d1, m2, d2, A):
    # 요일 문자열과 숫자 매핑
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    # 시작 날짜와 끝 날짜 설정
    start_date = datetime(2024, m1, d1)
    end_date = datetime(2024, m2, d2)
    
    # 목표 요일을 숫자로 변환
    target_weekday = days_of_week.index(A)
    
    # 날짜 순회하면서 목표 요일의 개수 세기
    current_date = start_date
    count = 0
    
    while current_date <= end_date:
        if current_date.weekday() == target_weekday:
            count += 1
        current_date += timedelta(days=1)
    
    return count

# 입력 받기
m1, d1, m2, d2 = map(int, input().strip().split())
A = input().strip()

# 결과 계산
result = count_specific_weekday(m1, d1, m2, d2, A)

# 결과 출력
print(result)