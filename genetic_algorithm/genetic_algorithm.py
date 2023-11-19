import numpy as np

class Genetic:
    def __init__(
            self,
            alphabet: list[int|str],
            fitness_func,
            population: list,
            parent_ratio: float = .7, # Probability of selecting a gene from the best parent
            transfer_ratio: float = .2,
            mutation_ratio: float = .2,
            n_generations: int|None = None,
            ):

        self.alphabet = alphabet
        self.fitness_func = fitness_func
        self.population = population
        self.population_size = len(population)
        self.parent_ratio = parent_ratio
        self.transfer_ratio = transfer_ratio
        self.mutation_ratio = mutation_ratio
        self.n_generations = n_generations

    def offspring(self, best_fit, second_best_fit):
        return np.array([
                gene[np.random.choice([0, 1], p=[self.parent_ratio, 1-self.parent_ratio])]
                if self.mutation_ratio <= np.random.rand()
                else np.random.choice(self.alphabet)
                for gene in zip(best_fit, second_best_fit)
               ])

    def sort_fitness(self):
        return sorted(self.population, key=self.fitness_func, reverse=True)

    def next_generation(self):
        fitness_sorted = self.sort_fitness()
        transfer = np.floor(self.transfer_ratio*self.population_size)
        transfer = int(transfer)

        new_generation = fitness_sorted[:transfer]

        best_fit, second_best_fit = fitness_sorted[:2]

        while len(new_generation) < self.population_size:
            new_generation.append(self.offspring(best_fit, second_best_fit))

        self.population = np.stack(new_generation)

    def evolve(self):
        if self.n_generations:
            for _ in range(self.n_generations):
                print(f"{_+1}. Generation's fittest: {self.sort_fitness()[0]}")
                self.next_generation()


def sum_fitness(gene):
    return np.array(gene).sum()

def test(x):
    return sum([ 1 if c==b else 0 for c, b in zip(x, list("batuhan")) ])
