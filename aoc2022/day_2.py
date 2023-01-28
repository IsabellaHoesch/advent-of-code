# Day 2: Rock Paper Scissors
## 1/2
import pandas as pd
#read the data
df = pd.read_csv(r"datafiles/day_2.csv", header = None, names = ["og"], skip_blank_lines = False)
#prep the data
df['elv'] = df['og'].str[0]
df['me'] = df['og'].str[-1]

# translate to abc
df['me_abc'] = df['me'].map({'X': 'A', 'Y': 'B', 'Z': 'C'})
df['value_me'] = df['me'].map({'X': 1, 'Y': 2, 'Z': 3})

# calculate score using rock-paper-scissors logic
def score_calc(df, elv_choice, my_choice):
    # get scores for each game
    df['value_result'] = 0
    for i, row in df.iterrows():
        if row[elv_choice] == row[my_choice]:
            df.at[i, 'value_result'] = 3
        elif row[elv_choice] == "A":
            if row[my_choice] == "C":
                df.at[i, 'value_result'] = 0
            elif row[my_choice] == "B":
                df.at[i, 'value_result'] = 6
        elif row[elv_choice] == "B":
            if row[my_choice] == "A":
                df.at[i, 'value_result'] = 0
            elif row[my_choice] == "C":
                df.at[i, 'value_result'] = 6
        elif row[elv_choice] == "C":
            if row[my_choice] == "B":
                df.at[i, 'value_result'] = 0
            elif row[my_choice] == "A":
                df.at[i, 'value_result'] = 6
    # calculate the score of each game plus which ABC used
    df['total_score'] = df['value_me'] + df['value_result']
    print("The total score", sum(df['total_score']))

result = score_calc(df, "elv", "me_abc")




## 2/2
df['result'] = df['og'].str[-1]
df['result_ldw'] = df['result'].map({'X': 'L', 'Y': 'D', 'Z': 'W'})

# get my_choice for each game
df['my_choice'] = 0
# logic
for i, row in df.iterrows():
    if row['elv'] == "A": # if rock
        if row['result_ldw'] == "L": # lose
            df.at[i, 'my_choice'] = "C" # -> lose with scissors
        elif row['result_ldw'] == "D": # draw
            df.at[i, 'my_choice'] = row['elv'] # -> draw with same
        elif row['result_ldw'] == "W": # win
            df.at[i, 'my_choice'] = "B" # -> win with paper
    elif row['elv'] == "B": # if paper
        if row['result_ldw'] == "L": # lose
            df.at[i, 'my_choice'] = "A" # -> lose with rock
        elif row['result_ldw'] == "D": # draw
            df.at[i, 'my_choice'] = row['elv'] # -> draw with same
        elif row['result_ldw'] == "W": # win
            df.at[i, 'my_choice'] = "C" # -> win with scissors
    elif row['elv'] == "C": # if scissors
        if row['result_ldw'] == "L": # lose
            df.at[i, 'my_choice'] = "B" # -> lose with paper
        elif row['result_ldw'] == "D": # draw
            df.at[i, 'my_choice'] = row['elv'] # -> draw with same
        elif row['result_ldw'] == "W": # win
            df.at[i, 'my_choice'] = "A" # -> win with rock

df['value_me'] = df['my_choice'].map({'A': 1, 'B': 2, 'C': 3})
result2 = score_calc(df, "elv", "my_choice")