from config.CrossoverOperatorConfig import CrossoverOperatorConfig
from config.MutationOperatorConfig import MutationOperatorConfig
from config.SelectionOperatorConfig import SelectionOperatorConfig


class SingleRunConfig:
    def __init__(
            self,
            mutation_operator_config: MutationOperatorConfig,
            crossover_operator_config: CrossoverOperatorConfig,
            selection_operator_config: SelectionOperatorConfig):
        self.mutation_operator_config = mutation_operator_config
        self.crossover_operator_config = crossover_operator_config
        self.selection_operator_config = selection_operator_config
