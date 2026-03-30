import csv
import Levenshtein
import random

data = []
# Use 'with open' to ensure the file is closed automatically
with open('data.csv', mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        data.append(row)

data = [[entry[0], entry[0], entry[1], entry[2]] for entry in data]
# input word, in-progress word, output word, meaning

def distance(data):
    return sum(Levenshtein.distance(entry[1], entry[2]) for entry in data)

alphabet = list(set(''.join([entry[0] + entry[2] for entry in data])))

substitutions = []

for _ in range(10000):
    print('.', end='')
    distance_before = distance(data)

    rule_type = random.choice(['modify_first', 'modify_second', 'modify_single', 'delete'])
    substitution_before = ''
    substitution_after = ''
    char_1 = random.choice(alphabet)
    char_2 = random.choice(alphabet)
    char_3 = random.choice(alphabet)
    if rule_type == 'modify_first':
        substitution_before = char_1 + char_2
        substitution_after = char_3 + char_2
    elif rule_type == 'modify_second':
        substitution_before = char_1 + char_2
        substitution_after = char_1 + char_3
    elif rule_type == 'modify_single':
        substitution_before = char_1
        substitution_after = char_2
    else: # deletion
        substitution_before = char_1
        substitution_after = ''

    candidate = [[entry[0], entry[1].replace(substitution_before, substitution_after), entry[2], entry[3]] for entry in data]

    if distance(candidate) < distance_before:
        print('lowered distance to ' + str(distance(candidate)))
        substitutions.append((substitution_before, substitution_after))
        data = candidate

print(substitutions)