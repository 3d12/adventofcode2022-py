from ..file_reader import read_file_into_list

def parse(line):
    line = line.replace('\n','')
    line_split = line.split(' -> ')
    points_split = [e.split(',') for e in line_split]
    points_tupled = [(int(e[0]), int(e[1])) for e in points_split]
    return points_tupled

class SandGrid:
    def __init__(self, data):
        self.input_data = data
        self.lines = []
        for pointsGroup in self.input_data:
            self.lines.append(self.parsePointsGroupToLines(pointsGroup))
        self.filled_lines = []
        for line in self.lines:
            tmpLine = []
            for coordPair in line:
                tmpLine.append(self.lineFill(coordPair))
            self.filled_lines.append(tmpLine)
        self.min_x = 99999
        self.max_x = 0
        self.min_y = 99999
        self.max_y = 0
        for line in self.lines:
            for coordPair in line:
                for x,y in coordPair:
                    if x < self.min_x:
                        self.min_x = x
                    if x > self.max_x:
                        self.max_x = x
                    if y < self.min_y:
                        self.min_y = y
                    if y > self.max_y:
                        self.max_y = y
        self.x_diff = self.max_x-self.min_x
        self.y_diff = self.max_y-self.min_y
        self.grid = []
        for y in range(self.max_y+1):
            self.grid.append('.' * (self.max_x+1))
        #print(f"DEBUG: self.filled_lines={self.filled_lines}")
        self.grid_w_structs = self.placeRockStructuresOntoGrid(self.filled_lines)
        self.sand = []

    def __str__(self):
        tmpStr = ''
        for displayLine in self.grid_w_structs:
            displayRegion = displayLine[self.min_x-1:]
            tmpStr += displayRegion + '\n'
        return tmpStr

    def dropSand(self):
        self.sandPath = []
        self.overflow = False
        while not self.overflow:
            self.sandPath = []
            self.sandPath.append((500,0))
            self.stable = False
            while not self.stable:
                current_pos = self.sandPath[-1]
                if current_pos[1] >= self.max_y:
                    self.stable = True
                    self.overflow = True
                    break
                char_below = self.getCharacter(current_pos[0], current_pos[1]+1)
                if char_below in ['o','#']:
                    char_below_left = self.getCharacter(current_pos[0]-1, current_pos[1]+1)
                    if char_below_left in ['o','#']:
                        char_below_right = self.getCharacter(current_pos[0]+1, current_pos[1]+1)
                        if char_below_right in ['o','#']:
                            self.stable = True
                            self.putSand(current_pos[0], current_pos[1])
                            self.sand.append((current_pos[0], current_pos[1]))
                            break
                        else:
                            self.sandPath.append((current_pos[0]+1, current_pos[1]+1))
                    else:
                        self.sandPath.append((current_pos[0]-1, current_pos[1]+1))
                else:
                    self.sandPath.append((current_pos[0], current_pos[1]+1))



    def getCharacter(self, x, y):
        return self.grid_w_structs[y][x]

    def putSand(self, x, y):
        tmpLine = self.grid_w_structs[y]
        self.grid_w_structs[y] = tmpLine[:x] + 'o' + tmpLine[x+1:]



    def parsePointsGroupToLines(self, pointsGroup):
        lines = []
        for i in range(len(pointsGroup)-1):
            point1 = pointsGroup[i]
            point2 = pointsGroup[i+1]
            lines.append((point1, point2))
        return lines
    
    def lineFill(self, line_coords):
        #print(f"DEBUG: beginning lineFill on line_coords={line_coords}")
        point1 = line_coords[0]
        point2 = line_coords[1]
        x1 = point1[0]
        y1 = point1[1]
        x2 = point2[0]
        y2 = point2[1]
        # fill right
        if x1 < x2:
            #print(f"DEBUG: fill right")
            return [(e, y1) for e in range(x1, x2+1)]
        # fill down
        if y1 < y2:
            #print(f"DEBUG: fill down")
            return [(x1, e) for e in range(y1, y2+1)]
        # fill left
        if x1 > x2:
            #print(f"DEBUG: fill left")
            return [(e, y1) for e in range(x1, x2-1, -1)]
        # fill up
        if y1 > y2:
            #print(f"DEBUG: fill up")
            return [(x1, e) for e in range(y1, y2-1, -1)]
    
    def placeRockStructuresOntoGrid(self, structs):
        tmpGrid = self.grid[:]
        for struct in structs:
            for line in struct:
                for point in line:
                    newLine = tmpGrid[point[1]][:point[0]] + '#' + tmpGrid[point[1]][point[0]+1:]
                    tmpGrid[point[1]] = newLine
        # place sand drop point
        tmpGrid[0] = tmpGrid[0][:500] + '+' + tmpGrid[0][501:]
        return tmpGrid



input_list = read_file_into_list('day14/input.txt', parse)

#print(input_list)

testObj = SandGrid(input_list)
print(testObj)
testObj.dropSand()
print()
print(testObj)

print(f"The answer is {len(testObj.sand)}")
