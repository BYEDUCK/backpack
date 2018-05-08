from functions import count_fitness_fnc_and_weights
import numpy as np
from random import randint


def do_selection(items, population, max_value, population_cardinality):
    result = count_fitness_fnc_and_weights(items, population)
    goal_function_values = result[0, :]
    nof_elements = goal_function_values.shape[0]
    ratio = population_cardinality * 2
    goal_function_values = np.round((goal_function_values / np.sum(goal_function_values) *
                                     ratio), 0)
    chosen_ones = [i for i in range(nof_elements)]
    weights = result[1, :]

    for i in range(nof_elements - 1):  # create a pseudo-distribuant
        goal_function_values[i + 1] += goal_function_values[i]

    for j in range(nof_elements):
        decision = randint(1, ratio)
        for n in range(nof_elements):
            if decision <= goal_function_values[n] and weights[n] <= max_value:
                chosen_ones[j] = n
                break

    return chosen_ones
