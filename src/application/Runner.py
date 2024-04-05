from config.GlobalConfig import GlobalConfig
from config.SingleRunConfig import SingleRunConfig
from src.application.TestConfig import TestConfig
from src.evo.Individual import Individual
from src.evo.Population import Population
from src.operators.FitnessFunction import FitnessFunction


class Runner:
    @staticmethod
    def run() -> tuple[Individual, float]:
        best_individual = None
        best_individual_fit_func_val = -float('inf')
        global_config, single_run_config = Runner.get_config()
        assert global_config.population_size > 0
        assert global_config.populations_count > 1
        current_generation = Runner.generate_random_ancestors(global_config)
        for i in range(global_config.populations_count - 1):
            generation_best_individual, generation_best_individual_fit_func_val \
                = Runner.get_generation_best_individual(current_generation)
            if generation_best_individual_fit_func_val > best_individual_fit_func_val:
                best_individual = generation_best_individual
                best_individual_fit_func_val = generation_best_individual_fit_func_val
            current_generation = current_generation.evolve(global_config, single_run_config)
        return best_individual, best_individual_fit_func_val

    @staticmethod
    def generate_random_ancestors(global_config: GlobalConfig) -> Population:
        ancestors = []
        while len(ancestors) < global_config.population_size:
            ancestors.append(Individual.random())
        return Population(ancestors)

    @staticmethod
    def get_generation_best_individual(current_generation: Population) -> tuple[Individual, float]:
        generation_best_individual = None
        generation_best_individual_fit_func_val = -float('inf')
        fit_func_values = FitnessFunction.compute_fitness_values(current_generation)
        assert len(fit_func_values) == current_generation.get_size()
        for j, fit_func_value in enumerate(fit_func_values):
            if fit_func_value > generation_best_individual_fit_func_val:
                generation_best_individual_fit_func_val = fit_func_value
                generation_best_individual = current_generation.get_list()[j].copy()
        return generation_best_individual, generation_best_individual_fit_func_val

    @staticmethod
    def get_config() -> tuple[GlobalConfig, SingleRunConfig]:
        test_config = TestConfig()
        return test_config.global_config, test_config.single_run_config
