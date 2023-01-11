with open('i2.txt') as f:
    data = f.read().split('\n')
    
outcome = {'A X': 4,
           'A Y': 8,
           'A Z': 3,
           'B X': 1,
           'B Y': 5,
           'B Z': 9,
           'C X': 7,
           'C Y': 2,
           'C Z': 6,}

results = {'A X': 3,
           'A Y': 4,
           'A Z': 8,
           'B X': 1,
           'B Y': 5,
           'B Z': 9,
           'C X': 2,
           'C Y': 6,
           'C Z': 7,}
    
score = 0
answer = 0
for d in data:
    score += outcome[d]
    answer += results[d]
    
print(f'the answer to part 1 is {score}')
print(f'the answer to part 2 is {answer}')
    
