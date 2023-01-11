import numpy as np

with open('i6.txt') as f:
    data = f.readlines()
data = np.array([list(d.strip()) for d in data])
answer = ''
for i in range(data.shape[1]):
    unique, counts = np.unique(data[:, i], return_counts=True)
    answer += unique[np.argmin(counts)]