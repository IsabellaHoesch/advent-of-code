# Day 3: Toboggan Trajectory
"""
Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

in work - b isnt correct
"""

import pandas as pd
import numpy as np

data = pd.read_csv(r"datafiles/day3.csv", header = None, names = ["og"])
data = data['og'].apply(lambda x: pd.Series(list(x)))
num_dfs = data.shape[0] / data.shape[1]
num_dfs = 7 #todo fix this so the apropriate amount is added (4 for part 1, 7 for part 2)




# Part 1:
"""
Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
"""

for d in range(int(num_dfs)):
    data_new = data.copy()
    data = pd.concat([data, data_new], axis=1)
data.columns = list(range(data.shape[1]))

counter = 0
col=0
for row in range(1,len(data)):
    col += 3
    if data.loc[row, col] == "#":
        counter += 1
print("You´d encounter", counter, "trees on the slope")

# Part 2:
"""
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.
What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""

## Right 1, down 1.
## Right 3, down 1. (This is the slope you already checked.)
## Right 5, down 1.
## Right 7, down 1.

skip_col = [1, 3, 5, 7]
counter_list = []
for skip in skip_col:
    counter = 0
    col = 0
    for row in range(1, len(data)):
        col += skip
        if data.loc[row, col] == "#":
            counter += 1
    counter_list.append(counter)


# Right 1, down 2. #todo this one might be wrong
counter_2 = 0
col=0
for row in range(1, len(data), 2):
    print(row)
    col += 1
    if data.loc[row, col] == "#":
        counter_2 += 1
counter_list.append(counter_2)


# multiplied counters
# result = np.prod(counter_list)
#result = 67*211*77*89*34 # too high

# 3293949274 = 67*211*77*89*34 --> too low

from operator import mul
result_1 = reduce(mul, counter_list, 1)

from numpy import prod
prod(counter_list)