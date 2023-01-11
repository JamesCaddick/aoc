import re
from copy import copy
import heapq

with open('i16t.txt') as f:
    data = f.read().split('\n')

node_pttn = r'Valve ([A-Z]+)'
flow_pttn = r'rate=([0-9]+)'
child_pttn = r'[A-Z]{2}'

nodes = []
flows = []
kids = []
for d in data:
    node = re.search(node_pttn, d)[1]
    flow = re.search(flow_pttn, d)[1]
    children = re.findall(child_pttn, d)[1:]
    nodes.append(node)
    flows.append(flow)
    kids.append(children)
    
network = {k:v for k, v in zip(nodes, kids)}
node_flow = {k:[int(v), True] for k, v in zip(nodes, flows)}

def get_weighted_distances(node):
    weighted_distances = {k: dijkstra(k, node) * node_flow[k][0] * node_flow[k][1] for k, v in network.items()}
    # print(f'{node}: {weighted_distances}, {sum(weighted_distances.values())}')
    return sum(weighted_distances.values())
    
def get_neighbours(node):
    return network[node]

def update_paths(tentative, neighbours, candidate):
    length = tentative[candidate] + 1
    for n in neighbours:
        if n in tentative and length >= tentative[n]:
            continue
        yield n, length

def dijkstra(origin, destination):
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
        neighbours = set(get_neighbours(candidate)) - certain
        # get updated shortest paths
        updates = update_paths(tentative, neighbours, candidate)
        # update paths to neighbours
        for pos, length in updates:
            tentative[pos] = length
            heapq.heappush(candidates, (length, pos))
    # return shortest path to destination
    if destination in tentative:
        return tentative[destination]
    
time = 0
current_node = 'DD'
# while time < 29:
node_flow['DD'][1] = False

# find candidates
candidates = get_neighbours(current_node)
# check distance between each candidate and every other closed node (that is reachable in 28 mins or less)
distances = {candidate:get_weighted_distances(candidate) for candidate in candidates}
# select the candidate with the lowest weighted distance
chosen_candidate = min(distances, key=distances.get)

print(chosen_candidate)