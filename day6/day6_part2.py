from ..file_reader import read_file_into_list

def parse(line):
    line_stripped = line.replace('\n','')
    return line_stripped

input_list = read_file_into_list('day6/input.txt', parse)

text = input_list[0] # pyright: ignore

packet_start_index = 0
for i in range(len(text)):
    packet_string = text[i:i+14]
    packet_start_test = True
    for j in range(len(packet_string)):
        char = packet_string[j]
        rest_of_list = packet_string[j+1:]
        if char in rest_of_list:
            packet_start_test = False
            break
    if packet_start_test == True:
        packet_start_index = i+14
        break

print(f"The answer is: {packet_start_index}")
