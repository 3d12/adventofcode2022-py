from ..file_reader import read_file_into_list

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Sensor:
    def __init__(self, location, nearest_beacon_location):
        self.location = location
        self.nearest_beacon_location = nearest_beacon_location
        self.coverage_radius = (abs(self.location.x - self.nearest_beacon_location.x) + abs(self.location.y - self.nearest_beacon_location.y))

    def __str__(self):
        return 'Sensor object at (' + str(self.location.x) + ',' + str(self.location.y) + ') with coverage radius ' + str(self.coverage_radius)

    def covered(self, x, y):
        x_dist = abs(x - self.location.x)
        remaining = self.coverage_radius - x_dist
        return (abs(y - self.location.y) <= remaining)

    def edge(self, min=0, max=4000000):
        coords = []
        tmp_radius = self.coverage_radius + 1
        for dist in range(tmp_radius, -1, -1):
            #print(f"DEBUG: dist={dist}")
            x_mods = (-1 * dist, dist) if dist != 0 else (dist,)
            remaining = tmp_radius - dist
            y_mods = (-1 * remaining, remaining) if remaining != 0 else (remaining,)
            #print(f"DEBUG: x_mods={x_mods}, remaining={remaining}, y_mods={y_mods}")
            for x_mod in x_mods:
                for y_mod in y_mods:
                    new_x = self.location.x + x_mod
                    new_y = self.location.y + y_mod
                    if new_x >= min and new_x <= max and new_y >= min and new_y <= max:
                        #print(f"DEBUG: {self.location.x + x_mod}, {self.location.y + y_mod}")
                        #coords.append(Point(self.location.x + x_mod, self.location.y + y_mod))
                        coords.append(Point(new_x, new_y))
        return coords


def parse(line):
    line = line.replace('\n','')
    line_split = line.split(': ')
    sensor_coords = line_split[0].split(' at ')[-1].split(', ')
    sensor_x = int(sensor_coords[0].split('=')[-1])
    sensor_y = int(sensor_coords[1].split('=')[-1])
    sensor = Point(sensor_x,sensor_y)
    beacon_coords = line_split[1].split(' at ')[-1].split(', ')
    beacon_x = int(beacon_coords[0].split('=')[-1])
    beacon_y = int(beacon_coords[1].split('=')[-1])
    beacon = Point(beacon_x,beacon_y)
    return { 'sensor': sensor, 'beacon': beacon }

input_list = read_file_into_list('day15/input.txt', parse)

sensors = [Sensor(e['sensor'], e['beacon']) for e in input_list] # pyright: ignore

edges = []
for sensor in sensors:
    print(f"DEBUG: sensor={sensor}")
    edges.append(sensor.edge())

beacon_location = None
for edge in edges:
    if beacon_location is not None:
        break
    for point in edge:
        if beacon_location is not None:
            break
        print(f"DEBUG: Checking point {point}")
        x = point.x
        y = point.y
        covered = False
        for sensor in sensors:
            if sensor.covered(x, y):
                print(f"DEBUG: Point {point} covered by sensor {sensor}")
                covered = True
                break
        if not covered:
            beacon_location = point
            break

print(f"The beacon at {beacon_location} has tuning frequency {(beacon_location.x * 4000000) + beacon_location.y}")
