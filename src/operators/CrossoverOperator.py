import random
from typing import Tuple

from config.CrossoverOperatorConfig import CrossoverOperatorConfig
from src.evo.Population import Population
from src.evo.Individual import Individual
from src.evo.IndividualValidator import IndividualValidator


class CrossoverOperator:
    @staticmethod
    def cross(population: Population, op_config: CrossoverOperatorConfig) -> Population:
        result = []
        while len(result) < population.get_size() / op_config.selection_probability:
            if random.uniform(0.0, 1.0) < op_config.crossover_probability:
                while True:
                    individual_a, individual_b = population.get_random_pair()
                    crossed_individual_a, crossed_individual_b = CrossoverOperator.cross_helper(
                        individual_a,
                        individual_b,
                        op_config
                    )
                    if (IndividualValidator.validate(crossed_individual_a)
                            and IndividualValidator.validate(crossed_individual_b)):
                        break
                result.append(crossed_individual_a)
                result.append(crossed_individual_b)
            else:
                individual_a, individual_b = population.get_random_pair()
                result.append(individual_a)
                result.append(individual_b)
        return Population(result)

    @staticmethod
    def cross_helper(
            individual_a: Individual,
            individual_b: Individual,
            op_config: CrossoverOperatorConfig
    ) -> Tuple[Individual, Individual]:
        crossed_individual_a_matrix = individual_a.get_matrix().copy()
        crossed_individual_b_matrix = individual_b.get_matrix().copy()

        if op_config.crossover_operator == CrossoverOperatorConfig.VERTICAL_SPLIT_CROSSOVER_STRATEGY:
            _, cols_count = individual_a.get_shape()
            splitting_gutter_idx = random.randint(0, cols_count)
            crossed_individual_a_matrix[:, splitting_gutter_idx:] = individual_b.get_matrix()[:, splitting_gutter_idx:]
            crossed_individual_b_matrix[:, splitting_gutter_idx:] = individual_a.get_matrix()[:, splitting_gutter_idx:]
        elif op_config.crossover_operator == CrossoverOperatorConfig.HORIZONTAL_SPLIT_CROSSOVER_STRATEGY:
            rows_count, _ = individual_a.get_shape()
            splitting_gutter_idx = random.randint(0, rows_count)
            crossed_individual_a_matrix[splitting_gutter_idx:, :] = individual_b.get_matrix()[splitting_gutter_idx:, :]
            crossed_individual_b_matrix[splitting_gutter_idx:, :] = individual_a.get_matrix()[splitting_gutter_idx:, :]
        else:
            raise NotImplementedError('WIP')

        individual_a.encoding = crossed_individual_a_matrix
        individual_b.encoding = crossed_individual_b_matrix
        return individual_a, individual_b
