import re

with open('i7.txt') as f:
    data = f.read().split('\n')

dir_size = {'/': 0}
dir_map = {'/': ['/']}
current_path = ['/']

new_dir = r'\$ cd [a-z]+'
up_dir = r'\$ cd ..'
dir_name = r'dir [a-z]+'
file_name = r'[0-9]+'
home = r'\$ cd /'

for d in data:
    if re.search(new_dir, d):
        _, _, name = d.split(' ')
        current_path.append(name)
        if '-'.join(current_path) not in dir_map:
            dir_size['-'.join(current_path)] = 0
            dir_map['-'.join(current_path)] = []
        for i, _ in enumerate(current_path):
            if '-'.join(current_path) not in dir_map['-'.join(current_path[:i + 1])]:
                dir_map['-'.join(current_path[:i + 1])].append('-'.join(current_path))
    elif re.search(up_dir, d):
        current_path.pop()
    elif re.search(file_name, d):
        size, _ = d.split(' ')
        size = int(size)
        dir_size['-'.join(current_path)] += size
    elif re.search(home, d):
        if '/' not in dir_map:
            dir_size['-'.join(current_path)] = 0
            dir_map['-'.join(current_path)] = []
        current_path = ['/']
        
dir_totals = [sum([dir_size[directory] for directory in v]) for k, v in dir_map.items()]
print(f'the answer to part 1 is {sum([directory for directory in dir_totals if directory < 100000])}')

totals = {k: sum([dir_size[directory] for directory in v]) for k, v in dir_map.items()}
target = 30000000 - (70000000 - totals['/'])
print(f'the answer to part 2 is {sorted([v for k, v in totals.items() if v > target])[0]}')