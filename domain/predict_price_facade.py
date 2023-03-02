import numpy as np

from domain.i_listings_model import IListingsModel
from domain.i_trained_models import ITrainedModels
from infrastructure.price_predictor.i_predict_price_facade import IPredictPriceFacade


class PredictPriceFacade(IPredictPriceFacade):

    def __init__(self, trained_model: ITrainedModels, listing_model: IListingsModel):
        self.price: np.array = None
        self.trained_model: ITrainedModels = trained_model
        self.listing: IListingsModel = listing_model

    def predict(self) -> dict[str, float]:
        listing_array = self.listing.to_array()
        self.trained_model.load()
        self.price = self.trained_model.predict(listing_array)
        return self.price_to_json()

    def price_to_json(self):
        return {'data': self.price[0]}
