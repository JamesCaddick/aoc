'''
--- Day 13: Transparent Origami ---
You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.
Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent 
paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:

6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, x, increases to the right. The second value, y, increases downward. So, the c
oordinate 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the paper and . is an empty, unmarked position:

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). 
In this example, the first fold instruction is fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with -):

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing 
this fold looks like this:

#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........
Now, only 17 dots are visible.

Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at 0,0 and 0,1). 
Because the paper is transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.

The second fold instruction is fold along x=5, which indicates this line:

#.##.|#..#.
#...#|.....
.....|#...#
#...#|.....
.#.#.|#.###
.....|.....
.....|.....
Because this is a vertical line, fold left:

#####
#...#
#...#
#...#
#####
.....
.....
The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, 17 dots are visible - dots that end up overlapping after the fold is 
completed count as a single dot.

How many dots are visible after completing just the first fold instruction on your transparent paper?
'''

import numpy as np
import re

with open('D:/Users/jcaddick/aoc/aoc/2021/input_day_13.txt') as f:
    data = f.read().split('\n')
dots = [list(map(int, d.split(','))) for d in data[0:data.index('')]]
pttn = r'([x,y])=(\d{1,3})'
folds = [re.findall(pttn, f)[0] for f in data[data.index('') + 1:]]
folds = [(f[0], int(f[1])) for f in folds]
xs = [d[1] for d in dots]
ys = [d[0] for d in dots]
grid = np.zeros((max(xs) + 1, max(ys) + 1))
grid[xs, ys] += 1

def fold(f, grid):
    direction, idx = f
    if direction == 'x':
        no_flip = grid[:, :idx]
        flip = grid[:, idx:]
        flip = np.fliplr(flip)
        if flip.shape[1] < no_flip.shape[1]:
            no_flip = no_flip[:,:flip.shape[1]]
            no_flip += flip
            return no_flip
        else:
            flip = flip[:,:no_flip.shape[1]] 
            flip += no_flip
            return flip
    else:
        no_flip = grid[:idx, :]
        flip = grid[idx:, :]
        flip = np.flipud(flip)
        if flip.shape[0] < no_flip.shape[0]:
            no_flip = no_flip[:flip.shape[0],:]
            no_flip += flip
            return no_flip
        else:
            flip = flip[:no_flip.shape[0],:]
            flip += no_flip
            return flip    
        
print(f'the answer to part 1 is {np.count_nonzero(fold(folds[0], grid))}')
    
'''
--- Part Two ---
Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera system?
'''

grid = np.zeros((max(xs) + 1, max(ys) + 1))
grid[xs, ys] += 1

for f in folds:
    grid = fold(f, grid)
grid = np.where(grid > 0, 1, grid)
code = [[' ' if col == 0 else '#' for col in row] for row in grid]
for c in code:
    print(''.join(c))