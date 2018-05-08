import numpy as np


def count_fitness_fnc_and_weights(items, population):
    nof_items = items.shape[0]
    nof_individuals = population.shape[0]
    if nof_items != population.shape[1]:
        return 0
    result = np.zeros((2, nof_individuals))
    for j in range(nof_individuals):
        result[0, j] = np.sum(items[np.where(np.transpose(population[j, :]) == 1), 2])
        result[1, j] = np.sum(items[np.where(np.transpose(population[j, :]) == 1), 0])
    return result


def fitness_fnc(items, population):
    nof_items = items.shape[0]
    nof_individuals = population.shape[0]
    if nof_items != population.shape[1]:
        return 0
    result = np.zeros(nof_individuals)
    for j in range(nof_individuals):
        result[j] = np.sum(items[np.where(np.transpose(population[j, :]) == 1), 2])
    return result


def chose_winner(final_score, final_weights, max_weight):
    maximum = 0
    it = 0
    index = -1
    for i, j in zip(final_score, final_weights):
        if i > maximum and j <= max_weight:
            maximum = i
            index = it
        it += 1
    return index
