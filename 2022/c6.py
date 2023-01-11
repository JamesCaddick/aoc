with open('i6.txt') as f:
    data = f.read()
for i in range(len(data) - 14):
    if len(set(data[i: i + 14])) == 14:
        print(f'the answer to part 1 is {i + 14}')
        break