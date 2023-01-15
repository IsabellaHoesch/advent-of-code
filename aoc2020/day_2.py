# Day 2: Password Philosophy

import pandas as pd
data = pd.read_csv(r"datafiles/day2.csv", header = None, names = ["og"])
data[["rule", "pw"]] = data["og"].str.split(":", expand = True)
data[["rule_amount", "rule_letter"]] = data["rule"].str.split(" ", expand = True)
data[["rule_#min", "rule_#max"]] = data["rule_amount"].str.split("-", expand = True)
data.drop(["rule", "og", "rule_amount"], axis=1, inplace=True)
data[["rule_#min", "rule_#max"]] = data[["rule_#min", "rule_#max"]].apply(pd.to_numeric, errors='coerce')


# Part 1
"""
Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
"""

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
Exactly one of these positions must contain the given letter:
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. 
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. 
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
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




