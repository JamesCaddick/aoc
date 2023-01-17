import re
import heapq
from itertools import combinations

with open('i16.txt') as f:
    data = f.read().split('\n')

node_pttn = r'Valve ([A-Z]+)'
flow_pttn = r'rate=([0-9]+)'
child_pttn = r'[A-Z]{2}'

network = {}
valves = {}
for d in data:
    node = re.search(node_pttn, d)[1]
    flow = re.search(flow_pttn, d)[1]
    children = re.findall(child_pttn, d)[1:]
    network[node] = children
    valves[node] = int(flow)
    
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
    
memo = {}
def search_network(time, node, valve_state):
    # if have seen state before, return state from memo
    if (time, node, valve_state) in memo:
        return memo[(time, node, valve_state)]
    max_pressure = 0
    # check each non-zero node
    for i, new_node in enumerate(non_zero_nodes):
        # if the node is already open or node is same as current node then skip it
        if valve_state[i] or new_node == node:
            continue
        # calculate remaining time after moving to node and opening it
        remaining = time - distances[tuple(sorted([node, new_node]))] - 1
        # if not enough time to reach the node then skip
        if remaining <= 0:
            continue
        # change valve state
        new_valve_state = tuple([1 if j == i else state for j, state in enumerate(valve_state)])
        # calculate new max pressure
        max_pressure = max(max_pressure, search_network(remaining, new_node, new_valve_state) + remaining * valves[new_node])
    # update memo
    memo[(time, node, valve_state)] = max_pressure
    return max_pressure
    
# create dictionary of distances between nodes with non-zero flow rates (and start node)
non_zero_nodes = [node for node, flow in valves.items() if flow > 0 or node == 'AA']
combos = list(combinations(non_zero_nodes, 2))
distances = {tuple(sorted(combo)):dijkstra(combo[0], combo[1]) for combo in combos}

# set valve state for nodes
valve_state = tuple([0] * len(network))

# run search
print(search_network(30, 'AA', valve_state))

# part 2
max_partnership = 0
all_nodes_except_aa = set(non_zero_nodes) - set('AA')
for n in range(0, len(all_nodes_except_aa) + 1):
    for combo in combinations(all_nodes_except_aa, n):
        elephant = all_nodes_except_aa - set(combo)
        me_valve_state = tuple([1 if node in elephant else 0 for node in non_zero_nodes])
        elephant_valve_state = tuple([1 if node in combo else 0 for node in non_zero_nodes])
        max_partnership = max(max_partnership, search_network(26, 'AA', me_valve_state) + search_network(26, 'AA', elephant_valve_state))

print(max_partnership)