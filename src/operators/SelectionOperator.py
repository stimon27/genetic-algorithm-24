import math

import numpy as np

from config.GlobalConfig import GlobalConfig
from src.evo.Individual import Individual
from src.evo.Population import Population
from config.SelectionOperatorConfig import SelectionOperatorConfig


class SelectionOperator:
    @staticmethod
    def select(
            population: Population,
            fitness_values: list[float],
            op_config: SelectionOperatorConfig,
            global_config: GlobalConfig
    ) -> Population:
        diversity_values = [individual.calculate_diversity(population.get_list())
                            for _, individual in enumerate(population.get_list())]
        population_data = [(individual, fitness_values[i], diversity_values[i])
                           for i, individual in enumerate(population.get_list())]
        population_scores = SelectionOperator.get_sorted_scores(population_data, op_config, global_config)
        population_probabilities = [(1 - op_config.best_choice_probability) ** i
                                    * op_config.best_choice_probability
                                    ** 1 if i != population.get_size() - 1 else 0
                                    for i in range(population.get_size())]
        assert sum(population_probabilities) == 1
        selected_indices = set()
        while len(selected_indices) < population.get_size() * op_config.selection_probability:
            selected_indices.add(np.random.choice(
                range(population.get_size()),
                p=population_probabilities,
                size=1
            )[0])
        selected_population = [population_scores[i][0] for i in selected_indices]
        return Population(selected_population)

    @staticmethod
    def get_sorted_scores(
            population_data: list[tuple[Individual, float, float]],
            op_config: SelectionOperatorConfig,
            global_config: GlobalConfig
    ) -> list[tuple[Individual, float]]:
        return sorted(
            [(individual_data[0], SelectionOperator.compute_score(
                individual_data[1],
                op_config.fitness_function_max_value,
                individual_data[2],
                np.linalg.norm(
                    global_config.domain_config.encoding_max_values
                    - global_config.domain_config.encoding_min_values)
                * len(population_data),
                op_config.diversity_multiplier)) for _, individual_data in enumerate(population_data)],
            key=lambda x: x[1],
            reverse=True)

    @staticmethod
    def compute_score(x_a: float, x_b: float, y_a: float, y_b: float, y_axis_scaler: float) \
            -> float:
        return math.sqrt((x_a - x_b) ** 2 + ((y_a - y_b) * y_axis_scaler) ** 2)
