with open('i10.txt') as f:
    data = f.read().split('\n')

cycle = 1
x = 1
interesting = []
crt_rows = ''
for d in data:
    if d == 'noop':
        cycle += 1
        if (cycle - 1) % 40 == x - 1 or (cycle - 1) % 40 == x or (cycle - 1) % 40 == x + 1:
            crt_rows += '#'
        else:
            crt_rows += '.'
        if cycle in [20, 60, 100, 140, 180, 220]:
            interesting.append(cycle * x)
    else:
        _, v = d.split(' ')
        v = int(v)
        cycle += 1
        if (cycle - 1) % 40 == x - 1 or (cycle - 1) % 40 == x or (cycle - 1) % 40 == x + 1:
            crt_rows += '#'
        else:
            crt_rows += '.'
        if cycle in [20, 60, 100, 140, 180, 220]:
            interesting.append(cycle * x)
        cycle += 1
        x += v
        if (cycle - 1) % 40 == x - 1 or (cycle - 1) % 40 == x or (cycle - 1) % 40 == x + 1:
            crt_rows += '#'
        else:
            crt_rows += '.'
        if cycle in [20, 60, 100, 140, 180, 220]:
            interesting.append(cycle * x)

print(f'the answer to part 1 is {sum(interesting)}\n')

print(crt_rows[0:40])
print(crt_rows[40:80])
print(crt_rows[80:120])
print(crt_rows[120:160])
print(crt_rows[160:200])
print(crt_rows[200:240])
