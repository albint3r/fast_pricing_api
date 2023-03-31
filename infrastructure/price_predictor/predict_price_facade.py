from dataclasses import dataclass
import numpy as np

from domain.price_predictor.i_listings_model import IListingsModel
from domain.price_predictor.i_predict_price_facade import IPredictPriceFacade
from domain.price_predictor.i_trained_models import ITrainedModels


@dataclass
class PredictPriceFacade(IPredictPriceFacade):
    """ Facade that predicts the price of a given listing model using a trained model."""
    trained_model: ITrainedModels
    listing_model: IListingsModel
    predicted_price: np.array = None

    def predict(self) -> dict[str, float]:
        listing_array = self.listing_model.to_array()
        # Load pickle File with the trained ML Model
        self.trained_model.load()
        # Predict Value of the listing request
        self.predicted_price = self.trained_model.predict(listing_array)
        self.listing_model.price = self.predicted_price[0]
        return self.listing_model.to_json()
