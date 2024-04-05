from random import randint

from config.GlobalConfig import GlobalConfig
from config.SingleRunConfig import SingleRunConfig
from src.evo.Individual import Individual
from src.operators.CrossoverOperator import CrossoverOperator
from src.operators.FitnessFunction import FitnessFunction
from src.operators.MutationOperator import MutationOperator
from src.operators.SelectionOperator import SelectionOperator


class Population:
    def __init__(self, population: list[Individual]):
        self.population = population

    def get_list(self) -> list[Individual]:
        return self.population

    def get_random_pair(self) -> tuple[Individual, Individual]:
        index_a = randint(0, len(self.population) - 1)
        while True:
            index_b = randint(0, len(self.population) - 1)
            if index_a != index_b:
                break
        return self.population[index_a].copy(), self.population[index_b].copy()

    def get_size(self) -> int:
        return len(self.population)

    def evolve(self,
               global_config: GlobalConfig,
               single_run_config: SingleRunConfig
               ) -> 'Population':
        mutated_generation = MutationOperator.mutate(self, single_run_config.mutation_operator_config)
        crossed_generation = CrossoverOperator.cross(
            mutated_generation,
            single_run_config.crossover_operator_config
        )
        fitness_function_values = FitnessFunction.compute_fitness_values(crossed_generation)
        return SelectionOperator.select(
            crossed_generation,
            fitness_function_values,
            single_run_config.selection_operator_config,
            global_config
        )
