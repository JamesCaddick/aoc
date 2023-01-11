import numpy as np

with open('i3.txt') as f:
    data = f.read().split('\n')
data = [[int(t) for t in d.split()] for d in data]
data2 = np.array(data)
col1 = data2[:, 0]
col2 = data2[:, 1]
col3 = data2[:, 2]
data2 = np.split(np.concatenate((col1, col2, col3)), len(data))

i = 0
for d in data2:
    a, b, c = d
    if a + b > c and a + c > b and b + c > a:
        i += 1
print(i)