from domain.price_predictor.i_predict_price_facade import IPredictPriceFacade


class PredictPriceFacade(IPredictPriceFacade):
    """ Facade that predicts the price of a given listing model using a trained model."""

    def predict(self) -> dict[str, float]:
        listing_array = self.listing.to_array()
        self.trained_model.load()
        self.predicted_price = self.trained_model.predict(listing_array)
        self.listing.price = self.predicted_price[0]
        return self.listing.to_json()
