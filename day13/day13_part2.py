from ..file_reader import read_file_into_list
from functools import cmp_to_key

def parseStringToList(line):
    line = line.replace('\n','')
    if len(line) == 0:
        return line
    #print(f"DEBUG: Entering parseStringToList, line={line}")
    loopLists = [[]]
    loopDepth = 0
    for i in range(1, len(line)-1):
        char = line[i]
        #print(f"DEBUG: Evaluating char={char}")
        if char == '[':
            #print(f"DEBUG: Detected '[', appending a new blank list and incrementing loopDepth to {loopDepth+1}")
            loopDepth += 1
            if loopDepth > len(loopLists)-1:
                loopLists.append([])
            else:
                loopLists[loopDepth] = []
        elif char == ']':
            #print(f"DEBUG: Detected ']', appending the current list ({loopLists[loopDepth]}) to the previous list ({loopLists[loopDepth-1]})")
            loopLists[loopDepth-1].append(loopLists[loopDepth])
            loopDepth -= 1
        elif char != ',':
            while (i < len(line)-1) and line[i+1] not in ['[',']',',']:
                nextChar = line[i+1]
                char += nextChar
                i += 1
            #print(f"DEBUG: Adding character {char} to list {loopLists[loopDepth]}")
            loopLists[loopDepth].append(int(char))
    return loopLists[loopDepth]

def comparePair(left, right):
    right_len = len(right)
    #print(f"DEBUG: iterating {len(left)} times")
    for i in range(len(left)):
        if i == right_len:
            #print(f"DEBUG: right list ran out of items, not in order")
            return 1
        leftVal = left[i]
        rightVal = right[i]
        if type(leftVal) == int and type(rightVal) == int:
            #print(f"DEBUG: comparing ints {leftVal} vs {rightVal}")
            if leftVal < rightVal:
                return -1
            if rightVal < leftVal:
                return 1
        elif type(leftVal) == list and type(rightVal) == list:
            #print(f"DEBUG: comparing lists {leftVal} vs {rightVal}")
            listCompare = comparePair(leftVal,rightVal)
            if listCompare != 0:
                return listCompare
        else:
            if type(leftVal) == int:
                #print(f"DEBUG: converting {leftVal} to list {[leftVal]}")
                leftVal = [leftVal]
            elif type(rightVal) == int:
                #print(f"DEBUG: converting {rightVal} to list {[rightVal]}")
                rightVal = [rightVal]
            listCompare = comparePair(leftVal,rightVal)
            if listCompare != 0:
                return listCompare
    #print(f"DEBUG: left list ran out of items, does right list still have items? {len(left) < right_len}")
    if len(left) < right_len:
        return -1
    #print(f"DEBUG: Inconclusive")
    return 0


input_list = read_file_into_list('day13/input.txt', parseStringToList)

packets = [e for e in input_list if type(e) == list] # pyright: ignore
packets.append([[2]])
packets.append([[6]])
packets_sorted = sorted(packets, key=cmp_to_key(comparePair)) # pyright: ignore
indexOfDivider1 = 0
indexOfDivider2 = 0
for i, packet in enumerate(packets_sorted):
    if packet == [[2]]:
        indexOfDivider1 = i+1
    if packet == [[6]]:
        indexOfDivider2 = i+1
    print(packet)

print(f"The answer is {indexOfDivider1 * indexOfDivider2}")
