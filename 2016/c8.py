import numpy as np
import copy

with open('i8.txt') as f:
    data = f.readlines()

# data = ['rect 3x2',
#         'rotate column x=1 by 1',
#         'rotate row y=0 by 4',
#         'rotate column x=1 by 1']

H = 6
W = 50
screen = np.zeros((H, W))
# not all sigle digits
for d in data:
    i = d.split()
    if i[0] == 'rect':
        width, height = [int(j) for j in i[1].split('x')]
        screen[:height, :width] = 1
    elif i[1] == 'column':
        col = int(i[2].split('=')[-1])
        offset = int(i[-1])
        c = copy.copy(screen[:, col])
        screen[offset:, col] = c[:H - offset]
        screen[:offset, col] = c[H - offset:]
    else:
        row = int(i[2].split('=')[-1])
        offset = int(i[-1])
        r = copy.copy(screen[row, :])
        screen[row, offset:] = r[:W - offset]
        screen[row, :offset] = r[W - offset:]

print(screen.sum())

for row in screen:
    print(''.join(['   ' if x == 0 else '#  ' for x in row]))