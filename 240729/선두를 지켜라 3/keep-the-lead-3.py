def calculate_leader_changes(N, M, moves_A, moves_B):
    # 두 사람의 이동 정보를 시간별로 병합
    events = []
    current_time = 0

    # A의 이동 정보 추가
    for v, t in moves_A:
        events.append((current_time, 'A', v, t))
        current_time += t
    
    current_time = 0
    
    # B의 이동 정보 추가
    for v, t in moves_B:
        events.append((current_time, 'B', v, t))
        current_time += t
    
    # 시간 순으로 정렬
    events.sort()
    
    pos_A = pos_B = 0
    last_leader = None
    leader_changes = 0
    
    for start_time, person, v, t in events:
        end_time = start_time + t
        
        if person == 'A':
            new_pos_A = pos_A + v * t
            pos_A = new_pos_A
        else:
            new_pos_B = pos_B + v * t
            pos_B = new_pos_B
        
        if pos_A > pos_B:
            current_leader = 'A'
        elif pos_A < pos_B:
            current_leader = 'B'
        else:
            current_leader = 'AB'
        
        if current_leader != last_leader:
            leader_changes += 1
            last_leader = current_leader
    
    return leader_changes

# 입력 받기
N, M = map(int, input().strip().split())
moves_A = [tuple(map(int, input().strip().split())) for _ in range(N)]
moves_B = [tuple(map(int, input().strip().split())) for _ in range(M)]

# 결과 계산
result = calculate_leader_changes(N, M, moves_A, moves_B)

# 결과 출력
print(result)