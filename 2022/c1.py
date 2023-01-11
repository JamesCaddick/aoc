with open('i1.txt') as f:
    data = f.read()
answer = [[int(food) for food in elf.split('\n')] for elf in data.split('\n\n')]
answer = [sum(elf) for elf in answer]
print(f'the answer to part 1 is {max(answer)}')
print(f'the answer to part 2 is {sum(sorted(answer)[-3:])}')