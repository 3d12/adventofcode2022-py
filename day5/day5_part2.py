from ..file_reader import read_file_into_list

def parse(line):
    line_stripped = line.replace('\n','')
    return line_stripped

class BoxYard:

    def __init__(self, data):
        box_list = []
        instructions_start_index = 0
        for i in range(len(data)):
            line = data[i]
            parsed = self.parseBoxesFromLine(line)
            if len(parsed) == 0:
                instructions_start_index = i+2
                break
            box_list.append(parsed)

        # transpose parsed rows into lists by column, from bottom up
        transposed_box_list = []
        for i in range(len(box_list)+1):
        #for i in range(len(box_list)):
            transposed_box_list.append([])
        i = len(box_list)-1
        while i >= 0:
            for j in range(len(box_list[i])):
                if box_list[i][j] is not None:
                    transposed_box_list[j].append(box_list[i][j])
            i -= 1
        self.box_list = transposed_box_list

        # parse and store instructions
        instructions = []
        for i in range(instructions_start_index, len(data)):
            split_line = data[i].split()
            instructions.append({ 'num': split_line[1], 'from': split_line[3], 'to': split_line[5] })
        self.instructions = instructions


    def parseBoxesFromLine(self, line):
        box_line = []
        for i in range(0,len(line),4):
            box = line[i:i+4]
            contents = box[1]
            if contents == ' ':
                box_line.append(None)
            else:
                if not (contents.islower() or contents.isnumeric()):
                    box_line.append(contents)
        return box_line
    
    def displayBoxes(self):
        for line in self.box_list:
            for i in range(len(line)):
                elem = line[i]
                if elem is None:
                    print('   ', end='')
                else:
                    print(f'[{elem}]', end='')
                if i != len(line)-1:
                    print(' ', end='')
            print()

    def moveBoxes(self, instruction):
        source = self.box_list[int(instruction['from'])-1]
        dest = self.box_list[int(instruction['to'])-1]
        slice_point = int(instruction['num']) * -1
        copy_item = source[slice_point:]
        self.box_list[int(instruction['from'])-1] = source[:slice_point]
        dest += copy_item

    def getKeyword(self):
        keyword = ''
        for column in self.box_list:
            keyword += column[-1]
        return keyword


input_list = read_file_into_list('day5/input.txt', parse)


yard = BoxYard(input_list)
yard.displayBoxes()
print('---')

for instruction in yard.instructions:
    yard.moveBoxes(instruction)
    yard.displayBoxes()
    print('---')

print(f"The answer is: {yard.getKeyword()}")
