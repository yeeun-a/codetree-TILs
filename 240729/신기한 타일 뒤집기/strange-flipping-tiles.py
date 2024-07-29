def flip_tiles(n, commands):
    tiles = {}
    position = 0
    
    for command in commands:
        x, direction = command.split()
        x = int(x)
        
        if direction == "L":
            for i in range(position, position - x, -1):
                if i in tiles:
                    if tiles[i] == "B":
                        tiles[i] = "W"
                    else:
                        del tiles[i]
                else:
                    tiles[i] = "W"
            position -= (x - 1)
        
        elif direction == "R":
            for i in range(position, position + x):
                if i in tiles:
                    if tiles[i] == "W":
                        tiles[i] = "B"
                    else:
                        del tiles[i]
                else:
                    tiles[i] = "B"
            position += (x - 1)

    white_count = sum(1 for color in tiles.values() if color == "W")
    black_count = sum(1 for color in tiles.values() if color == "B")
    
    return white_count, black_count

# 입력 받기
n = int(input().strip())
commands = [input().strip() for _ in range(n)]

# 결과 계산
white_count, black_count = flip_tiles(n, commands)

# 결과 출력
print(white_count, black_count)