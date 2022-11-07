import pandas as pd
import re
import random

def main():
    txt = pd.read_fwf('BankProblem.txt')
    capacity = float(txt.columns[1])
    list = txt.values.tolist()
    data = []
    for li in list:
        if "bag" in li[0]:
            index = list.index(li)
            row = [str(len(data)),
                   float(re.findall(r'\d+\.\d+', list[index+1][0])[0]),
                   float(re.findall(r'\d+', list[index+2][0])[0])]
            data.append(row)

    solutions = initialize(data, capacity)


    d = []
    for solution in solutions:
        print(solution)
        row=[]
        total = 0
        value = 0
        for b in solution:
            total += b[1]
            value += b[2]

        row.append(total)
        row.append(value)
        row.append(calculateFitness(solution, capacity))
        d.append(row)



    df = pd.DataFrame(data=d, columns=["weight", "value", "fitness"])
    print(df)


def initialize(data, capacity):
    solutions = []
    # initial population size 50 when number of decision variables < 5
    for i in range(0, 50):
        c = capacity
        solution = []
        while c >= 0:
            rand_bag = random.choice(data)
            solution.append(rand_bag)
            c = c - rand_bag[1]

        solutions.append(solution)

    return solutions


def calculateFitness(s, c):
    # solution (s), capacity (c), fitness (f), constant (k)
    f, k = 0, 2
    for b in s: f+=(b[1]/b[2])**k # for bag in solution

    return float(f/c)



if __name__ == '__main__':
    main()