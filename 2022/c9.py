import numpy as np

with open('i9.txt') as f:
    data = f.read().split('\n')
    
tail_path = [(0, 0)]

def move_tail(head_pos, tail_pos):
    x_head, y_head = head_pos
    x_tail, y_tail = tail_pos
    if (x_head - x_tail > 1 and y_head - y_tail == 1) or (x_head - x_tail == 1 and y_head - y_tail > 1) or (x_head - x_tail > 1 and y_head - y_tail > 1):
        y_tail += 1
        x_tail += 1
    elif (x_head - x_tail < -1 and y_head - y_tail == -1) or (x_head - x_tail == -1 and y_head - y_tail < -1) or (x_head - x_tail < -1 and y_head - y_tail < -1):
        y_tail -= 1
        x_tail -= 1
    elif (x_head - x_tail > 1 and y_head - y_tail == -1) or (x_head - x_tail == 1 and y_head - y_tail < -1) or (x_head - x_tail > 1 and y_head - y_tail < -1):
        y_tail -= 1
        x_tail += 1
    elif (x_head - x_tail < -1 and y_head - y_tail == 1) or (x_head - x_tail == -1 and y_head - y_tail > 1) or (x_head - x_tail < -1 and y_head - y_tail > 1):
        y_tail += 1
        x_tail -= 1
    elif x_head - x_tail > 1:
        x_tail += 1
    elif x_head - x_tail < -1:
        x_tail -= 1
    elif y_head - y_tail > 1:
        y_tail += 1
    elif y_head - y_tail < -1:
        y_tail -= 1
    tail_pos = (x_tail, y_tail)
    return tail_pos

x_head = 0
y_head = 0
x_tail_1 = 0
y_tail_1 = 0
x_tail_2 = 0
y_tail_2 = 0
x_tail_3 = 0
y_tail_3 = 0
x_tail_4 = 0
y_tail_4 = 0
x_tail_5 = 0
y_tail_5 = 0
x_tail_6 = 0
y_tail_6 = 0
x_tail_7 = 0
y_tail_7 = 0
x_tail_8 = 0
y_tail_8 = 0
x_tail = 0
y_tail = 0
for d in data:
    direction, distance = d.split(' ')
    distance = int(distance)
    for i in range(distance):
        if direction == 'U':
            y_head += 1
        elif direction == 'D':
            y_head -= 1
        elif direction == 'L':
            x_head -= 1
        elif direction == 'R':
            x_head += 1
        # print(f'head is at {(x_head, y_head)}')
        x_tail_1, y_tail_1 = move_tail((x_head, y_head), (x_tail_1, y_tail_1))
        x_tail_2, y_tail_2 = move_tail((x_tail_1, y_tail_1), (x_tail_2, y_tail_2))
        x_tail_3, y_tail_3 = move_tail((x_tail_2, y_tail_2), (x_tail_3, y_tail_3))
        x_tail_4, y_tail_4 = move_tail((x_tail_3, y_tail_3), (x_tail_4, y_tail_4))
        x_tail_5, y_tail_5 = move_tail((x_tail_4, y_tail_4), (x_tail_5, y_tail_5))
        x_tail_6, y_tail_6 = move_tail((x_tail_5, y_tail_5), (x_tail_6, y_tail_6))
        x_tail_7, y_tail_7 = move_tail((x_tail_6, y_tail_6), (x_tail_7, y_tail_7))
        x_tail_8, y_tail_8 = move_tail((x_tail_7, y_tail_7), (x_tail_8, y_tail_8))
        x_tail, y_tail = move_tail((x_tail_8, y_tail_8), (x_tail, y_tail))
        tail_path.append((x_tail, y_tail))
        # print(f'tail is at {(x_tail, y_tail)}\n')

print(f'the answer to part 1 is {len(set(tail_path))}')

max_x = max([point[0] for point in tail_path])
min_x = min([point[0] for point in tail_path])
max_y = max([point[1] for point in tail_path])
min_y = min([point[1] for point in tail_path])

visual = np.zeros((max_x - min_x + 1, max_y - min_y + 1))
for point in set(tail_path):
    visual[point[0] + abs(min_x), point[1] + abs(min_y)]=1
for row in np.rot90(visual):
    print(''.join(['#' if x == 1 else '.' for x in row]))
