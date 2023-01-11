import re

with open('i9.txt') as f:
    data = f.read()
    
# data = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'

marker = True
decompressed = ''
while marker:
    marker = re.search(r'\((.*?)\)', data)
    if marker:
        start, end = marker.span()
        length, multiples = marker[1].split('x')
        decompressed += data[:start]
        repeat = data[end:end + int(length)]
        data = repeat * int(multiples) + data[end + int(length):]
    else:
        decompressed += data
    # print(len(data))
    print(decompressed)
print(len(decompressed))