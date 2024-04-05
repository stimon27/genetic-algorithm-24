import numpy as np

from config.CrossoverOperatorConfig import CrossoverOperatorConfig
from config.DomainConfig import DomainConfig
from config.GlobalConfig import GlobalConfig
from config.MutationOperatorConfig import MutationOperatorConfig
from config.SelectionOperatorConfig import SelectionOperatorConfig
from config.SingleRunConfig import SingleRunConfig


class TestConfig:
    def __init__(self):
        selection_probability = 0.5

        self.global_config = GlobalConfig(
            domain_config=DomainConfig(
                np.zeros([1, 1], dtype=int),
                np.zeros([1, 1], dtype=int)
            ),
            populations_count=123,
            population_size=10000
        )
        self.single_run_config = SingleRunConfig(
            MutationOperatorConfig(mutation_probability=0.1),
            CrossoverOperatorConfig(
                crossover_probability=0.5,
                crossover_operator=CrossoverOperatorConfig.VERTICAL_SPLIT_CROSSOVER_STRATEGY,
                selection_probability=selection_probability
            ),
            SelectionOperatorConfig(
                selection_probability=selection_probability,
                diversity_multiplier=0.2,
                best_choice_probability=0.2,
                fitness_function_max_value=100
            )
        )
