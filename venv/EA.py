import pandas as pd
import re
import random
from itertools import chain

def main(seed, t, p, m):
    random.seed(seed)
    txt = pd.read_fwf('BankProblem.txt')
    capacity = float(txt.columns[1])
    list = txt.values.tolist()
    data = []
    for li in list:
        if "bag" in li[0]:
            index = list.index(li)
            row = [str(len(data)),
                   re.findall(r'\d+\.\d+', list[index+1][0])[0],
                   re.findall(r'\d+', list[index+2][0])[0]]
            data.append(row)

    total_value = 0

    for bag in data:
        total_value += float(bag[2])

    data = encode_data(data)
    solutions = initialize(p, data, capacity)

    fitness_scores = []
    count = 0
    for solution in solutions:
        # store index in list incase two fitness values are the same
        fitness_scores.append([count, calculateFitness(solution, capacity, total_value)])
        count += 1

    evaluations = 0
    while evaluations < 10000:

        parent_a = binary_tournament_selection(solutions, t, fitness_scores)
        parent_b = binary_tournament_selection(solutions, t, fitness_scores)

        child_c, child_d = single_point_crossover(parent_a, parent_b)
        mutated_e, mutated_f = mutation(m, child_c), mutation(m, child_d)
        fitness_e, fitness_f = calculateFitness(mutated_e, capacity, total_value), calculateFitness(mutated_f, capacity, total_value)

        weakest_rep1 = weakest_replacement(mutated_e, fitness_e, fitness_scores, solutions)
        solutions, fitness_scores = weakest_rep1[0], weakest_rep1[1]
        weakest_rep2 = weakest_replacement(mutated_f, fitness_f, fitness_scores, solutions)
        solutions, fitness_scores = weakest_rep2[0], weakest_rep2[1]

        # + 2 becuase 2 fitness evaluations were made
        evaluations += 2


    ss = []
    for fitness in fitness_scores:
        ss.append(fitness[1])

    best = max(ss)
    i = ss.index(best)
    l = solutions[i].split("  ")
    tv = 0
    tw = 0
    for bag in l:
        tv += float(bag.split(" ")[2])
        tw += float(bag.split(" ")[1])

    bags = []
    for sol in solutions[i].split("  "):
        bags.append(sol.split(" ")[0])

    return [p, t, m, seed, len(l), is_duplicates(l), tw, tv, best]


def initialize(p, data, capacity):
    c = 1
    solutions = []
    while c <= p:
        solution = []
        num_bags = random.randint(0, len(data))
        count = 0
        while count < num_bags:
            rand_bag = random.choice(data)
            solution.append(rand_bag)
            if is_duplicates(solution) == True:
                solution.pop()
            else:
                count += 1

        solutions.append("  ".join(solution))
        c += 1

    return solutions


def binary_tournament_selection(solutions, t_size, f_scores):
    fitness_pool = []

    for i in range(t_size):
        fitness = random.choice(f_scores)
        fitness_pool.append(fitness)

    index = 0
    temp = 0
    for f in fitness_pool:
        if f[1] > temp:
            temp = f[1]
            index = f[0]
        elif f[1] == temp:
            index = random.choice([index,f[0]])
            temp = f_scores[index][1]

    return solutions[index]


def encode_data(data):
    # value encoding technique with following strucure:
    # "bag_number bag_weight bag_value"
    encoded = []
    for bag in data: encoded.append(bag[0]+" "+bag[1]+" "+bag[2])

    return encoded


def calculateFitness(s, c, v):
    # solution (s), capacity (c), total value (v)
    sum_weight = 0
    sum_value = 0
    if len(s) > 0:
        s = s.split("  ")
        for b in s:
            sum_weight += float(b.split(" ")[1])
            sum_value += float(b.split(" ")[2])

        if sum_weight <= c:
            fw = (sum_weight / c)
        else:
            fw = (c / sum_weight)-0.15

        if sum_value <= v:
            fv = (sum_value / v)
            if fv > 0.7:
                fv += 0.15
        else:
            fv = v / sum_value

        return fw + fv
    else:
        return 0


def single_point_crossover(parent1, parent2):
    child1, child2 = [], []

    if (len(parent1) and len(parent2)) > 2:
        parent1 = parent1.split("  ")
        parent2 = parent2.split("  ")

        c_point1 = random.randint(0, len(parent1)-2)
        c_point2 = random.randint(0, len(parent2)-2)

        child1 = parent2[:c_point2] + parent1[c_point1:]
        child1 = remove_duplicates(child1)
        child1 = "  ".join(list(dict.fromkeys(child1)))

        child2 = parent1[:c_point1] + parent2[c_point2:]
        child2 = remove_duplicates(child2)
        child2 = "  ".join(list(dict.fromkeys(child2)))

        return child1, child2
    else:
        return parent1, parent2


def remove_duplicates(seq):
    # removes duplicates while maintaining current order
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def mutation(m, child):
    # Randomly swap values in the solution#
    child = child.split("  ")
    if len(child) > 1:
        for i in range(m):
            pos1 = child.index(random.choice(child))
            pos2 = child.index(random.choice(child))

            child[pos1], child[pos2] = child[pos2], child[pos1]

    return "  ".join(child)


def weakest_replacement(new_s, new_f, fitness_scores, solutions):
    scores = list(chain.from_iterable(fitness_scores))[1::2]

    if len(set(scores)) == 1:
        index = random.randint(0, len(solutions)-1)
        solutions[index] = new_s
        fitness_scores[index][1] = new_f
    else:
        min_fitness = min(scores)
        min_index = []

        for i in range(len(scores)):
            if scores[i] == min_fitness:
                min_index.append(i)

        index = random.choice(min_index)
        solutions[index] = new_s
        fitness_scores[index][1] = new_f

    return solutions, fitness_scores


def is_duplicates(list):
    if len(list) == len(set(list)):
        return False
    else:
        return True


if __name__ == '__main__':

    columns = ['p', 't', 'm', 'seed', "num_bags", "duplicate_bags", "total_weight", "total_value", "fitness"]

    data = []
    count = 0
    while count < 100:
        seed = random.randint(1,100000)
        random.seed(seed)
        population = random.randint(25, 200)
        tournament = random.randint(2, 50)
        mutate = random.randint(1, 50)
        sol = main(seed, tournament, population, mutate)
        if sol not in data:
            print(True)
            data.append(sol)
            count += 1
        else:
            print(False)


    df = pd.DataFrame(data = data, columns = columns)
    df.to_csv('even_bigger_data.csv')


