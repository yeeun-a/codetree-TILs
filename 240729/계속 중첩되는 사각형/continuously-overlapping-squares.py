def calculate_blue_area(n, rectangles):
    # 격자 크기를 설정합니다.
    offset = 100  # -100 ~ 100 의 좌표를 0 ~ 200 으로 이동
    grid_size = 201  # -100 ~ 100 을 포함하는 전체 크기
    
    # 격자 초기화
    grid = [[0] * grid_size for _ in range(grid_size)]
    
    # 직사각형 처리
    for i, (x1, y1, x2, y2) in enumerate(rectangles):
        color = (i % 2) + 1  # 1: Red, 2: Blue
        for x in range(x1 + offset, x2 + offset):
            for y in range(y1 + offset, y2 + offset):
                grid[x][y] = color
    
    # 파란색 영역의 넓이 계산
    blue_area = 0
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] == 2:
                blue_area += 1
    
    return blue_area

# 입력 처리
n = int(input().strip())
rectangles = [tuple(map(int, input().strip().split())) for _ in range(n)]

# 결과 계산
result = calculate_blue_area(n, rectangles)

# 결과 출력
print(result)