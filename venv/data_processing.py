import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


files = ["t2_p25_m1.csv", "t2_p50_m1.csv", "t2_p50_m2.csv",
         "t2_p50_m3.csv", "t2_p50_m4.csv", "t2_p50_m5.csv",
         "t2_p75_m1.csv", "t2_p100_m1.csv", "t2_p125_m1.csv",
         "t3_p50_m1.csv", "t4_p50_m1.csv", "t4_p50_m4.csv",
         "t4_p100_m4.csv", "t4_p100_m10.csv", "t5_p50_m1.csv",
         "t10_p100_m4.csv"]


trial = []
total_value = []
dataframes = []

for file in files:
    df = pd.read_csv(file).rename(columns={'num bags': 'num_bags',
                                           'duplicate bags': 'duplicate_bags',
                                           'total weight': 'total_weight',
                                           'total value': 'total_value',
                                           'fitness': 'fitness'})

    df['id'] = files.index(file)+1
    df['name'] = file
    dataframes.append(df)



df = pd.concat(dataframes)
df = df.drop('Unnamed: 0', axis='columns')
# df.to_csv(combined_isolated.csv)
groups = df.groupby('name')
for name, group in groups:
    plt.plot(group.total_weight, group.total_value, marker='o', linestyle='', markersize=7, label=name)
plt.legend(bbox_to_anchor=(1.1, 1.05))
plt.show()





