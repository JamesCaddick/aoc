import numpy as np
import hashlib
import re

filepath = 'D:/Users/jcaddick/aoc/'

def q1():
    with open(filepath + 'input_1.txt') as f:
        input = f.read()
    return input.count('(') - input.count(')')

def q2():
    with open(filepath + 'input_1.txt') as f:
        input = f.read()
        total = 0
        for x, y in enumerate(input):
            if y == '(':
                total += 1
            else:
                total -= 1
            if total < 0:
                return x + 1

def q3():
    with open(filepath + 'input_2.txt') as f:
        input = f.readlines()
        input = [list(map(int, x.strip('\n').split('x'))) for x in input]
        total = 0
        for d in input:
            l, w, h = d
            total += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, l * h)
    return total
    
def q4():
    with open(filepath + 'input_2.txt') as f:
        input = f.readlines()
        input = [list(map(int, x.strip('\n').split('x'))) for x in input]
        total = 0
        for d in input:
            l, w, h = d
            total += l * w * h + min(2 * l + 2 * w, 2 * w + 2 * h, 2 * l + 2 * h)
    return total


def q5():
    with open(filepath + 'input_3.txt') as f:
        input = f.read()
    visited = [(0,0)]
    x = 0
    y = 0
    for a in input:
        if a == '^':
            y += 1
        elif a == 'v':
            y -= 1
        elif a == '>':
            x += 1
        elif a == '<':
            x -= 1
        if (x, y) not in visited:
            visited.append((x, y))
    return len(visited)

def q6():
    with open(filepath + 'input_3.txt') as f:
        input = f.read()
    santa = [input[i] for i in range(len(input)) if i % 2 == 0]
    robo = [input[i] for i in range(len(input)) if i % 2 != 0]
    santa_visited = {(0,0)}
    robo_visited = {(0,0)}
    x = 0
    y = 0
    for a in santa:
        if a == '^':
            y += 1
        elif a == 'v':
            y -= 1
        elif a == '>':
            x += 1
        elif a == '<':
            x -= 1
        santa_visited.add((x, y))
    x = 0
    y = 0
    for a in robo:
        if a == '^':
            y += 1
        elif a == 'v':
            y -= 1
        elif a == '>':
            x += 1
        elif a == '<':
            x -= 1
        robo_visited.add((x, y))
    return len(santa_visited.union(robo_visited))

def q7():
    coin = 0
    key = 'iwrupvqb'
    h = ''
    while h[:5] != '00000':
        coin += 1
        h = hashlib.md5((key + str(coin)).encode()).hexdigest()
    return coin

def q8():
    coin = 0
    key = 'iwrupvqb'
    h = ''
    while h[:6] != '000000':
        coin += 1
        h = hashlib.md5((key + str(coin)).encode()).hexdigest()
    return coin

def q9():
    with open(filepath + 'input_4.txt') as f:
        input = f.readlines()
    input = [i.strip('\n') for i in input]
    good = 0
    for s in input:
        vowels = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') > 2
        bad = 'ab' not in s and 'cd' not in s and 'pq' not in s and 'xy' not in s
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        consecutive = False
        for _ in alpha:
            if _ * 2 in s:
                consecutive = True
                break
        if vowels and bad and consecutive:
            good += 1
    return good

def q10():
    with open(filepath + 'input_4.txt') as f:
        input = f.readlines()
    input = [i.strip('\n') for i in input]
    good = 0
    for s in input:
        pair = False
        repeat = False
        for i in range(len(s) - 2):
            if s[i: i + 2] in s[i + 2:]:
                pair = True
                break
        for i in range(len(s) - 2):
            if s[i] == s[i + 2]:
                repeat = True
                break
        if pair and repeat:
            good += 1
    return good

def q11():
    with open(filepath + 'input_5.txt') as f:
        input = f.readlines()
    input = [i.strip('\n') for i in input]
    lights = np.zeros((1000, 1000))
    for i in input:
        j = i.split(' ')
        j = j[-4:]
        action = j[0]
        a, b = map(int, j[1].split(','))
        c, d = map(int, j[-1].split(','))
        if action =='on':
            lights[a:c + 1, b:d + 1] = 1
        elif 'off' in i:
            lights[a:c + 1, b:d + 1] = 0
        elif 'toggle' in i:
            lights[a:c + 1, b:d + 1] = np.where(lights[a:c + 1, b:d + 1] == 1, 0, 1)
    return lights.sum()

