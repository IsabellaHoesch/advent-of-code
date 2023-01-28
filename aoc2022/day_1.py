#print("hi") # let's refamiliarize ourselves with Pycharm!
#print("everything") #control r
#print("only this") #control shift e!

# Day 1: Calorie Counting
## 1/2
import pandas as pd

#read the data
data = pd.read_csv(r"datafiles/day_1.csv", header = None, names = ["og"], skip_blank_lines = False)

sums = []
num = 0

#loop thorugh the column and sum all rows between empty cells
#store values in sums
for i in data.og:
    if pd.isna(i):
        sums.append(num)
        num = 0
    else:
        num += int(i)

#get the max value of sums
print("The elf carrying the most Calories is carrying", max(sums), "calories.")

## 2/2
# order by value
top3_sums = sorted(sums, reverse=True)[0:3]
print("The calories combined of the three top elf is: ", sum(top3_sums))
