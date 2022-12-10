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
#crt_rows = [['.'] * 40] * 6
crt_rows = []
for _ in range(6):
    crt_rows.append(['.'] * 40)

for instruction in input_list: # pyright: ignore
    print(f"DEBUG: executing instruction {instruction}")
    for _ in range(instruction['cycles']):
        # draw
        hpos = cycle_count % 40
        vpos = cycle_count // 40
        print(f"DEBUG: hpos={hpos}, vpos={vpos}")

        print(f"DEBUG: hpos - register_x = {hpos - register_x}")
        if abs(hpos - register_x) <= 1:
            print(f"DEBUG: updating pixel {hpos},{vpos}")
            crt_rows[vpos][hpos] = '#'

        cycle_count += 1

    if instruction['action'] == 'addx':
        register_x += instruction['value']
        print(f"DEBUG: register_x updated to {register_x}")

for line in crt_rows:
    print(''.join(line))
