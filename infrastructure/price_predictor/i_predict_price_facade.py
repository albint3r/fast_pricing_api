from abc import ABC, abstractmethod


class IPredictPriceFacade(ABC):

    @abstractmethod
    def predict(self) -> dict[str, float]:
        pass
