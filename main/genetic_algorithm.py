import numpy as np
from functions import *
import random as rng
import matplotlib.pyplot as plt
import matplotlib.animation as anm


class GeneticAlgorithm:

    albumNumber = 277125
    numberOfIterations = 0
    populationCardinality = 0
    mutationProbability = 0
    crossingProbability = 0
    numberOfItems = 0
    writeDataToFile = False

    def __init__(self, number_of_iterations, population_cardinality,
                 mutation_probability, crossing_probability, number_of_items, write_data_to_file, app=None):
        self.vars = []
        self.stds = []
        self.avgs = []
        self.mins = []
        self.maxes = []
        self.generations = []
        self.app = app
        self.numberOfIterations = number_of_iterations
        self.populationCardinality = population_cardinality
        self.mutationProbability = mutation_probability
        self.crossingProbability = crossing_probability
        self.numberOfItems = number_of_items
        self.writeDataToFile = write_data_to_file
        w = np.round_(0.1 + 0.9 * np.random.random((self.numberOfItems, 1)), 1)
        p = np.round_(1 + 99 * np.random.random((self.numberOfItems, 1)))
        f = w * p
        self.backpackItems = np.concatenate((w, p, f), axis=1)
        self.maxWeight = 0.3 * np.sum(self.backpackItems[:, 0])
        self.thePopulation = np.random.random_integers(0, 1, size=(self.populationCardinality, self.numberOfItems))
        if self.writeDataToFile:
            self.resultFile = open("result.txt", "w")
            self.resultFile.write("Mutation probability: " + repr(self.mutationProbability / 10) + "%\n" +
                                  "Crossing over probability: " + repr(self.crossingProbability) + "%\n" +
                                  "Number of items: " + repr(self.numberOfItems) + "\n" +
                                  "Population cardinality: " + repr(self.populationCardinality) + "\n" +
                                  "Number of iterations: " + repr(self.numberOfIterations) + "\n\n")

    def start(self):
        animation = anm.FuncAnimation(self.app.figure, self.animate_plot, interval=1000)

        if self.check_if_correct():
            for iteration in range(self.numberOfIterations):
                mutate(self.thePopulation, self.mutationProbability)
                one = rng.randint(0, self.populationCardinality - 1)
                two = rng.randint(0, self.populationCardinality - 1)
                if one != two:
                    cross_over(self.thePopulation[one, :], self.thePopulation[two, :],
                               self.numberOfItems, self.crossingProbability)
                after_selection = do_selection(self.backpackItems, self.thePopulation,
                                               self.maxWeight, self.populationCardinality)
                self.thePopulation = self.thePopulation[after_selection, :]
                fitness = fitness_fnc(self.backpackItems, self.thePopulation)
                temp_var = np.var(fitness)
                temp_std = np.std(fitness)
                temp_avg = np.average(fitness)
                temp_min = np.min(fitness)
                temp_max = np.max(fitness)
                self.app.values_changed(temp_std, temp_var, temp_avg, temp_min, temp_max)
                self.vars.append(temp_var)
                self.stds.append(temp_std)
                self.avgs.append(temp_avg)
                self.mins.append(temp_min)
                self.maxes.append(temp_max)
                self.generations.append(iteration + 1)

                if self.writeDataToFile:
                    self.resultFile.write("Generation [" + repr(iteration + 1) + "]:\n" +
                                          "Variance: " + repr(self.vars[iteration]) +
                                          "\nStandard deviation: " + repr(self.stds[iteration]) +
                                          "\nMax: " + repr(self.maxes[iteration]) +
                                          "\nMin: " + repr(self.mins[iteration]) +
                                          "\nAverage: " + repr(self.avgs[iteration]) + "\n\n")

            final = count_fitness_fnc_and_weights(self.backpackItems, self.thePopulation)
            final_score = final[0, :]
            final_weight = final[1, :]
            the_winner = chose_winner(final_score, final_weight, self.maxWeight)
            print("\n\n")
            print("And the winner is... :\n")
            print(self.thePopulation[the_winner])
            print("\nWith the score of: ")
            print(final_score[the_winner])
            print("\nWith the weight of: ")
            print(final_weight[the_winner])
            print("Where max weight was: " + repr(self.maxWeight) + "\n")

            if self.writeDataToFile:
                self.resultFile.write("\nWinner's result: " + repr(final_score[the_winner]) + "\n")
                self.resultFile.write("Winner's weight: " + repr(final_weight[the_winner]) + "\n")
                self.resultFile.write("Max weight was: " + repr(self.maxWeight) + "\n")
                self.resultFile.close()

            generation = [i for i in range(1, self.numberOfIterations + 1)]
            plt.figure(1)
            plt.plot(generation, self.stds, 'b-', generation, self.avgs, 'y-',
                     generation, self.mins, 'g-', generation, self.maxes, 'r-')
            plt.grid(True)
            plt.xlabel("Generation")
            plt.legend(["Standard deviation", "Average", "Min", "Max"])
            plt.title("Iterations=%d; Populations cardinality=%d; Items=%d\n"
                      "Mutation probability=%.1f%%; Crossing probability=%d%%"
                      % (self.numberOfIterations, self.populationCardinality, self.numberOfItems,
                         self.mutationProbability/10, self.crossingProbability))
            plt.show()
            return final_score[the_winner]
        else:
            print("Data out of bounds or no data!")

    def check_if_correct(self):
        if 0 < self.numberOfIterations < 5000 and 0 < self.populationCardinality < 2000 \
            and 0 < self.numberOfItems < 1000 and 1000 >= self.mutationProbability >= 0 \
                and 0 <= self.crossingProbability <= 100:
            return True
        else:
            return False

    def animate_plot(self, i):
        self.app.graph.clear()
        self.app.graph.plot(self.generations, self.stds, 'b-', self.generations, self.avgs, 'y-',
                            self.generations, self.mins, 'g-', self.generations, self.maxes, 'r-')
