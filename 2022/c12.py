import string
import numpy as np
from copy import copy
import heapq

def get_neighbours(coords, data):
    x_max, y_max = data.shape
    x, y = coords
    neighbours = []
    if x + 1 <= x_max - 1:
        if data[x + 1, y] <= data[x, y] + 1:
            neighbours.append((x + 1, y))
    if x - 1 >= 0:
        if data[x - 1, y] <= data[x, y] + 1:
            neighbours.append((x - 1, y))
    if y + 1 <= y_max - 1:
        if data[x, y + 1] <= data[x, y] + 1:
            neighbours.append((x, y + 1))
    if y - 1 >= 0:
        if data[x, y - 1] <= data[x, y] + 1:
            neighbours.append((x, y - 1))
    return neighbours

def update_paths(data, tentative, neighbours, candidate):
    x, y = candidate
    length = tentative[candidate] + 1
    for n in neighbours:
        if n in tentative and length >= tentative[n]:
            continue
        yield n, length

def dijkstra(data, start_pos, end_pos):
    origin = (start_pos[0], start_pos[1])
    destination = (end_pos[0], end_pos[1])
    x, y = destination
    tentative = {origin: 0}
    candidates = [(0, origin)]
    certain = set()
    while destination not in certain and len(candidates) > 0:
        # get candidate
        _ignored, candidate = heapq.heappop(candidates)
        if candidate in certain:
            continue
        # add node to certain
        certain.add(candidate)
        # find neighbours not in certain set
        neighbours = set(get_neighbours(candidate, data)) - certain
        # get updated shortest paths
        updates = update_paths(data, tentative, neighbours, candidate)
        # update paths to neighbours
        for pos, length in updates:
            tentative[pos] = length
            heapq.heappush(candidates, (length, pos))
    # return shortest path to destination
    if destination in tentative:
        return tentative[destination]

alphabet = {k:v for k, v in zip(string.ascii_lowercase, range(26))}
alphabet['S'] = 0
alphabet['E'] = 25

with open('i12.txt') as f:
    data = np.array([list(d) for d in f.read().split('\n')])
start_pos = np.argwhere(data == 'S')[0]
end_pos = np.argwhere(data == 'E')[0]
data = np.array([[alphabet[a] for a in d] for d in data])

print(dijkstra(data, start_pos, end_pos))

# what if you can't reach a destination
starts = np.argwhere(data == 0)
print(min([999 if not dijkstra(data, start, end_pos) else dijkstra(data, start, end_pos) for start in starts]))
    

