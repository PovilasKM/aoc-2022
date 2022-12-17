import re
import time

lines = open('data.txt', "r").read().split("\n")
pattern = r"Valve ([A-Z]{2}) has flow rate=([-+]?[0-9]+); tunnel[s]? lead[s]? to valve[s]? ([A-Z, ].*)"
routes = {}
points = []
for line in lines:
    g = re.search(pattern, line.strip())
    route_from = g.group(1)
    points.append(route_from)
    rate = int(g.group(2))
    destinations = [item.strip() for item in g.group(3).split(",")]
    routes[route_from] = (rate, destinations)

distances = {current: {point: 999 for point in points if point != current} for current in points}

for point in points:
    neighbours = routes[point][1]
    distance = 1
    while len(neighbours):
        new_neighbours = set()
        for neighbour in neighbours:
            if point != neighbour and distances[point][neighbour] > distance:
                distances[point][neighbour] = distance
                new_neighbours.update(routes[neighbour][1])

        neighbours = new_neighbours
        distance += 1

# prune
points = [point for point in points if routes[point][0] != 0]


def simulate(minutes_left, current_point, used_points):
    if minutes_left <= 0:
        return 0
    pressures = []
    for point in points:
        if point in used_points:
            continue
        if point == current_point:
            continue
        distance = distances[current_point][point]
        if minutes_left - distance <= 0:
            continue
        used_points.append(point)
        pressure = (minutes_left - distance - 1) * routes[point][0]
        pressures.append(pressure + simulate(minutes_left-distance-1, point, used_points))
        used_points.pop()

    return max(pressures, default=0)


start_time = time.time()
print(simulate(30, "AA", []))
print("--- %s seconds ---" % (time.time() - start_time))
