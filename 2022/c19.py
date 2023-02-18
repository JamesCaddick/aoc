import re
import heapq

def get_neighbours(blueprint, state):
    time, ore, clay, obsidian, geodes, ore_robots, clay_robots, obsidian_robots, geode_robots = state
    id, ore_r_ore_cost, clay_r_ore_cost, obsidian_r_ore_cost, obsidian_r_clay_cost, geode_r_ore_cost, geode_r_obsidian_cost = blueprint
 
memo = {}
def maximise_geodes(state=(24, 0, 0, 0, 1, 0, 0, 0)):
    time, ore, clay, obsidian, ore_robots, clay_robots, obsidian_robots, geode_robots = state
    # if have seen state before, return state from memo
    if state in memo:
        return memo[state]
    # check each non-zero node
    for neighbour in get_neighbours(state):
        time, _ = neighbour
        geodes = memo[neighbour]
        # if not enough time to reach the node then skip
        if time <= 0:
            continue
        # calculate new max pressure
        geodes = max(geodes, maximise_geodes(neighbour))
    # update memo
    memo[state] = geodes
    return geodes

with open('i19t.txt') as f:
    data = f.read().split('\n')
    
quality = []
for d in data:
    blueprint = [int(v) for v in re.findall(r'\d+', d)]
    geodes = maximise_geodes()
    quality.append(blueprint * geodes)

