#print("hi") # let's refamiliarize ourselves with Pycharm!
#print("everything") #control r
#print("only this") #control shift e!

# Day 1: Calorie Counting
import pandas as pd
data = pd.read_csv(r"datafiles/day_1.csv", header = None, names = ["og"], skip_blank_lines = False)

sums = []
num = 0
for i in data.og:
    if pd.isna(i):
        sums.append(num)
        num = 0
    else:
        num += int(i)


