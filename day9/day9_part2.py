from ..file_reader import read_file_into_list

def parse(line):
    line_stripped = line.replace('\n','')
    line_split = line_stripped.split()
    return { 'direction': line_split[0], 'distance': int(line_split[1]) }

class RopeGrid:
    def __init__(self):
        self.coords = [(0,0)] * 10
        self.tail_visited = [(0,0)]

    def processInstruction(self, instruction):
        # move head according to instruction (one step)
        for _ in range(instruction['distance']):
            self.move(0, instruction['direction'], 1)
            # ... then update all the other positions (for each step)
            for i in range(1, len(self.coords)):
                coord = self.coords[i]
                if not self.areTwoNodesNeighbors(self.coords[i-1], coord):
                    newDirection = self.directionBetweenTwoNodes(coord, self.coords[i-1])
                    self.move(i, newDirection, 1)
                    if i == 9:
                        if self.coords[i] not in self.tail_visited:
                            self.tail_visited.append(self.coords[i])

    def move(self, rope_section, direction, distance):
        startPos = self.coords[rope_section]
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
        if rope_section < len(self.coords):
            self.coords[rope_section] = endPos
        else:
            return ValueError

    def areTwoNodesNeighbors(self, node1, node2):
        return (abs(node1[0] - node2[0]) <= 1 and abs(node1[1] - node2[1]) <= 1)

    def directionBetweenTwoNodes(self, node1, node2):
        if (node1[0] == node2[0] and node1[1] > node2[1]):
            return "U"
        elif (node1[0] == node2[0] and node1[1] < node2[1]):
            return "D"
        elif (node1[1] == node2[1] and node1[0] > node2[0]):
            return "L"
        elif (node1[1] == node2[1] and node1[0] < node2[0]):
            return "R"
        elif (node1[0] > node2[0] and node1[1] > node2[1]):
            return "UL"
        elif (node1[0] < node2[0] and node1[1] > node2[1]):
            return "UR"
        elif (node1[0] > node2[0] and node1[1] < node2[1]):
            return "DL"
        elif (node1[0] < node2[0] and node1[1] < node2[1]):
            return "DR"
        else:
            return ValueError


    def countTailVisitedSpaces(self):
        return len(self.tail_visited)

input_list = read_file_into_list('day9/input.txt', parse)

newGrid = RopeGrid()


for instruction in input_list: # pyright: ignore
    newGrid.processInstruction(instruction)

answer = newGrid.countTailVisitedSpaces()

print(f"The answer is: {answer}")
