import numpy as np

class Genetic:
    def __init__(
            self,
            population: np.ndarray,
            fitness_func,
            parent_ratio: float, # Probability of selecting a gene from the best parent
            transfer_ratio: float,
            mutation_ratio: float,
            n_generations: int|None = None,
            ):

        self.population = population
        self.population_size = len(population)
        self.n_generations = n_generations
        self.fitness_func = fitness_func
        self.parent_ratio = parent_ratio
        self.transfer_ratio = transfer_ratio
        self.mutation_ratio = mutation_ratio

    def offspring(self, best_fit, second_best_fit, method="cross_over"):
        return np.array([
                gene[np.random.choice([0, 1], p=[self.parent_ratio, 1-self.parent_ratio])]
                if self.mutation_ratio <= np.random.rand()
                else np.random.randint(0,2)
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

# To test it
x = Genetic(population=[np.zeros(20) for _ in range(20)], parent_ratio=.6, fitness_func=sum_fitness, transfer_ratio=.2, mutation_ratio=.2, n_generations=16)
x.evolve()


