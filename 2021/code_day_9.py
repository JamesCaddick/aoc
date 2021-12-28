'''
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly 
settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap 
of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent
locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal 
locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one 
is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. 
The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?
'''
import numpy as np

test = np.array([[2,1,9,9,9,4,3,2,1,0],
                 [3,9,8,7,8,9,4,9,2,1],
                 [9,8,5,6,7,8,9,8,9,2],
                 [8,7,6,7,8,9,6,7,8,9],
                 [9,8,9,9,9,6,5,6,7,8]])

def is_lower(y, x, arr):
    if x - 1 >= 0:
        if arr[y][x] >= arr[y][x - 1]:
            return False
    if x + 1 <= len(arr[y]) - 1:
        if arr[y][x] >= arr[y][x + 1]:
            return False
    if y - 1 >= 0:
        if arr[y][x] >= arr[y - 1][x]:
            return False
    if y + 1 <= len(arr) - 1:
        if arr[y][x] >= arr[y + 1][x]:
            return False
    return True

with open('D:/Users/jcaddick/aoc/aoc/2021/input_day_9.txt') as f:
    data = f.read().split()
data = np.array([list(d) for d in data]).astype(np.int16)
# data = test
risk_pts = []
lows = []
for x in range(data.shape[0]):
    for y in range(data.shape[1]):
        if is_lower(x, y, data):
            risk_pts.append(data[x, y] + 1)
            lows.append((x, y))
part1 = sum(risk_pts)
print(f'the answer to part 1 is {part1}')

'''
--- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are 
very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
'''

def basin_size(arr, x, y, coords_cache={}):
    result = 0
    if x - 1 >= 0:
        if (x - 1, y) not in coords_cache:
            coords_cache[(x - 1, y)] = arr[x - 1, y]
            if arr[x - 1, y] < 9:
                result += 1 + basin_size(arr, x - 1, y, coords_cache)
    if x + 1 <= len(arr[y]) - 1:
        if (x + 1, y) not in coords_cache:
            coords_cache[(x + 1, y)] = arr[x + 1, y]
            if arr[x + 1, y] < 9:
                result += 1 + basin_size(arr, x + 1, y, coords_cache)
    if y - 1 >= 0:
        if (x, y - 1) not in coords_cache:
            coords_cache[(x, y - 1)] = arr[x, y - 1]
            if arr[x, y - 1] < 9:
                result += 1 + basin_size(arr, x, y - 1, coords_cache)
    if y + 1 <= len(arr) - 1:
        if (x, y + 1) not in coords_cache:
            coords_cache[(x, y + 1)] = arr[x, y + 1]
            if arr[x, y + 1] < 9:
                result += 1 + basin_size(arr, x, y + 1, coords_cache)
    return result

def find_basin_sizes():
    sizes = []
    for coords in lows:
        x, y = coords
        sizes.append(basin_size(data, x, y))
    sizes = sorted(sizes, reverse=True)[0:3]
    return sizes
    
a, b, c = find_basin_sizes()
print(f'the answer to part 2 is {a * b * c}')
        