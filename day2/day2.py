from ..file_reader import read_file_into_list
from enum import Enum

def parse(line):
    line_stripped = line.replace('\n','')
    line_split = line_stripped.split(' ')
    return { 'opponent': line_split[0], 'mine': line_split[1] }

input_list = read_file_into_list('day2/input.txt', parse)

my_score = 0

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    def __gt__(self, other):
        if not (self in RPS and other in RPS):
            return False
        if self is RPS.ROCK and other is RPS.SCISSORS \
            or self is RPS.PAPER and other is RPS.ROCK \
            or self is RPS.SCISSORS and other is RPS.PAPER:
                return True
        return False
    def __eq__(self, other):
        if not (self in RPS and other in RPS):
            return False
        if self is RPS.ROCK and other is RPS.ROCK \
            or self is RPS.PAPER and other is RPS.PAPER \
            or self is RPS.SCISSORS and other is RPS.SCISSORS:
                return True
        return False
    def __ge__(self, other):
        if not (self in RPS and other in RPS):
            return False
        if self.__gt__(other) or self.__eq__(other):
            return True
        return False
    def __int__(self):
        if self is RPS.ROCK:
            return 1
        if self is RPS.PAPER:
            return 2
        if self is RPS.SCISSORS:
            return 3
        return 0

round_counter = 0
for rps_round in input_list: # pyright: ignore
    opp = rps_round['opponent']
    opp_mapping = { 'A': RPS.ROCK, 'B': RPS.PAPER, 'C': RPS.SCISSORS }
    opp_mapped = opp_mapping[opp]
    my = rps_round['mine']
    my_mapping = { 'X': RPS.ROCK, 'Y': RPS.PAPER, 'Z': RPS.SCISSORS }
    my_mapped = my_mapping[my]
    if my_mapped > opp_mapped:
        my_score += 6
    if my_mapped == opp_mapped:
        my_score += 3
    my_score += int(my_mapped)
    print(f"Round {round_counter+1}: opp {opp_mapped}, me {my_mapped} -- my score: {my_score}")
    round_counter += 1

print(f"The answer is: {my_score}")
