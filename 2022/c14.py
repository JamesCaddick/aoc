import numpy as np
    
def drop_sand(cave, entrance):
    dropping = True
    x, y = entrance
    while dropping:
        if x == 999:
            dropping = False
            x = 0
            y = 0
        elif cave[x + 1, y] == 0:
            x += 1
        elif cave[x + 1, y - 1] == 0:
            x += 1
            y -= 1
        elif cave[x + 1, y + 1] == 0:
            x += 1
            y += 1
        elif cave[x + 1, y] == 1 and cave[x + 1, y - 1] == 1 and cave[x + 1, y + 1] == 1:
            dropping = False
    return x, y
    
def drop_sand_again(cave, entrance):
    dropping = True
    x, y = entrance
    while dropping:
        if x == 163:
            if cave[x + 1, y] == 0:
                x += 1
                dropping =  False
            elif cave[x + 1, y - 1] == 0:
                x += 1
                y -= 1
                dropping =  False
            elif cave[x + 1, y + 1] == 0:
                x += 1
                y += 1
                dropping =  False
            elif cave[x + 1, y] == 1 and cave[x + 1, y - 1] == 1 and cave[x + 1, y + 1] == 1:
                dropping = False
        else:
            if cave[x + 1, y] == 0:
                x += 1
            elif cave[x + 1, y - 1] == 0:
                x += 1
                y -= 1
            elif cave[x + 1, y + 1] == 0:
                x += 1
                y += 1
            elif cave[x + 1, y] == 1 and cave[x + 1, y - 1] == 1 and cave[x + 1, y + 1] == 1:
                dropping = False
    return x, y

with open('i14.txt') as f:
    data = f.read().split('\n')
    
# read cave layout
bottom = 0
cave = np.zeros((165, 1000))
for d in data:
    points = [[int(p) for p in point.split(',')] for point in d.split(' -> ')]
    for i, point in enumerate(points[:-1]):
        a, b = point
        x, y = points[i + 1]
        i = min(a, x) 
        j = min(b, y)
        k = max(a, x)
        l = max(b, y)
        bottom = max(l, bottom)
        cave[j: l + 1, i: k + 1] = 1
        
# drop sand
drip = True
count = 0
while drip:
    x, y = drop_sand_again(cave, (0, 500))
    if x == 0 and y == 500:
        drip = False
        count += 1
    else:
        cave[x, y] = 1
        count += 1
        
print(f'the asnwer to part 1 is {count}')