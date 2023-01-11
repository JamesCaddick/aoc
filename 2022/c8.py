import numpy as np

with open('i8.txt') as f:
    data = f.read().split('\n')
data = np.array([list(d) for d in data], dtype=int)

height, width = data.shape
visible = np.zeros((height, width), dtype=int)
scenic = np.zeros((height, width), dtype=int)

for i, row in enumerate(data):
    max_height = [-1]
    for j, col in enumerate(row):
        if data[i, j] > max(max_height):
            visible[i, j] = 1
            max_height.append(data[i, j])
    max_height = [-1]
    for j, col in enumerate(list(reversed(row))):
        if data[i, width - j - 1] > max(max_height):
            visible[i, width - j - 1] = 1
            max_height.append(data[i, width - j - 1])
            scenic[i, j] += 1

for j, col in enumerate(np.transpose(data)):
    max_height = [-1]
    for i, row in enumerate(col):
        if data[i, j] > max(max_height):
            visible[i, j] = 1
            max_height.append(data[i, j])
    max_height = [-1]
    for i, row in enumerate(list(reversed(col))):
        if data[height - i - 1, j] > max(max_height):
            visible[height - i - 1, j] = 1
            max_height.append(data[height - i - 1, j])
            
def count_trees(i, j, trees):
    #up
    up_count = 0
    if i < height:
        # up_count += 1
        up = data[i + 1:, j]
        for u in up:
            if u < trees[i, j]:
                up_count += 1
            else:
                up_count += 1
                break
    # down
    down_count = 0
    if i > 0:
        # down_count += 1
        down = list(reversed(data[: i, j]))
        for d in down:
            if d < trees[i, j]:
                down_count += 1
            else:
                down_count += 1
                break
    # left
    left_count = 0
    if j > 0:
        # left_count += 1
        left = list(reversed(data[i, :j]))
        for l in left:
            if l < trees[i, j]:
                left_count += 1
            else:
                left_count += 1
                break
    # right
    right_count = 0
    if j < width:
        # right_count += 1
        right = data[i, j + 1:]
        for r in right:
            if r < trees[i, j]:
                right_count += 1
            else:
                right_count += 1
                break
    return up_count * down_count * left_count * right_count
            
for i, row in enumerate(data):
    for j, col in enumerate(row):
        scenic[i, j] = count_trees(i, j, data)
        
print(f'the answer to part 1 is {visible.sum()}')
print(f'the answer to part 2 is {scenic.max()}')