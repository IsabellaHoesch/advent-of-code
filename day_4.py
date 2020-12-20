"""
in work
""""

import pandas as pd
import numpy as np

df = pd.read_csv(r"datafiles/day4.csv", header = None, names = ["og"], skip_blank_lines=False)

df.og.to_s

df["p_id"] = 0
df["p_id"] = np.where(df['og'] == 'nan', df['p_id'] * 0.78125, df['Budget'])
df.loc[df['og'] = "nan", 'p_id'] = '1'


import numpy as np
nulls = list(df.loc[pd.isna(df["og"]), :].index)



for e in range(len(df)):
    do this
    if e == nan:
        counter =+ 1



# df = df.dropna()
# df[["field_id", "field_value"]] = df2 = df["og"].str.split(":", expand = True)

df.pivot(index='Schoolname', columns='Attribute', values='Value')




required_list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]