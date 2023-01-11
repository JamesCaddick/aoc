import numpy as np
import textwrap

def move_crate(s, o, d):
    s[d] = s[o][0] + s[d]
    s[o] = s[o][1:]
    return s

def move_crate_9001(s, o, d, n):
    s[d] = s[o][0:n] + s[d]
    s[o] = s[o][n:]
    return s

with open('i5.txt') as f:
    data = f.read()

stacks, instructions = data.split('\n\n')
stacks = [textwrap.wrap(stack, 4, replace_whitespace=False, drop_whitespace=False) for stack in stacks.split('\n')]
stacks = np.asarray([[s.replace('[', '').replace(']', '').replace(' ', '') for s in stack] for stack in stacks][:-1])
stacks = [''.join(stacks[:, i]) for i in range(len(stacks[0]))]
instructions = instructions.split('\n')

for i in instructions:
    _, number, _, origin, _, destination = i.split(' ')
    number = int(number)
    origin = int(origin) - 1
    destination = int(destination) - 1
    # part 1
    # for n in range(number):
    #     stacks = move_crate(stacks, origin, destination)
    # part 2
    stacks = move_crate_9001(stacks, origin, destination, number)
        
print(stacks[0][0] + stacks[1][0] + stacks[2][0] + stacks[3][0] + stacks[4][0] + stacks[5][0] + stacks[6][0] + stacks[7][0] + stacks[8][0])