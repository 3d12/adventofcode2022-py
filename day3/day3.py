from ..file_reader import read_file_into_list

def parse(line):
    line_stripped = line.replace('\n','')
    return line_stripped

input_list = read_file_into_list('day3/input.txt', parse)

letter_val_total = 0
for rucksack in input_list: # pyright: ignore
    total_rucksack_size = len(rucksack)
    compartment_divider = int(total_rucksack_size/2)
    compartment1 = rucksack[:compartment_divider]
    compartment2 = rucksack[compartment_divider:]
    print(f"Testing {rucksack} -- compartment1: {compartment1}, compartment2: {compartment2}")
    for letter in compartment1:
        if letter in compartment2:
            print(f"Shared letter: {letter}")
            ascii_val = ord(letter)
            letter_val = 0
            if ascii_val >= 97:
                letter_val = ascii_val-96
            else:
                letter_val = ascii_val-38
            letter_val_total += letter_val
            print(f"Value: {letter_val}")
            break

print(f"The answer is: {letter_val_total}")
