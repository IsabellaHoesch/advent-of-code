# Day 2: Part 1
import pandas as pd
data = pd.read_csv(r"datafiles/day2.csv", header = None, names = ["og"])
data[["rule", "pw"]] = data["og"].str.split(":", expand = True)
data[["rule_amount", "rule_letter"]] = data["rule"].str.split(" ", expand = True)
data[["rule_#min", "rule_#max"]] = data["rule_amount"].str.split("-", expand = True)
data.drop(["rule", "og", "rule_amount"], axis=1, inplace=True)
data[["rule_#min", "rule_#max"]] = data[["rule_#min", "rule_#max"]].apply(pd.to_numeric, errors='coerce')


# Part 1
counter = []
for e in range(len(data["pw"])):
    t=data.pw[e]
    counter.append(t.count(data["rule_letter"][e]))
data["letter_count"] = counter

data['pwcorrect_part1'] = (data['letter_count'] >= data['rule_#min']) & (data['letter_count'] <= data['rule_#max'])
data_correctpw = data[data["pwcorrect_part1"] == True]
print("Number of correct passwords part1", len(data_correctpw))


# Part 2:
"""
Exactly one of these positions must contain the given letter.
"""
position = []
for e in range(len(data["pw"])):
    passw = data["pw"][e]
    letter = data["rule_letter"][e]
    position.append([pos for pos, char in enumerate(passw) if char == letter])
data["position_list"] = position



in_list = []
for t in range(len(data["pw"])):
    pos_list = data['position_list'][t]
    min_num = data['rule_#min'][t]
    max_num = data['rule_#max'][t]
    counter = 0
    if min_num in pos_list:
        counter += 1
    if max_num in pos_list:
        counter += 1

    if counter == 1:
        in_list.append("True")
    else:
        in_list.append("False")

data["pwcorrect_part2"] = in_list
data_correctpw2 = data[data["pwcorrect_part2"] == "True"]
print("Number of correct passwords part2", len(data_correctpw2))




