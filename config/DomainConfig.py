import numpy as np


class DomainConfig:
    def __init__(self, encoding_min_values, encoding_max_values):
        self.encoding_min_values = encoding_min_values
        self.encoding_max_values = encoding_max_values
        # TODO: Add domain-specific config params here
