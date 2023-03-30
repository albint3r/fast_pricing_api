import numpy as np
from abc import ABC, abstractmethod

from domain.price_predictor.i_listings_model import IListingsModel
from domain.price_predictor.i_trained_models import ITrainedModels


class IPredictPriceFacade(ABC):
    def __init__(self, trained_model: ITrainedModels, listing_model: IListingsModel):
        """ Initializes a new instance of the PredictPriceFacade class.

        Parameters:
            trained_model (ITrainedModels): The trained model to use for prediction.
            listing_model (IListingsModel): The listing model to predict the price for.
        """
        self.predicted_price: np.array = None
        self.trained_model: ITrainedModels = trained_model
        self.listing: IListingsModel = listing_model

    @abstractmethod
    def predict(self) -> dict[str, float]:
        """Predicts the price for a given listing using the trained model.

        Returns:
            dict[str, float]: A dictionary containing the predicted price and the input features used for prediction.
        """
        pass
