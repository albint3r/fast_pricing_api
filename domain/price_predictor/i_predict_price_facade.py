from abc import ABC, abstractmethod


class IPredictPriceFacade(ABC):

    @abstractmethod
    def predict(self) -> dict[str, float]:
        """Predicts the price for a given listing using the trained model.

        Returns:
            dict[str, float]: A dictionary containing the predicted price and the input features used for prediction.
        """
        pass
