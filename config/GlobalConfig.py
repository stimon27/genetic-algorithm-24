from config.DomainConfig import DomainConfig


class GlobalConfig:
    def __init__(self, domain_config: DomainConfig, populations_count: int, population_size: int):
        self.domain_config = domain_config
        self.populations_count = populations_count
        self.population_size = population_size
