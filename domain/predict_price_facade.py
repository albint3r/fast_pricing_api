import numpy as np

from domain.i_listings_model import IListingsModel
from domain.i_trained_models import ITrainedModels
from infrastructure.price_predictor.i_predict_price_facade import IPredictPriceFacade


class PredictPriceFacade(IPredictPriceFacade):
    """ Facade that predicts the price of a given listing model using a trained model."""

    def __init__(self, trained_model: ITrainedModels, listing_model: IListingsModel):
        """ Initializes a new instance of the PredictPriceFacade class.

        Parameters:
            trained_model (ITrainedModels): The trained model to use for prediction.
            listing_model (IListingsModel): The listing model to predict the price for.
        """
        self.price: np.array = None
        self.trained_model: ITrainedModels = trained_model
        self.listing: IListingsModel = listing_model

    def predict(self) -> dict[str, float]:
        """ Predicts the price of the listing model using the trained model.

        Returns:
            dict[str, float]: A dictionary containing the predicted price."""
        listing_array = self.listing.to_array()
        self.trained_model.load()
        self.price = self.trained_model.predict(listing_array)
        return self.price_to_json()

    def price_to_json(self):
        """ Converts the predicted price to a JSON format.

        Returns:
            dict[str, float]: A dictionary containing the predicted price."""
        return {'data': self.price[0]}
