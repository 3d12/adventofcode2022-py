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
        if x == self.nearest_beacon_location.x and y == self.nearest_beacon_location.y:
            return False
        x_dist = abs(x - self.location.x)
        remaining = self.coverage_radius - x_dist
        return (abs(y - self.location.y) <= remaining)

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
min_sensor_x = min([e.location.x-e.coverage_radius for e in sensors])
min_sensor_y = min([e.location.y-e.coverage_radius for e in sensors])
max_sensor_x = max([e.location.x+e.coverage_radius for e in sensors])
max_sensor_y = max([e.location.y+e.coverage_radius for e in sensors])

print(f"DEBUG: min_sensor_x:{min_sensor_x}, max_sensor_x:{max_sensor_x}, min_sensor_y:{min_sensor_y}, max_sensor_y:{max_sensor_y}")
min_beacon_x = min([e.nearest_beacon_location.x for e in sensors])
min_beacon_y = min([e.nearest_beacon_location.y for e in sensors])
max_beacon_x = max([e.nearest_beacon_location.x for e in sensors])
max_beacon_y = max([e.nearest_beacon_location.y for e in sensors])

print(f"DEBUG: min_beacon_x:{min_beacon_x}, max_beacon_x:{max_beacon_x}, min_beacon_y:{min_beacon_y}, max_beacon_y:{max_beacon_y}")

grid_min_x = min_sensor_x if min_sensor_x < min_beacon_x else min_beacon_x
grid_max_x = max_sensor_x if max_sensor_x > max_beacon_x else max_beacon_x
grid_min_y = min_sensor_y if min_sensor_y < min_beacon_y else min_beacon_y
grid_max_y = max_sensor_y if max_sensor_y > max_beacon_y else max_beacon_y

print(f"DEBUG: grid_min_x:{grid_min_x}, grid_max_x:{grid_max_x}, grid_min_y:{grid_min_y}, grid_max_y:{grid_max_y}")

row = 2000000 
coveredSpaces = 0
for x in range(grid_min_x, grid_max_x+1):
    print(f"DEBUG: testing ({x},{row})")
    for sensor in sensors:
        if sensor.covered(x, row):
            print(f"DEBUG: ({x},{row}) covered by sensor {sensor}")
            coveredSpaces += 1
            break
print(f"The answer is {coveredSpaces}")
