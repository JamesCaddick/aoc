from itertools import cycle
import numpy as np
from copy import copy

def print_formation(formation):
    for row in np.flipud(formation):
        r = ''.join(['.' if i == 0 else '#' for i in row])
        print(r)
    print('\n')

def stringify_formation(formation):
    return '\n'.join([''.join('.' if i == 0 else '#' for i in row) for row in np.flipud(formation)])

def move_rock(formation, rock, direction, x, y):
    test_formation = copy(formation)
    i = x + directions[direction][0]
    j = y + directions[direction][1]
    if i < 0:
        return formation, True, x, y
    elif j + rock.shape[1] - 1 > 6 or j < 0:
        j = y
    test_formation[i: i + rock.shape[0], j: j + rock.shape[1]] = (test_formation[i: i + rock.shape[0],
                                                                                 j: j + rock.shape[1]] 
                                                                  + rock)
    test_formation[x: x + rock.shape[0], y: y + rock.shape[1]] = (test_formation[x: x + rock.shape[0],
                                                                                 y: y + rock.shape[1]] 
                                                                  - rock)
    if not (test_formation == 2).any():
        return test_formation, False, i, j
    elif (test_formation == 2).any() and direction == 'v':
        return formation, True, x, y
    else:
        return formation, False, x, y

with open('i17.txt') as f:
    data = f.read()
    
directions = {'<': (0, -1),
              '>': (0, 1),
              'v': (-1, 0)}
    
rock_type = {'a': np.array([[1,1,1,1]]),
             'b': np.array([[0,1,0],[1,1,1],[0,1,0]]),
             'c': np.array([[1,1,1],[0,0,1],[0,0,1]]),
             'd': np.array([[1],[1],[1],[1]]),
             'e': np.array([[1,1],[1,1]])}

rock_cycle = cycle('abcde')
gust_cycle = cycle(data)

formation = np.zeros((1, 7))

# part 1
# n = 0
# height = 0
# while n < 2022:
#     rock = next(rock_cycle)
#     x = 3 + height
#     y = 2
#     at_rest = False
#     formation = np.concatenate([formation, np.zeros((7, 7))], axis=0)
#     formation[x: x + rock_type[rock].shape[0], y: y + rock_type[rock].shape[1]] = (formation[x: x + rock_type[rock].shape[0],
#                                                                                              y: y + rock_type[rock].shape[1]] 
#                                                                                    + rock_type[rock])
#     while not at_rest:
#         gust = next(gust_cycle)
#         formation, at_rest, x, y = move_rock(formation, rock_type[rock], gust, x, y)
#         formation, at_rest, x, y = move_rock(formation, rock_type[rock], 'v', x, y)
#     height = max(x + rock_type[rock].shape[0], height)
#     formation = formation[:height,:]
#     n += 1

# find the repeating cycle
n = 0
g = 0
height = 0
rocks = 'abcde'
state = {}
while n < 100000:
    rock = rocks[n % 5]
    x = 3 + height
    y = 2
    at_rest = False
    formation = np.concatenate([formation, np.zeros((7, 7))], axis=0)
    formation[x: x + rock_type[rock].shape[0], y: y + rock_type[rock].shape[1]] = (formation[x: x + rock_type[rock].shape[0],
                                                                                             y: y + rock_type[rock].shape[1]] 
                                                                                   + rock_type[rock])
    while not at_rest:
        gust = data[g % len(data)]
        formation, at_rest, x, y = move_rock(formation, rock_type[rock], gust, x, y)
        g += 1
        formation, at_rest, x, y = move_rock(formation, rock_type[rock], 'v', x, y)
    height = max(x + rock_type[rock].shape[0], height)
    formation = formation[:height,:]
    if (n % 5, g % len(data), stringify_formation(formation[-80:])) in state:
        non_repeating_height, non_repeating_bricks = state[(n % 5, g % len(data), stringify_formation(formation[-80:]))]
        height_per_cycle = height - non_repeating_height
        bricks_per_cycle = n - non_repeating_bricks
        n = 200000
    state[(n % 5, g % len(data), stringify_formation(formation[-80:]))] = height, n
    n += 1
    
total_bricks = 1_000_000_000_000
bricks_in_partial_cycle = (total_bricks - non_repeating_bricks) % bricks_per_cycle

total_height = (total_bricks - bricks_in_partial_cycle - non_repeating_bricks) / bricks_per_cycle * height_per_cycle + non_repeating_height

# get size of partially repeated cycle
formation = np.zeros((1, 7))
n = 0
g = 0
height = 0
while n < bricks_in_partial_cycle + non_repeating_bricks:
    rock = rocks[n % 5]
    x = 3 + height
    y = 2
    at_rest = False
    formation = np.concatenate([formation, np.zeros((7, 7))], axis=0)
    formation[x: x + rock_type[rock].shape[0], y: y + rock_type[rock].shape[1]] = (formation[x: x + rock_type[rock].shape[0],
                                                                                             y: y + rock_type[rock].shape[1]] 
                                                                                   + rock_type[rock])
    while not at_rest:
        gust = data[g % len(data)]
        formation, at_rest, x, y = move_rock(formation, rock_type[rock], gust, x, y)
        g += 1
        formation, at_rest, x, y = move_rock(formation, rock_type[rock], 'v', x, y)
    height = max(x + rock_type[rock].shape[0], height)
    formation = formation[:height,:]
    n += 1

partial_height = height - non_repeating_height
print(int(total_height + partial_height))