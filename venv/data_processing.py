"""
Year: 2022
Version: 1
Author: 690024916
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


files = ['t2_p25_m1.csv', 't2_p50_m1.csv', 't2_p50_m2.csv', 't2_p50_m3.csv', 't2_p50_m4.csv', 't2_p50_m5.csv',
         't2_p75_m1.csv', 't2_p100_m1.csv', 't2_p125_m1.csv', 't3_p50_m1.csv', 't4_p50_m1.csv', 't4_p50_m4.csv',
         't4_p100_m4.csv', 't4_p100_m10.csv', 't5_p50_m1.csv', 't10_p100_m4.csv']

new_names = ['t=2 p=25 m=1', 't=2, p=50, m=1', 't=2, p=50, m=2', 't=2, p=50, m=3', 't=2, p=50, m=4', 't=2, p=50, m=5',
             't=2, p=75, m=1', 't=2, p=100, m=1', 't=2, p=125, m=1', 't=3, p=50, m=1', 't=4, p=50, m=1',
             't=4, p=50, m=4', 't=4, p=100, m=4', 't=4, p=100, m=10', 't=5, p=50, m=1', 't=10, p=100, m=4']


total_value = []
dataframes = []
for file in files:
    # generate all DataFrames
    df = pd.read_csv('Data/'+file).rename(columns={'num bags': 'num_bags', 'duplicate bags': 'duplicate_bags',
                                           'total weight': 'total_weight', 'total value': 'total_value',
                                           'fitness': 'fitness'})
    df['id'] = files.index(file) + 1
    df['name'] = new_names[files.index(file)]
    dataframes.append(df)

df = pd.concat(dataframes)
df = df.drop('Unnamed: 0', axis='columns')


"""
Scatter graph to show distribtion of scores accross the parameter tests
"""
plt.figure(figsize=(8,4), dpi=150)
cmap = sns.color_palette("hls", n_colors=16)
groups = df.groupby('name')
count = 0
for name, group in groups:
    plt.plot(group.total_weight, group.total_value, marker='o', linestyle='',
             color=cmap[count], markersize=8, label=name)
    count += 1

font = {'family': 'serif', 'size': 10}
font2 = {'family': 'serif', 'size': 10}
plt.xlabel("Total Weight (kg)", fontdict=font)
plt.ylabel("Total Value (£)", fontdict=font)
plt.title("GA with varying p, t, and m values", fontdict=font2)
plt.legend(bbox_to_anchor=(1.1, 1.00))
plt.show()


"""
Boxplots to show distribtion of Total Value accross parameter testing
"""
fig, ax = plt.subplots()
data = []
for name, group in groups:
    data.append(group.total_value)

ax.boxplot(data)
ax.set_xticks(range(1, 17))
ax.set_xticklabels(new_names, rotation=90)
ax.set_ylabel('Total Value (£)')
ax.set_xlabel('Solutions')
ax.set_title('Distribtion of Total Value accross parameter testing')


"""
Boxplots to show distribtion of Total Weight accross parameter testing
"""
fig, ax = plt.subplots()
data = []
for name, group in groups:
    data.append(group.total_weight)

ax.boxplot(data)
ax.set_xticks(range(1, 17))
ax.set_xticklabels(new_names, rotation=90)
ax.set_ylabel('Total Weight (kg)')
ax.set_xlabel('Solutions')
ax.set_title('Distribtion of Total Weight accross parameter testing')
# plt.show()


"""
Graph(s) to show relation between Population, Tournament size, 
and Mutation size with Fitness score using the largest dataset
"""
df = pd.read_csv('Data/even_bigger_data.csv')
df.nlargest(n=10, columns='total_value')
df.nsmallest(n=10, columns='total_value')

colors = np.random.rand(100)
area = (df.fitness) ** 11
plt.scatter(df.p, df.t, s=area, c=colors, alpha=0.5)
plt.title("Effect of Population and Tournament size on fitness")
#plt.show()

colors = np.random.rand(100)
area = (df.fitness) ** 11
plt.scatter(df.p, df.m, s=area, c=colors, alpha=0.5)
plt.title("Effect of Population and Mutation size on fitness")
# plt.show()

colors = np.random.rand(100)
area = (df.fitness) ** 11
plt.scatter(df.t, df.m, s=area, c=colors, alpha=0.5)
plt.title("Effect of Tournament and Mutation size on fitness")
# plt.show()


"""
Graph to show performance difference between GA run with and without mutation
"""
df = pd.read_csv('Data/p=100, t=2, m=0.csv')
df2 = pd.read_csv('Data/p=100, t=2, m=1.csv')
plt.figure(figsize=(8, 6), dpi=150)
df.total_value.plot(label="M=0", color="orange")
df2.total_value.plot(label="M=1", color="green")
plt.title("GA performance with and without mutation")
plt.xlabel("Iterations with different seeds")
plt.ylabel("Total Value")
plt.legend()
# plt.show()


"""
Graph to show performance difference between GA run with and without crossover
"""
df3 = pd.read_csv('Data/no_crossover.csv')
df4 = pd.read_csv('Data/with_crossover.csv')
plt.figure(figsize=(8, 6), dpi=150)
df3.total_value.plot(label="Value no crossover", color="darkred")
df4.total_value.plot(label="Value crossover", color="darkblue")
df3.total_weight.plot(label="Weight no crossover", color="lightcoral")
df4.total_weight.plot(label="Weight crossover", color="lightskyblue")
plt.title("GA performance with and without crossover")
plt.xlabel("Iterations with different seeds")
plt.ylabel("Total Value and weight")
plt.legend()
#plt.show()
