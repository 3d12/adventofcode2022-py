from ..file_reader import read_file_into_list
from enum import Enum

class Room:
    def __init__(self, name, flowRate, leadsTo):
        self.name = name
        self.flowRate = flowRate
        self.leadsTo = leadsTo
        self.opened = False

    def __str__(self):
        return 'Room ' + self.name + ' (flowRate: ' + str(self.flowRate) + ', leadsTo: ' + str(self.leadsTo) + ', opened: ' + str(self.opened) + ')'

    def __repr__(self):
        return self.__str__()

class Action:
    def __init__(self, actionType, target=None):
        self.actionType = actionType
        self.target = target

class ActionType(Enum):
    OPEN = 0
    MOVE = 1

def process_list(valves, action_list):
    pressure = 0
    max_turns = 30
    position = 'AA'
    for turn in range(max_turns):
        new_pressures = [e.flowRate for e in valves if e.opened]
        pressure += sum(new_pressures)

        action = action_list[turn]
        # logic based on action type goes here
        if action.actionType == ActionType.MOVE:
            position = action.target
        elif action.actionType == ActionType.OPEN:
            current_valve = next(e for e in valves if e.name == position)
            current_valve.opened = True
    return pressure


def parse(line):
    line = line.replace('\n','')
    line_split = line.split()
    name = line_split[1]
    flowRate = int(line_split[4].split('=')[-1][:-1])
    leadsTo = line_split[9:]
    return Room(name, flowRate, leadsTo)

input_list = read_file_into_list('day16/test_input.txt', parse)

print(input_list)

# example optimum action list from problem description
optimum_test_action_list = []
optimum_test_action_list.append(Action(ActionType.MOVE, 'DD'))
optimum_test_action_list.append(Action(ActionType.OPEN))
optimum_test_action_list.append(Action(ActionType.MOVE, 'CC'))
optimum_test_action_list.append(Action(ActionType.MOVE, 'BB'))
optimum_test_action_list.append(Action(ActionType.OPEN))
optimum_test_action_list.append(Action(ActionType.MOVE, 'AA'))
optimum_test_action_list.append(Action(ActionType.MOVE, 'II'))
optimum_test_action_list.append(Action(ActionType.MOVE, 'JJ'))
optimum_test_action_list.append(Action(ActionType.OPEN))
optimum_test_action_list.append(Action(ActionType.MOVE, 'II'))
optimum_test_action_list.append(Action(ActionType.MOVE, 'AA'))
optimum_test_action_list.append(Action(ActionType.MOVE, 'DD'))
optimum_test_action_list.append(Action(ActionType.MOVE, 'EE'))
optimum_test_action_list.append(Action(ActionType.MOVE, 'FF'))
optimum_test_action_list.append(Action(ActionType.MOVE, 'GG'))
optimum_test_action_list.append(Action(ActionType.MOVE, 'HH'))
optimum_test_action_list.append(Action(ActionType.OPEN))
optimum_test_action_list.append(Action(ActionType.MOVE, 'GG'))
optimum_test_action_list.append(Action(ActionType.MOVE, 'FF'))
optimum_test_action_list.append(Action(ActionType.MOVE, 'EE'))
optimum_test_action_list.append(Action(ActionType.OPEN))
optimum_test_action_list.append(Action(ActionType.MOVE, 'DD'))
optimum_test_action_list.append(Action(ActionType.MOVE, 'CC'))
optimum_test_action_list.append(Action(ActionType.OPEN))
optimum_test_action_list.append(Action(ActionType.OPEN))
optimum_test_action_list.append(Action(ActionType.OPEN))
optimum_test_action_list.append(Action(ActionType.OPEN))
optimum_test_action_list.append(Action(ActionType.OPEN))
optimum_test_action_list.append(Action(ActionType.OPEN))
optimum_test_action_list.append(Action(ActionType.OPEN))

print(process_list(input_list, optimum_test_action_list))
