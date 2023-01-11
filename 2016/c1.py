def update_direction(direction, rotation):
    if direction == 'N' and rotation == 'R':
        return 'E'
    elif direction == 'N' and rotation == 'L':
        return 'W'
    elif direction == 'S' and rotation == 'R':
        return 'W'
    elif direction == 'S' and rotation == 'L':
        return 'E'
    elif direction == 'E' and rotation == 'R':
        return 'S'
    elif direction == 'E' and rotation == 'L':
        return 'N'
    elif direction == 'W' and rotation == 'R':
        return 'N'
    elif direction == 'W' and rotation == 'L':
        return 'S'

def plot_route(data):
    direction = 'N'
    x = 0
    y = 0
    visits = {(0,0)}
    for d in data:
        direction = update_direction(direction, d[0])
        distance = int(d[1:])
        if direction == 'E':
            for i in range(x + 1, x + distance + 1):
                if (i, y) in visits:
                    return abs(i) + abs(y)
                else:
                    visits.add((i, y))
            x += distance
        elif direction == 'W':
            for i in range(x - 1, x - distance - 1, -1):
                if (i, y) in visits:
                    return abs(i) + abs(y)
                else:
                    visits.add((i, y))
            x -= distance
        elif direction == 'N':
            for i in range(y + 1, y + distance + 1):
                if (x, i) in visits:
                    return abs(x) + abs(i)
                else:
                    visits.add((x, i))
            y += distance
        elif direction == 'S':
            for i in range(y - 1, y - distance - 1, -1):
                if (x, i) in visits:
                    return abs(x) + abs(i)
                else:
                    visits.add((x, i))
            y -= distance
            
with open('i1.txt') as f:
    data = f.read().replace(' ', '').split(',')
    
print(plot_route(data))

