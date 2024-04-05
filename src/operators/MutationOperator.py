import random

from config.MutationOperatorConfig import MutationOperatorConfig
from src.evo.Population import Population
from src.evo.Individual import Individual
from src.evo.IndividualValidator import IndividualValidator


class MutationOperator:
    @staticmethod
    def mutate(population: Population, op_config: MutationOperatorConfig) \
            -> Population:
        result = []
        for _, individual in enumerate(population.population):
            individual_copy = individual.copy()
            if random.uniform(0.0, 1.0) <= op_config.mutation_probability:
                while True:
                    mutated_individual = MutationOperator.mutate_helper(individual_copy, op_config)
                    if IndividualValidator.validate(mutated_individual):
                        break
                result.append(mutated_individual)
            else:
                result.append(individual_copy)
        return Population(result)

    @staticmethod
    def mutate_helper(individual: Individual, mutation_config: MutationOperatorConfig) \
            -> Individual:
        raise NotImplementedError('WIP')
