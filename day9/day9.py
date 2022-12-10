from ..file_reader import read_file_into_list

def parse(line):
    line_stripped = line.replace('\n','')
    line_split = line_stripped.split()
    return { 'direction': line_split[0], 'distance': int(line_split[1]) }

class RopeGrid:
    def __init__(self):
        self.head_coords = (0,0)
        self.tail_coords = (0,0)
        self.tail_visited = [(0,0)]

    def processInstruction(self, instruction):
        # move head according to instruction (one step)
        for _ in range(instruction['distance']):
            old_head_coords = self.head_coords
            self.move("head", instruction['direction'], 1)
            # ... then update the tail position (for each step)
            if not self.areHeadAndTailNeighbors():
                self.tail_coords = old_head_coords
                if self.tail_coords not in self.tail_visited:
                    self.tail_visited.append(self.tail_coords)
        pass

    def move(self, rope_section, direction, distance):
        startPos = (self.head_coords if rope_section == "head" else self.tail_coords)
        endPos = startPos
        if direction == "R":
            endPos = (startPos[0]+distance, startPos[1])
        elif direction == "DR":
            endPos = (startPos[0]+distance, startPos[1]+distance)
        elif direction == "D":
            endPos = (startPos[0], startPos[1]+distance)
        elif direction == "DL":
            endPos = (startPos[0]-distance, startPos[1]+distance)
        elif direction == "L":
            endPos = (startPos[0]-distance, startPos[1])
        elif direction == "UL":
            endPos = (startPos[0]-distance, startPos[1]-distance)
        elif direction == "U":
            endPos = (startPos[0], startPos[1]-distance)
        elif direction == "UR":
            endPos = (startPos[0]+distance, startPos[1]-distance)
        else:
            return ValueError
        if rope_section == "head":
            self.head_coords = endPos
        elif rope_section == "tail":
            self.tail_coords = endPos
        else:
            return ValueError

    def areHeadAndTailNeighbors(self):
        # based on head_coords and tail_coords, are they next to each other (include diagonal and sharing a space)
        return (abs(self.head_coords[0] - self.tail_coords[0]) <= 1 and abs(self.head_coords[1] - self.tail_coords[1]) <= 1)

    def countTailVisitedSpaces(self):
        return len(self.tail_visited)

input_list = read_file_into_list('day9/input.txt', parse)

newGrid = RopeGrid()

for instruction in input_list: # pyright: ignore
    newGrid.processInstruction(instruction)

answer = newGrid.countTailVisitedSpaces()

print(f"The answer is: {answer}")
