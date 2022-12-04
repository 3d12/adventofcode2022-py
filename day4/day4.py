from ..file_reader import read_file_into_list

def parse(line):
    line_stripped = line.replace('\n','')
    pair_split = [pair.split('-') for pair in line_stripped.split(',')]
    conv_to_int = [[int(num) for num in pair] for pair in pair_split]
    return conv_to_int

def listCompare(list1, list2):
    list1in2 = True
    for elem in list1:
        if elem not in list2:
            list1in2 = False
            break
    list2in1 = True
    for elem in list2:
        if elem not in list1:
            list2in1 = False
            break
    return (list1in2 or list2in1)


input_list = read_file_into_list('day4/input.txt', parse)

nested_list_count = 0
for pair in input_list: # pyright: ignore
    range1 = range(pair[0][0], pair[0][1]+1)
    range2 = range(pair[1][0], pair[1][1]+1)
    if (listCompare(range1, range2)):
        nested_list_count += 1

print(f"The answer is {nested_list_count}")
