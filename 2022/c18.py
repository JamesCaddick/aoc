import heapq

def is_external(xyz, internals):
    to_do_set = set()
    done_set = set()
    to_do_set.add(xyz)
    while len(to_do_set) > 0:
        node = to_do_set.pop()
        done_set.add(node)
        neighbours = get_neighbours(node)
        for neighbour in neighbours:
            x, y, z = neighbour
            if x == 21 or y == 21 or z == 21:
                return True, internals
            elif neighbour in internals:
                return False, internals
            if neighbour not in done_set:
                to_do_set.add(neighbour)
    internals.add(xyz)
    return False, internals
        
def get_neighbours(xyz):
    x, y, z = xyz
    offsets = [[0, 0, 1],
               [0, 1, 0],
               [1, 0, 0],
               [0, 0, -1],
               [0, -1, 0],
               [-1, 0, 0]]
    neighbours = set()
    for offset in offsets:
        a, b, c = offset
        if (x + a, y + b, z + c) not in data:
            neighbours.add((x + a, y + b, z + c))
    return neighbours

with open('i18.txt') as f:
    data = f.read().splitlines()
data = [tuple([int(x) for x in row.split(',')]) for row in data]

surfaces = 0
external_surfaces = 0
offsets = [[0, 0, 1],
           [0, 1, 0],
           [1, 0, 0],
           [0, 0, -1],
           [0, -1, 0],
           [-1, 0, 0]]

internals = set()
for i, d in enumerate(data):
    x, y, z = d
    for offset in offsets:
        a, b, c = offset
        if (a + x, b + y, c + z) not in data:
            surfaces += 1
            status, internals = is_external((a + x, b + y, c + z), internals)
            if status:
                external_surfaces += 1
    print(i)

print(surfaces)
print(external_surfaces)