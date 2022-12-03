from ..file_reader import read_file_into_list
from enum import Enum

def parse(line):
    line_stripped = line.replace('\n','')
    line_split = line_stripped.split(' ')
    return { 'opponent': line_split[0], 'outcome': line_split[1] }

input_list = read_file_into_list('day2/input.txt', parse)

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
    def losesTo(self):
        if self is RPS.ROCK:
            return RPS.PAPER
        if self is RPS.PAPER:
            return RPS.SCISSORS
        if self is RPS.SCISSORS:
            return RPS.ROCK
        return RPS.ROCK
    def winsAgainst(self):
        if self is RPS.ROCK:
            return RPS.SCISSORS
        if self is RPS.PAPER:
            return RPS.ROCK
        if self is RPS.SCISSORS:
            return RPS.PAPER
        return RPS.ROCK
    def tiesTo(self):
        return self

my_score = 0
round_counter = 0
for rps_round in input_list: # pyright: ignore
    opp = rps_round['opponent']
    opp_mapping = { 'A': RPS.ROCK, 'B': RPS.PAPER, 'C': RPS.SCISSORS }
    opp_mapped = opp_mapping[opp]
    outcome = rps_round['outcome']
    my_mapped = None
    if outcome == 'X':
        my_mapped = opp_mapped.winsAgainst()
    if outcome == 'Y':
        my_mapped = opp_mapped.tiesTo()
    if outcome == 'Z':
        my_mapped = opp_mapped.losesTo()
    if my_mapped > opp_mapped: # pyright: ignore
        my_score += 6
    if my_mapped == opp_mapped:
        my_score += 3
    my_score += int(my_mapped) # pyright: ignore
    print(f"Round {round_counter+1}: opp {opp_mapped}, me {my_mapped} -- my score: {my_score}")
    round_counter += 1

print(f"The answer is: {my_score}")
