from ..file_reader import read_file_into_list

def parse(line):
    line_stripped = line.replace('\n','')
    return line_stripped

def displayGrid(grid, visited, currentX, currentY):
    outputGrid = grid[:]
    for (visitedX, visitedY) in visited:
        outputGrid[visitedY] = outputGrid[visitedY][:visitedX] + '#' + outputGrid[visitedY][visitedX+1:]
    outputGrid[currentY] = outputGrid[currentY][:currentX] + '*' + outputGrid[currentY][currentX+1:]
    outputStr = ""
    for line in outputGrid:
        outputStr += line + '\n'
    print(outputStr)

def eligibleNeighbors(grid, x, y):
    up_coord = ((x, y-1) if y-1 >= 0 else None)
    up_char = (grid[up_coord[1]][up_coord[0]] if up_coord is not None else None)
    up_value = (ord('a') if up_char == 'S' else ord('z') if up_char == 'E' else ord(up_char) if up_char is not None else None)
    right_coord = ((x+1, y) if x+1 < len(grid[y]) else None)
    right_char = (grid[right_coord[1]][right_coord[0]] if right_coord is not None else None)
    right_value = (ord('a') if right_char == 'S' else ord('z') if right_char == 'E' else ord(right_char) if right_char is not None else None)
    down_coord = ((x, y+1) if y+1 < len(grid) else None)
    down_char = (grid[down_coord[1]][down_coord[0]] if down_coord is not None else None)
    down_value = (ord('a') if down_char == 'S' else ord('z') if down_char == 'E' else ord(down_char) if down_char is not None else None)
    left_coord = ((x-1, y) if x-1 >= 0 else None)
    left_char = (grid[left_coord[1]][left_coord[0]] if left_coord is not None else None)
    left_value = (ord('a') if left_char == 'S' else ord('z') if left_char == 'E' else ord(left_char) if left_char is not None else None)
    current_value = (ord('a') if grid[y][x] == 'S' else ord('z') if grid[y][x] == 'E' else ord(grid[y][x]))
    eligibleList = []
    if up_value is not None and up_value - current_value == 1:
        eligibleList.append(up_coord)
    if right_value is not None and right_value - current_value == 1:
        eligibleList.append(right_coord)
    if down_value is not None and down_value - current_value == 1:
        eligibleList.append(down_coord)
    if left_value is not None and left_value - current_value == 1:
        eligibleList.append(left_coord)
    #if len(eligibleList) > 0:
    #    return eligibleList

    if up_value is not None and up_value - current_value <= 0:
        eligibleList.append(up_coord)
    if right_value is not None and right_value - current_value <= 0:
        eligibleList.append(right_coord)
    if down_value is not None and down_value - current_value <= 0:
        eligibleList.append(down_coord)
    if left_value is not None and left_value - current_value <= 0:
        eligibleList.append(left_coord)
    return eligibleList


# implementation of wycy's answer from Tildes day 12 AoC thread
class Path:
    def __init__(self, x, y, steps):
        self.x = x
        self.y = y
        self.steps = steps
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ') (' + str(self.steps) + ' steps)'

def shortest_path(grid, startX, startY):
    visited = []
    heap = []
    heap.append(Path(startX, startY, 0))
    while len(heap) > 0:
        path = heap.pop(0)
        currentX = path.x
        currentY = path.y
        currentSteps = path.steps
        currentStr = grid[currentY][currentX]
        currentValue = (ord('a') if currentStr == 'S' else ord('z') if currentStr == 'E' else ord(currentStr))
        # debug view
        displayGrid(grid, visited, currentX, currentY)
        neighbors = eligibleNeighbors(grid, currentX, currentY)
        for neighbor in neighbors:
            neighborStr = grid[neighbor[1]][neighbor[0]]
            neighborVal = (ord('a') if neighborStr == 'S' else ord('z') if neighborStr == 'E' else ord(neighborStr))
            if neighborVal > (currentValue + 1):
                continue

            if neighbor in visited:
                continue
            visited.append(neighbor)

            newSteps = currentSteps + 1

            if neighborStr == 'E':
                return newSteps
            heap.append(Path(neighbor[0], neighbor[1], newSteps))


input_list = read_file_into_list('day12/input.txt', parse)

start = (0,0)
end = (0,0)
for y in range(len(input_list)): # pyright: ignore
    current_row = input_list[y] # pyright: ignore
    for x in range(len(current_row)):
        current_letter = current_row[x]
        if current_letter == 'S':
            start = (x,y)
        if current_letter == 'E':
            end = (x,y)

shortestPath = shortest_path(input_list, start[0], start[1])

print(f"The answer is {shortestPath}")
