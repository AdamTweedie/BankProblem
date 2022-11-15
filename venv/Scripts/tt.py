

def calculateFitness(s, c, v):

    if len(s) > 0:
        s = s.split("  ")

        solution_total_value = 0
        solution_total_weight = 0

        sum_v_div_w = 0

        for bag in s:
            bag = bag.split(" ")
            solution_total_weight += float(bag[1])
            solution_total_value += float(bag[2])
            sum_v_div_w += float(bag[2]) / float(bag[1])


        return f3
    else:
        return 0

    # def weakest_replacement(new_sol, new_fitness, fitness_scores, population):
    #     solutions = population
    #     f_scores_with_index = fitness_scores
    #     f_scores = []
    #     for score in f_scores_with_index:
    #         f_scores.append(score[1])
    #
    #     min_fitness = min(f_scores)
    #     index = f_scores.index(min_fitness)
    #
    #     if (new_fitness > min_fitness):
    #         f_scores_with_index[index][1] = new_fitness
    #         solutions[index] = new_sol
    #     elif (new_fitness == min_fitness):
    #         b = random.choice(["new", "old"])
    #         if b == "new":
    #             f_scores_with_index[index][1] = new_fitness
    #             solutions[index] = new_sol
    #
    #     return solutions, f_scores_with_index

    # def mutation(m, child):
    #     # Randomly swap values in the solution
    #     child = child.split("  ")
    #     c = int(m)
    #     if len(child) > 1:
    #         while c > 0:
    #             identicle = True
    #             r_bag1 = ""
    #             r_bag2 = ""
    #             while identicle:
    #                 r_bag1 = random.choice(child)
    #                 r_bag2 = random.choice(child)
    #                 if r_bag1 != r_bag2:
    #                     identicle = False
    #             pos1 = child.index(r_bag1)
    #             pos2 = child.index(r_bag2)
    #             child[pos1], child[pos2] = child[pos2], child[pos1]
    #             c = c - 1
    #
    #     return "  ".join(child)





