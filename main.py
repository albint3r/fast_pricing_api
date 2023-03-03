from fastapi import FastAPI, Depends

from domain.i_listings_model import IListingsModel
from domain.predict_price_facade import PredictPriceFacade
from infrastructure.models.apartment import Apartment
from infrastructure.models.house import House
from infrastructure.price_predictor.apartment_price_predictor import ApartmentPricePredictor
from infrastructure.price_predictor.house_price_predictor import HousePricePredictor

app = FastAPI()


@app.get('/house/')
async def get_house_predicted_price(house: IListingsModel = Depends(House)):
    """ Predicts the price of a house based on its features.

    Parameters:
    - house: an instance of a class implementing IListingsModel with the features of the house to predict its price.

    Returns:
    A dictionary with the predicted price and the input features used for the prediction."""
    facade = PredictPriceFacade(listing_model=house, trained_model=HousePricePredictor())
    return facade.predict()


@app.get('/apartment/')
async def get_apartment_predicted_price(apartment: IListingsModel = Depends(Apartment)):
    """ Predicts the price of an apartment based on its features.

    Parameters:
    - apartment: an instance of a class implementing IListingsModel with
     the features of the apartment to predict its price.

    Returns:
    A dictionary with the predicted price and the input features used for the prediction. """
    facade = PredictPriceFacade(listing_model=apartment, trained_model=ApartmentPricePredictor())
    return facade.predict()
