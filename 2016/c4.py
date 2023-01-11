with open('i4.txt') as f:
    data = f.readlines()
data = [d.strip().split('-') for d in data]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
valid = 0
for room in data:
    char_count = {}
    name = ''.join(room[:-1])
    name2 = ' '.join(room[:-1])
    unique_chars = set(name)
    for char in unique_chars:
        char_count[char] = name.count(char)
    char_count = ''.join([k for k, v in sorted(char_count.items(), key=lambda item: (-item[1], item[0]))][:5])
    checksum = room[-1].split('[')[1][:-1]
    id_num = int(room[-1].split('[')[0])
    if checksum == char_count:
        valid += id_num
    shift = id_num % 26
    name3 = ''
    for n in name2:
        if n == ' ':
            name3 = name3 + ' '
        elif shift + alphabet.index(n) >= 25:
            i = shift + alphabet.index(n) - 25
            name3 = name3 + alphabet[i-1]
        else:
            i = shift + alphabet.index(n)
            name3 = name3 + alphabet[i]
    print(f'{name3}, {id_num}')