from itertools import cycle
import numpy as np

with open('i17.txt') as f:
    data = f.read()
    
rock_type = {'a': np.array([[1,1,1,1]]),
              'b': np.array([[0,1,0],[1,1,1],[0,1,0]]),
              'c': np.array([[0,0,1],[0,0,1],[1,1,1]]),
              'd': np.array([1,1,1,1]),
              'e': np.array([[1,1],[1,1]])} 
rock_cycle = cycle('abcde')
gust_cycle = cycle(data)
formation = np.zeros((6, 7))
n = 0

# while n < 2022:
#     rock = next(rock_cycle)
#     x = 2
#     y = 3
#     at_rest = False
#     while not at_rest:
#         gust = next(gust_cycle)
#         if gust == '<':
#             x = min(0, x - 1)
#         if gust == '>':
#             x = max(6, x + 1)
        
#         # move object
#         # drop object
#         # test whether at rest
#             # if at rest then change status of at_rest and update rock_formation
#         n += 1
        

formation[3: 3 + rock_type['e'].shape[0], 2: 2 + rock_type['e'].shape[1]] = formation[3: 3 + rock_type['e'].shape[0], 2: 2 + rock_type['e'].shape[1]] + rock_type['e']
print(np.flipud(formation))