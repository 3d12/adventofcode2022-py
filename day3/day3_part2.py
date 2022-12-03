from ..file_reader import read_file_into_list

def parse(line):
    line_stripped = line.replace('\n','')
    return line_stripped

input_list = read_file_into_list('day3/input.txt', parse)

letter_val_total = 0
group_counter = 1
for i in range(0, len(input_list), 3): # pyright: ignore
    print(i)
    rucksack = input_list[i] # pyright: ignore
    rucksack2 = input_list[i+1] # pyright: ignore
    rucksack3 = input_list[i+2] # pyright: ignore
    print(f"Group {group_counter}:")
    print(f"{rucksack} -- {rucksack2} -- {rucksack3}")
    group_counter += 1
    for letter in rucksack:
        if letter in rucksack2 and letter in rucksack3:
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
