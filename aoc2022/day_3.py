# Day 2: Rucksack Reorganization
## 1/2
import pandas as pd
import string
#read the data
df = pd.read_csv(r"datafiles/day_3.csv", header = None, names = ["og"], skip_blank_lines = False)

#split og column and create columns with half of value
df['first_half'] = df['og'].apply(lambda x: x[:len(x)//2])
df['second_half'] = df['og'].apply(lambda x: x[len(x)//2:])

#find the same letter
# define a custom function to compare the strings of col1 and col2
def find_common_string(row):
    return ''.join(sorted(set(row['first_half']).intersection(row['second_half'])))
# apply the custom function to each row of the dataframe
df['result'] = df.apply(find_common_string, axis=1)

# find value of that same_letter
## create list a to z and 1 to 26
letters_l = list(string.ascii_lowercase)
numbers_l = list(range(1,27))
letters_u = [l.upper() for l in letters_l]
numbers_u = list(range(27, 53))

letters = letters_l + letters_u
numbers = numbers_l + numbers_u

## turn into dictionary
d = dict(zip(letters, numbers))

#retrieve right value for the number in
df['val'] = df['result'].map(d)

# sum all values of dictionary
df['val'].sum()


## 2/2
#find the same letter in each 3 rows
# define a custom function to compare the strings of col1 and col2
def find_common_string_3(row):
    return ''.join(sorted(set(row['first_half']).intersection(row['second_half'])))
# apply the custom function to each row of the dataframe
df['result'] = df.apply(find_common_string_3, axis=1)

# converting the first three rows to a set of characters

num_sets = df.shape[0] // 3
common_letters = []

for i in range(num_sets):
    char_set = set("".join(df.iloc[i*3:i*3+3, 0].tolist()))
    common_letter = [char for char in char_set if all(char in string for string in df.iloc[i*3:i*3+3, 0].tolist())]
    common_letters.extend(common_letter)

df_2 = pd.DataFrame({"day_1": common_letters})
df_2['val_2'] = df_2['day_1'].map(d)
