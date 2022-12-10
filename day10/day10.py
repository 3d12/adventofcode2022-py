from ..file_reader import read_file_into_list

def parse(line):
    line_stripped = line.replace('\n','')
    line_split = line_stripped.split()
    if len(line_split) == 1:
        return { 'action': line_split[0], 'value': 0, 'cycles': 1 }
    else:
        return { 'action': line_split[0], 'value': int(line_split[1]), 'cycles': 2 }

input_list = read_file_into_list('day10/input.txt', parse)

register_x = 1
cycle_count = 0
cycle_breakpoints = {'20': 0, '60': 0, '100': 0, '140': 0, '180': 0, '220': 0}

for instruction in input_list: # pyright: ignore
    for _ in range(instruction['cycles']):
        cycle_count += 1
        if str(cycle_count) in cycle_breakpoints:
            cycle_breakpoints[str(cycle_count)] = (register_x * cycle_count)
    if instruction['action'] == 'addx':
        register_x += instruction['value']

print(f"The answer is {sum(cycle_breakpoints.values())}")
