"""Smoke check: a short GA run on each TSPLIB instance.

For every instance it asserts that the best tour is a valid permutation and
that its reported length is the true length on that instance's own matrix.
Before the fix, bayg29 tours were scored on swiss42 and brazil58 crashed.
"""
import os
import random
import tempfile

from charles.charles import Population
from charles.crossover import cycle_co
from charles.mutation import inversion_mutation
from charles.selection import tournament_selection
from data.tsp_data import bayg29, brazil58, swiss42


def tour_length(tour, matrix):
    return sum(matrix[tour[i - 1]][tour[i]] for i in range(len(tour)))


def main():
    random.seed(0)
    os.chdir(tempfile.mkdtemp())  # Population.log writes a CSV every generation
    for name, matrix in [("swiss42", swiss42), ("bayg29", bayg29), ("brazil58", brazil58)]:
        n = len(matrix)
        pop = Population(size=30, optim="min", elite_size=2, sol_size=n, replacement=False,
                         valid_set=list(range(n)), distance_matrix=matrix)
        best, history = pop.evolve(20, tournament_selection, cycle_co, inversion_mutation,
                                   0.8, 0.2, True, False)
        assert sorted(best.representation) == list(range(n)), name
        assert best.fitness == tour_length(best.representation, matrix), name
        assert history[-1] <= history[0], name
        print(f"{name}: best tour length {best.fitness} after 20 generations")
    print("all checks passed")


if __name__ == "__main__":
    main()
