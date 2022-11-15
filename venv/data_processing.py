import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

files = ["t2_p25_m1.csv", "t2_p50_m1.csv", "t2_p50_m2.csv",
         "t2_p50_m3.csv", "t2_p50_m4.csv", "t2_p50_m5.csv",
         "t2_p75_m1.csv", "t2_p100_m1.csv", "t2_p125_m1.csv",
         "t3_p50_m1.csv", "t4_p50_m1.csv", "t4_p50_m4.csv",
         "t4_p100_m4.csv", "t4_p100_m10.csv", "t5_p50_m1.csv",
         "t10_p100_m4.csv"]


for file in files:
    df = pd.read_csv(file).rename(columns={'num bags': 'num_bags',
                                           'duplicate bags': 'duplicate_bags',
                                           'total weight': 'total_weight',
                                           'total value': 'total_value',
                                           'fitness': 'fitness'})

    print(file)
    print("Weight Range: ", df.total_weight.min(), ",",df.total_weight.max())
    print("Value Range: ", df.total_value.min(), ",",df.total_value.max())
    print("\n")
