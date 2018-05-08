from random import randint


def mutate(population, probability):
    nof_individuals = population.shape[0]
    nof_items = population.shape[1]
    for i in range(nof_individuals):
        for j in range(nof_items):
            decision = randint(1, 1000)
            if decision <= probability:
                population[i, j] = negate(population[i, j])


def negate(boolean_as_int):
    if boolean_as_int == 1:
        return 0
    else:
        if boolean_as_int == 0:
            return 1
    return -1


def cross_over(one, two, nof_bits, probability):
    decision = randint(1, 100)
    if decision <= probability:
        cross_point = randint(1, nof_bits - 1)
        second_part = [i for i in range(cross_point, nof_bits)]
        temp = two[second_part]
        two[second_part] = one[second_part]
        one[second_part] = temp
