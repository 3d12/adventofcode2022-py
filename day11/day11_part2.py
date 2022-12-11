from ..file_reader import read_file_into_list

def parse(line):
    line_stripped = line.replace('\n','')
    return line_stripped

class Monkey:
    def __init__(self, data):
        self.held_items = [int(e) for e in data[1].split(': ')[-1].split(', ')]
        self.operation_str = data[2].split(' = ')[-1]
        term1 = 0 if self.operation_str.split()[0] == 'old' else int(self.operation_str.split()[0])
        term2 = 0 if self.operation_str.split()[-1] == 'old' else int(self.operation_str.split()[-1])
        self.operation = (lambda e: (e if term1 == 0 else term1) + (e if term2 == 0 else term2)) \
                if self.operation_str.split()[1] == '+' else \
                (lambda e: (e if term1 == 0 else term1) * (e if term2 == 0 else term2))
        self.throw_test_num = int(data[3].split()[-1])
        self.throw_test = (lambda e: e % self.throw_test_num == 0)
        self.true_dest = int(data[4].split()[-1])
        self.false_dest = int(data[5].split()[-1])
        self.inspection_count = 0
        #print(f"DEBUG: {data[0]} {self.held_items} {self.operation_str} (test({self.throw_test_num}) ? {self.true_dest} : {self.false_dest})={self.throw_test(38)}")

    def monkeyTurn(self, largestFactor):
        thrown_items = []
        for _ in range(len(self.held_items)):
            item = self.held_items.pop(0)
            item = self.operation(item)
            item = item % largestFactor
            thrown_items.append({ 'value': item, 'dest': self.true_dest if self.throw_test(item) else self.false_dest })
            self.inspection_count += 1
        return thrown_items

    def receiveItem(self, item):
        self.held_items.append(int(item))


input_list = read_file_into_list('day11/input.txt', parse)


monkeys = []

for i in range(0,len(input_list),7): # pyright: ignore
    newMonkey = Monkey(input_list[i:i+7]) # pyright: ignore
    monkeys.append(newMonkey)

# setting upper limit on the resulting product, shared across all monkeys
largestFactor = 1
for i in range(len(monkeys)):
    largestFactor *= monkeys[i].throw_test_num

for i in range(10000):
    print(f"Beginning of round {i+1}")
    for monkey in monkeys:
        thrown_items = monkey.monkeyTurn(largestFactor)
        for item in thrown_items:
            monkeys[item['dest']].receiveItem(item['value'])

monkeyTouches = [e.inspection_count for e in monkeys]
monkeyTouches.sort()
twoMostActiveMonkeys = monkeyTouches[-2:]
answer = twoMostActiveMonkeys[0] * twoMostActiveMonkeys[1]
print(f"The answer is {answer}")
