'''
--- Day 14: Extended Polymerization ---
The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has polymerization equipment that would produce suitable materials to reinforce the 
submarine, and the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.

The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a polymer template and a list of pair insertion rules (your puzzle input). You just need to 
work out what polymer would result after repeating the pair insertion process a few times.

For example:

NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
The first line is the polymer template - this is the starting point of the process.

The following section defines the pair insertion rules. A rule like AB -> C means that when elements A and B are immediately adjacent, element C should be inserted between them. These insertions all 
happen simultaneously.

So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.
Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously, inserted elements are not considered to be 
part of a pair until the next step.

After the first step of this process, the polymer becomes NCNBCHB.

Here are the results of a few steps using the above rules:

Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, H occurs 161 times, and N occurs 865 times; 
taking the quantity of the most common element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract 
the quantity of the least common element?
'''

from collections import Counter

with open('D:/Users/jcaddick/aoc/aoc/2021/input_day_14.txt') as f:
    data = f.read().split('\n')
start = data[0]
subs = {key:key[0] + value + key[1] for key, value in [d.split(' -> ') for d in data[2:]]}
for step in range(10):
    pairs = [start[i:i + 2] for i in range(len(start) - 1)]
    inserts = [subs[p] for p in pairs]
    rejoin = [j[:-1] if i < len(inserts) - 1 else j for i, j in enumerate(inserts)]
    start = ''.join(rejoin)
total = Counter(start)
print(f'the answer to part 1 is {max(total.values()) - min(total.values())}')

'''
--- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.

In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H (occurring 3849876073 times); subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract 
the quantity of the least common element?
'''

import string
from copy import copy

pairs = {key:0 for key, value in [d.split(' -> ') for d in data[2:]]}
subs = {key:[key[0] + value, value + key[1]] for key, value in [d.split(' -> ') for d in data[2:]]}
new_letter = {key:value for key, value in [d.split(' -> ') for d in data[2:]]}
letters = {key:0 for key in string.ascii_uppercase}
start_pairs = [data[0][i:i + 2] for i in range(len(data[0]) - 1)]
for pair in start_pairs:
    pairs[pair] += 1
for char in data[0]:
    letters[char] += 1
for step in range(40):
    temp_pairs = copy(pairs)
    for pair in temp_pairs:
        if temp_pairs[pair] > 0:
            pairs[subs[pair][0]] += temp_pairs[pair]
            pairs[subs[pair][1]] += temp_pairs[pair]
            pairs[pair] -= temp_pairs[pair]
            letters[new_letter[pair]] += temp_pairs[pair]
letters = {key: value for key, value in letters.items() if value > 0}
print(f'the answer to part 2 is {max(letters.values()) - min(letters.values())}')