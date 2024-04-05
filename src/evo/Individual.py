import numpy as np
import numpy.typing as npt


class Individual:
    def __init__(self, encoding: npt.NDArray[np.int64]):
        self.encoding = encoding

    def get_element(self, i: int, j: int) -> int:
        return int(self.encoding[i, j])

    def set_element(self, i: int, j: int, value: int) -> None:
        self.encoding[i, j] = value

    def copy(self) -> 'Individual':
        return Individual(self.encoding.copy())

    def get_shape(self) -> tuple[int, int]:
        rows_count, cols_count = self.get_shape()
        return rows_count, cols_count

    def get_matrix(self) -> npt.NDArray[np.int64]:
        return self.encoding

    def calculate_diversity(self, population: list['Individual']) -> float:
        diversity = 0
        for individual in population:
            diversity += np.linalg.norm(self.encoding - individual.encoding)
        return diversity

    @staticmethod
    def random() -> 'Individual':
        # TODO: Implement domain-specific random Individual generation
        raise NotImplementedError
