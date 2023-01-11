with open('i4.txt') as f:
    data = f.readlines()
    
part1 = 0
part2 = 0

for d in data:
    a, b = d.strip('\n').split(',')
    a_low, a_high = a.split('-')
    b_low, b_high = b.split('-')
    if (min(int(a_low), int(b_low)), max(int(a_high), int(b_high))) in [(int(a_low), int(a_high)), (int(b_low), int(b_high))]:
        part1 += 1
    if (int(a_low) <= int(b_low) <= int(a_high)) or (int(a_low) <= int(b_high) <= int(a_high)):
        part2 += 1
    elif (int(b_low) <= int(a_low) <= int(b_high)) or (int(b_low) <= int(a_high) <= int(b_high)):
        part2 += 1
        
print(f'the answer to part 1 is {part1}')
print(f'the answer to part 2 is {part2}')