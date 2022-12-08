from ..file_reader import read_file_into_list

def parse(line):
    line_stripped = line.replace('\n','')
    return line_stripped

input_list = read_file_into_list('day8/input.txt', parse)

def viewingDistanceTop(forest, x, y):
    tree = int(forest[y][x])
    tmp_viewDist = 0
    for i in range(y-1, -1, -1):
        if int(forest[i][x]) >= tree:
            tmp_viewDist += 1
            return tmp_viewDist
        else:
            tmp_viewDist += 1
    return tmp_viewDist

def viewingDistanceBottom(forest, x, y):
    tree = int(forest[y][x])
    tmp_viewDist = 0
    for i in range(y+1, len(forest)):
        if int(forest[i][x]) >= tree:
            tmp_viewDist += 1
            return tmp_viewDist
        else:
            tmp_viewDist += 1
    return tmp_viewDist

def viewingDistanceLeft(forest, x, y):
    tree = int(forest[y][x])
    tmp_viewDist = 0
    for i in range(x-1, -1, -1):
        if int(forest[y][i]) >= tree:
            tmp_viewDist += 1
            return tmp_viewDist
        else:
            tmp_viewDist += 1
    return tmp_viewDist

def viewingDistanceRight(forest, x, y):
    tree = int(forest[y][x])
    tmp_viewDist = 0
    for i in range(x+1, len(forest[y])):
        if int(forest[y][i]) >= tree:
            tmp_viewDist += 1
            return tmp_viewDist
        else:
            tmp_viewDist += 1
    return tmp_viewDist

def totalViewingDistance(forest, x, y):
    return viewingDistanceTop(forest, x, y) \
            * viewingDistanceLeft(forest, x, y) \
            * viewingDistanceBottom(forest, x, y) \
            * viewingDistanceRight(forest, x, y)


best_scenic_score = 0
best_scenic_spot = (0,0)
for y in range(len(input_list)): # pyright: ignore
    for x in range(len(input_list[y])): # pyright: ignore
        scenic_score = totalViewingDistance(input_list, x, y)
        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score
            best_scenic_spot = (x,y)

print(f"The answer is {best_scenic_score} at {best_scenic_spot}")
