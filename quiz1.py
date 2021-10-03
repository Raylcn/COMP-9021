# COMP9021 21T3
# Quiz 1 *** Due Friday Week 3 @ 9.00pm
#        *** Late penalty 10% per day
#        *** Not accepted after Monday Week 4 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())#order numbers ascendingly
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE

#cycles
#avoiding repeating
visited = []
for key in keys:
    if key in visited:
        continue
    cycle = [key]
#finding cycles
    while True:
        key = mapping[key]
        if key == cycle[0]:
            visited.extend(cycle)
            cycles.append(cycle)
            break
        elif key in cycle:
            break
        elif key not in mapping:
            break
        else:
            cycle.append(key)


#reversed dictionary
library = {}
for key,value in mapping.items():
    if value in library:
        library[value].append(key)
    else:
        library[value] = [key]

#length
for key,values in library.items():
    if len(values) not in reversed_dict_per_length:
        reversed_dict_per_length[len(values)] = {}
    reversed_dict_per_length[len(values)][key] = values


print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)
