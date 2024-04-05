class CrossoverOperatorConfig:
    VERTICAL_SPLIT_CROSSOVER_STRATEGY = 'vs'
    HORIZONTAL_SPLIT_CROSSOVER_STRATEGY = 'hs'

    def __init__(self, crossover_probability: float, crossover_operator: str, selection_probability: float):
        self.crossover_probability = crossover_probability
        self.crossover_operator = crossover_operator
        self.selection_probability = selection_probability
        # TODO: Add domain-specific config params here
