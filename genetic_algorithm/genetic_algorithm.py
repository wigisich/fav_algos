import numpy as np

class Genetic:
    def __init__(
            self,
            alphabet: list[int|str],    # The alphabet chromosomes' been coded
            fitness_func,               # A function that evaluates a single chromosome
            population: list,           # List of chromosomes
            parent_ratio: float = .7,   # Probability of selecting a gene from the best parent
            transfer_ratio: float = .2, # Ratio of transfer of the fittest ones to next generation
            mutation_ratio: float = .2, # Mutation probability of a single gene during cross over
            n_generations: int = None,  # Generation number
            ):

        self.alphabet = alphabet
        self.fitness_func = fitness_func
        self.population = population
        self.population_size = len(population)
        self.parent_ratio = parent_ratio
        self.transfer_ratio = transfer_ratio
        self.mutation_ratio = mutation_ratio
        self.n_generations = n_generations

    # After coupling the parents, we choose genes randomly from them with a given mutation ratio to produce offsprings.
    def offspring(self, best_fit, second_best_fit):
        return np.array([
                gene[np.random.choice([0, 1], p=[self.parent_ratio, 1-self.parent_ratio])]
                if self.mutation_ratio <= np.random.rand()
                else np.random.choice(self.alphabet)
                for gene in zip(best_fit, second_best_fit)
               ])

    def sort_fitness(self):
        return sorted(self.population, key=self.fitness_func, reverse=True)

    # This functions selects the best parents and produces the offsprings from them
    def next_generation(self):
        fitness_sorted = self.sort_fitness()
        transfer = np.floor(self.transfer_ratio*self.population_size)
        transfer = int(transfer)

        new_generation = fitness_sorted[:transfer]

        best_fit, second_best_fit = fitness_sorted[:2]

        while len(new_generation) < self.population_size:
            new_generation.append(self.offspring(best_fit, second_best_fit))

        self.population = np.stack(new_generation)

    # This function is for iteratively generating the next generations
    def evolve(self):
        if self.n_generations:
            for _ in range(self.n_generations):
                print(f"{_+1}. Generation's fittest: {self.sort_fitness()[0]}")
                self.next_generation()

        else:
            i = 0
            while True:
                self.next_generation()
                best_fit = self.sort_fitness()[0]
                print(f"{i}.Generation's fittest: {best_fit}")
                i += 1

def sum_fitness(gene):
    return sum(gene)

def hamming_fitness(word):
    return lambda t: sum([ 1 if c==b else 0 for c, b in zip(t, list(word)) ])

