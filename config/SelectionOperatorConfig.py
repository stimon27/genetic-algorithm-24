class SelectionOperatorConfig:
    def __init__(
            self,
            selection_probability: float,
            diversity_multiplier: float,
            best_choice_probability: float,
            fitness_function_max_value: float
    ):
        self.selection_probability = selection_probability
        self.diversity_multiplier = diversity_multiplier
        self.best_choice_probability = best_choice_probability
        self.fitness_function_max_value = fitness_function_max_value
