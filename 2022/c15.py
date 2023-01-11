import re
import matplotlib.pyplot as plt
import matplotlib.patches as patches 

def get_perimeter(sensor, distance):
    perimeter = set()
    for x in range(-distance, distance + 1):
        sx, sy = sensor
        y = distance - abs(x)
        perimeter.add((sx + x, sy + y))
        perimeter.add((sx + x, sy - y))
    return perimeter

def check_distance(upper, mulitple):
    for sensor, distance in zip(sensors, distances):
        sx, sy = sensor
        test_perimeter = get_perimeter((sx, sy), distance + 1)
        for point in test_perimeter:
            status = False
            px, py = point
            for s, d in zip(sensors, distances):
                ax, ay = s
                if abs(ax - px) + abs(ay - py) <= d:
                    status = True
            if not status and 0 <= px <= upper and 0 <= py <= upper:
                return px * mulitple + py

with open('i15.txt') as f:
    data = f.read().split('\n')
    
sensors = []
distances = []
pattern = r'[x|y]=(-*[0-9]+)'
for d in data:
    sx, sy, bx, by = [int(c) for c in re.findall(pattern, d)]
    distance = abs(sx - bx) + abs(sy - by)
    distances.append(distance)
    sensors.append((sx, sy))
    
answer = check_distance(4000000, 4000000)
print(answer)

# part 1

beacons = []
x_target = 10
pattern = r'[x|y]=(-*[0-9]+)'
blanks = []
n_blanks = 0
for d in data:
    sy, sx, by, bx = [int(c) for c in re.findall(pattern, d)]
    beacons.append((bx, by))
    distance = abs(sx - bx) + abs(sy - by)
    if abs(sx - x_target) <= distance:
        y_offset = distance - abs(sx - x_target)
        blanks.append((sy - y_offset, sy + y_offset + 1))
    blanks = sorted(blanks, key=lambda x: x[0])
max_y = -999999999
for b in blanks:
    low, high = b
    if low > max_y:
        n_blanks += high - low
        max_y = high
    elif low < max_y and high > max_y:
        n_blanks += high - max_y
        max_y = high
tracked_beacons = []
for beacon in beacons:
    x, y = beacon
    if x == x_target:
        if (x, y) not in tracked_beacons:
            tracked_beacons.append((x, y))
            for blank in blanks:
                a, b = blank
                if a <= y <= b:
                    n_blanks -= 1
                    break

print(n_blanks)