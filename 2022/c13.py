
def compare_again(left, right):
    pass

def compare(left, right=[]):
    result = 0
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            result = 1
        elif left > right:
            result = -1
    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            result = compare(l, r)
            if result == 1 or result == -1:
                return result
        if len(left) < len(right):
            result = 1
        elif len(left) > len(right):
            result = -1    
    elif isinstance(left, int) and isinstance(right, list):
        result = compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        result = compare(left, [right])
    return result

def sort_pairs(sorted_data, new):
    for i, pair in enumerate(sorted_data):
        status = compare(eval(new), eval(pair))
        if status == 1:
            sorted_data.insert(i, new)
            return sorted_data
    sorted_data.append(new)
    return sorted_data

with open('i13.txt') as f:
    data = [d.split('\n') for d in f.read().split('\n\n')]
indeces = []
for i, d in enumerate(data):
    left = eval(d[0])
    right = eval(d[1])
    status = compare(left, right)
    if status == 1:
        indeces.append(i + 1)
        
data = [p for pair in data for p in pair]
data.extend(['[[2]]', '[[6]]'])

sorted_data = [data.pop()]
while data:
    new_pair = data.pop()
    sorted_data = sort_pairs(sorted_data, new_pair)

print(f'the answer to part 1 is {sum(indeces)}')
print(f'the answer to part  2 is {(sorted_data.index("[[2]]") + 1) * (sorted_data.index("[[6]]") + 1)}')