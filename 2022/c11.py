primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

class Monkey:
    
    def __init__(self, data, id):
        self.id = id
        self.items = [int(i) for i in d[1].split(':')[1].split(',')]
        self.primes_of_items = [[prime for prime in primes if item % prime == 0] for item in self.items]
        self.operator = d[2].split('=')[1].split(' ')[2]
        self.parameter = int(d[2].split('=')[1].split(' ')[3]) if d[2].split('=')[1].split(' ')[3] != 'old' else 'old'
        self.check = int(d[3].split(' ')[-1])
        self.if_true = int(d[4].split(' ')[-1])
        self.if_false = int(d[5].split(' ')[-1])
        self.item = ''
        self.primes = ''
        self.status = ''
        self.inspections = 0
        
    def inspect_item(self):
        self.inspections += 1
        item = self.items.pop(0)
        if self.operator == '*' and self.parameter == 'old':
            item *= item
        elif self.operator == '*':
            item *= self.parameter
        elif self.operator == '+':
            item += self.parameter
        self.item = item
        
    def item_relief(self):
        self.item = self.item % supermod
        
    def check_item(self):
        if self.item % self.check == 0:
            self.status = True
        else:
            self.status = False
        
    def pass_item(self, monkeys):
        if self.status:
            monkeys[self.if_true].items.append(self.item)
        else:
            monkeys[self.if_false].items.append(self.item)

with open('i11.txt') as f:
    data = [d.split('\n') for d in f.read().split('\n\n')]
    
monkeys = []
id = 0
for d in data:
    monkey = Monkey(d, id)
    monkeys.append(monkey)
    id += 1
    
supermod = 1
checks = [monkey.check for monkey in monkeys]
for check in checks:
    supermod *= check
    
for round in range(10000):
    for monkey in monkeys:
        while monkey.items:
            monkey.inspect_item()
            monkey.item_relief()
            monkey.check_item()
            monkey.pass_item(monkeys)
 
inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
print(inspections[0] * inspections[1])