def q12():
    with open(filepath + 'input_5.txt') as f:
        input = f.readlines()
    input = [i.strip('\n') for i in input]
    lights = np.zeros((1000, 1000))
    for i in input:
        j = i.split(' ')
        j = j[-4:]
        action = j[0]
        a, b = map(int, j[1].split(','))
        c, d = map(int, j[-1].split(','))
        if action =='on':
            lights[a:c + 1, b:d + 1] += 1
        elif 'off' in i:
            lights[a:c + 1, b:d + 1] -= 1
            lights = np.where(lights < 0, 0, lights)
        elif 'toggle' in i:
            lights[a:c + 1, b:d + 1] += 2
    return lights.sum()

def q13():
    with open(filepath + 'input_6.txt') as f:
        input = f.readlines()
    input = [i.strip('\n').split(' ') for i in input]    
    wires = {}
    while len(input) > 0:
        for i in input:
            if 'AND' in i:
                arg1, action, arg2, arrow, out = i
                try:
                    arg1 = int(arg1)
                except ValueError:
                    pass
                try:
                    arg2 = int(arg2)
                except ValueError:
                    pass     
                if arg1 in wires and arg2 in wires:
                    wires[out] = wires[arg1] & wires[arg2]
                    input.remove(i)
                elif isinstance(arg1, int) and isinstance(arg2, int):
                    wires[out] = arg1 & arg2
                    input.remove(i)
                elif isinstance(arg1, int) and arg2 in wires:
                    wires[out] = arg1 & wires[arg2]
                    input.remove(i)
                elif arg1 in wires and isinstance(arg2, int):
                    wires[out] = wires[arg1] & arg2
                    input.remove(i)
            elif 'OR' in i:
                arg1, action, arg2, arrow, out = i
                try:
                    arg1 = int(arg1)
                except ValueError:
                    pass
                try:
                    arg2 = int(arg2)
                except ValueError:
                    pass  
                if arg1 in wires and arg2 in wires:
                    wires[out] = wires[arg1] | wires[arg2]
                    input.remove(i)
                elif isinstance(arg1, int) and isinstance(arg2, int):
                    wires[out] = arg1 | arg2
                    input.remove(i)
                elif isinstance(arg1, int) and arg2 in wires:
                    wires[out] = arg1 | wires[arg2]
                    input.remove(i)
                elif arg1 in wires and isinstance(arg2, int):
                    wires[out] = wires[arg1] | arg2
                    input.remove(i)
            elif 'LSHIFT' in i:
                arg1, action, arg2, arrow, out = i
                try:
                    arg1 = int(arg1)
                except ValueError:
                    pass
                if arg1 in wires:
                    wires[out] = wires[arg1] << int(arg2)
                    input.remove(i)
                elif isinstance(arg1, int):
                    wires[out] = arg1 << int(arg2)
                    input.remove(i)
            elif 'RSHIFT' in i:
                arg1, action, arg2, arrow, out = i
                try:
                    arg1 = int(arg1)
                except ValueError:
                    pass
                if arg1 in wires:
                    wires[out] = wires[arg1] >> int(arg2)
                    input.remove(i)
                elif isinstance(arg1, int):
                    wires[out] = arg1 >> int(arg2)
                    input.remove(i)
            elif 'NOT' in i:
                action, arg1, arrow, out = i
                try:
                    arg1 = int(arg1)
                except ValueError:
                    pass
                if arg1 in wires:
                    wires[out] = 65535 - wires[arg1]
                    input.remove(i)
                elif isinstance(arg1, int):
                    wires[out] = 65535 - arg1
                    input.remove(i)
            else:
                try:
                    arg1 = int(arg1)
                except ValueError:
                    pass
                arg1, arrow, out = i
                if isinstance(arg1, int):
                    wires[out] = arg1
                    input.remove(i)
                elif arg1 in wires:
                    wires[out] = wires[arg1]
                    input.remove(i)
        return wires['a']


def q15():
    with open(filepath + 'input_7.txt') as f:
        input = f.readlines()
    input = [i.strip('\n') for i in input]
    raw = [len(i) for i in input]
    escaped = [len(re.escape(i)) for i in input]
    return input

i = q15()