def flip_tiles(commands):
    tiles = {}
    position = 0

    for command in commands:
        x, direction = command.split()
        x = int(x)
        
        if direction == 'L':
            for i in range(position, position - x, -1):
                if i in tiles:
                    tiles[i] = 'W' if tiles[i] == 'B' else 'B'
                else:
                    tiles[i] = 'W'
            position -= (x - 1)
        elif direction == 'R':
            for i in range(position, position + x):
                if i in tiles:
                    tiles[i] = 'B' if tiles[i] == 'W' else 'W'
                else:
                    tiles[i] = 'B'
            position += (x - 1)

    white_count = sum(1 for color in tiles.values() if color == 'W')
    black_count = sum(1 for color in tiles.values() if color == 'B')

    return white_count, black_count

# Input reading
n = int(input().strip())
commands = [input().strip() for _ in range(n)]

# Execute the commands and get the result
white_count, black_count = flip_tiles(commands)

# Output the result
print(white_count, black_count)