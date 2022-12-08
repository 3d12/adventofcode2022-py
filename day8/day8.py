from ..file_reader import read_file_into_list

def parse(line):
    line_stripped = line.replace('\n','')
    return line_stripped

input_list = read_file_into_list('day8/input.txt', parse)

def visibleFromTop(forest, x, y):
    tree = int(forest[y][x])
    for i in range(y-1, -1, -1):
        if int(forest[i][x]) >= tree:
            return False
    return True

def visibleFromBottom(forest, x, y):
    tree = int(forest[y][x])
    for i in range(y+1, len(forest)):
        if int(forest[i][x]) >= tree:
            return False
    return True

def visibleFromLeft(forest, x, y):
    tree = int(forest[y][x])
    for i in range(x-1, -1, -1):
        if int(forest[y][i]) >= tree:
            return False
    return True

def visibleFromRight(forest, x, y):
    tree = int(forest[y][x])
    for i in range(x+1, len(forest[y])):
        if int(forest[y][i]) >= tree:
            return False
    return True

def isTreeVisible(forest, x, y):
    if visibleFromTop(forest,x,y) or \
        visibleFromLeft(forest,x,y) or \
        visibleFromBottom(forest,x,y) or \
        visibleFromRight(forest,x,y):
            return True
    else:
        return False


total_trees_visible = 0
for y in range(len(input_list)): # pyright: ignore
    for x in range(len(input_list[y])): # pyright: ignore
        if isTreeVisible(input_list, x, y):
            total_trees_visible += 1

print(f"The answer is {total_trees_visible}")
