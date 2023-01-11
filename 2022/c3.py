import string

priority = dict(zip(string.ascii_letters, range(1, 53)))

with open('i3.txt') as f:
    data = f.readlines()
    
part1 = 0
for d in data:
    split = int(len(d.strip('\n'))/2)
    first = set(d[:split])
    second = set(d[split:])
    common = list(first & second)[0]
    part1 += priority[common]

part2 = 0
for i in range(0, len(data), 3):
    first, second, third = data[i: i+3]
    first = set(first.strip('\n'))
    second = set(second.strip('\n'))
    third = set(third.strip('\n'))
    common = list(first & second & third)[0]
    part2 += priority[common]
    
print(f'the answer for part 1 is {part1}')
print(f'the answer for part 2 is {part2}')