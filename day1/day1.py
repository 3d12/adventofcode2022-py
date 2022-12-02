from ..file_reader import read_file_into_list

def strip_newline(line):
    return line.replace('\n','')

input_list = read_file_into_list('day1/input.txt', strip_newline)

elf_totals = []
current_total = 0

for line in input_list: # pyright: ignore
    if line == '':
        elf_totals.append(current_total)
        current_total = 0
    else:
        current_total += int(line)

elf_totals.append(current_total)

print(f"The answer is: {max(elf_totals)}")
