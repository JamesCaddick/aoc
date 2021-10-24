import numpy as np
import hashlib
import re

filepath = 'D:/Users/jcaddick/aoc/aoc/'

def day_1_part_1():
    with open(filepath + 'input_1.txt') as f:
        input = f.read()
    return input.count('(') - input.count(')')

def day_1_part_2():
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

def day_2_part_1():
    with open(filepath + 'input_2.txt') as f:
        input = f.readlines()
        input = [list(map(int, x.strip('\n').split('x'))) for x in input]
        total = 0
        for d in input:
            l, w, h = d
            total += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, l * h)
    return total
    
def day_2_part_2():
    with open(filepath + 'input_2.txt') as f:
        input = f.readlines()
        input = [list(map(int, x.strip('\n').split('x'))) for x in input]
        total = 0
        for d in input:
            l, w, h = d
            total += l * w * h + min(2 * l + 2 * w, 2 * w + 2 * h, 2 * l + 2 * h)
    return total


def day_3_part_1():
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

def day_3_part_2():
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

def day_4_part_1():
    coin = 0
    key = 'iwrupvqb'
    h = ''
    while h[:5] != '00000':
        coin += 1
        h = hashlib.md5((key + str(coin)).encode()).hexdigest()
    return coin

def day_4_part_2():
    coin = 0
    key = 'iwrupvqb'
    h = ''
    while h[:6] != '000000':
        coin += 1
        h = hashlib.md5((key + str(coin)).encode()).hexdigest()
    return coin

def day_5_part_1():
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

def day_5_part_2():
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

def day_6_part_1():
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

def day_6_part_2():
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

def day_7_part_1():
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

def day_7_part_2():
    ...

def day_8_part_1():
    with open(filepath + 'input_7.txt') as f:
        input = f.readlines()
    input = [i.strip('\n') for i in input]
    raw = [len(i) for i in input]
    escaped = [len(re.escape(i)) for i in input]
    return input


def day_8_part_2():
    ...


# --- Day 9: All in a Single Night ---
# Every year, Santa manages to deliver all of his presents in a single night.

# This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

# For example, given the following distances:

# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# The possible routes are therefore:

# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982
# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

# What is the distance of the shortest route?

def day_9_part_1():
    ...


def day_9_part_2():
    ...

# --- Day 10: Elves Look, Elves Say ---
# Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

# Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

# For example:

# 1 becomes 11 (1 copy of digit 1).
# 11 becomes 21 (2 copies of digit 1).
# 21 becomes 1211 (one 2 followed by one 1).
# 1211 becomes 111221 (one 1, one 2, and two 1s).
# 111221 becomes 312211 (three 1s, two 2s, and one 1).
# Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

# Your puzzle input is 1113222113.

# --- Day 11: Corporate Policy ---
# Santa's previous password expired, and he needs help choosing a new one.

# To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

# Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

# Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
# Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
# Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
# For example:

# hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
# abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
# abbcegjk fails the third requirement, because it only has one double letter (bb).
# The next password after abcdefgh is abcdffaa.
# The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
# Given Santa's current password (your puzzle input), what should his next password be?

# Your puzzle input is hxbxwxba.

# --- Day 12: JSAbacusFramework.io ---
# Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

# They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

# For example:

# [1,2,3] and {"a":2,"b":4} both have a sum of 6.
# [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
# {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
# [] and {} both have a sum of 0.
# You will not encounter any strings containing numbers.

# What is the sum of all numbers in the document?

# --- Day 13: Knights of the Dinner Table ---
# In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.

# You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

# For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

# Alice would gain 54 happiness units by sitting next to Bob.
# Alice would lose 79 happiness units by sitting next to Carol.
# Alice would lose 2 happiness units by sitting next to David.
# Bob would gain 83 happiness units by sitting next to Alice.
# Bob would lose 7 happiness units by sitting next to Carol.
# Bob would lose 63 happiness units by sitting next to David.
# Carol would lose 62 happiness units by sitting next to Alice.
# Carol would gain 60 happiness units by sitting next to Bob.
# Carol would gain 55 happiness units by sitting next to David.
# David would gain 46 happiness units by sitting next to Alice.
# David would lose 7 happiness units by sitting next to Bob.
# David would gain 41 happiness units by sitting next to Carol.
# Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

# If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:

#      +41 +46
# +55   David    -2
# Carol       Alice
# +60    Bob    +54
#      -7  +83
# After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

# What is the total change in happiness for the optimal seating arrangement of the actual guest list?

# --- Day 14: Reindeer Olympics ---
# This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

# Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

# For example, suppose you have the following Reindeer:

# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
# After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

# In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

# Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?

# --- Day 15: Science for Hungry People ---
# Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

# Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

# capacity (how well it helps the cookie absorb milk)
# durability (how well it keeps the cookie intact when full of milk)
# flavor (how tasty it makes the cookie)
# texture (how it improves the feel of the cookie)
# calories (how many calories it adds to the cookie)
# You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

# For instance, suppose you have these two ingredients:

# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
# Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

# A capacity of 44*-1 + 56*2 = 68
# A durability of 44*-2 + 56*3 = 80
# A flavor of 44*6 + 56*-2 = 152
# A texture of 44*3 + 56*-1 = 76
# Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?