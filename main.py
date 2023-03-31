from fastapi import FastAPI, Depends
from injector import Injector


from infrastructure.open_ai.completion_facade_impl import CompletionFacadeImpl
from domain.price_predictor.i_listings_model import IListingsModel
from infrastructure.open_ai.img_facade_impl import ImgFacadeImpl
from infrastructure.price_predictor.predict_price_facade import PredictPriceFacade
from domain.models.apartment import Apartment
from domain.models.house import House
from domain.models.img_response import ImgResponse
from infrastructure.price_predictor.apartment_price_predictor import ApartmentPricePredictor
from infrastructure.price_predictor.house_price_predictor import HousePricePredictor
from injectable import AppModule

app = FastAPI()
injector = Injector(AppModule())


@app.get('/api/v1/house-price-predictor/')
async def get_house_predicted_price(house: IListingsModel = Depends(House)):
    """ Predicts the price of a house based on its features.

    Parameters:
    - house: an instance of a class implementing IListingsModel with the features of the house to predict its price.

    Returns:
    A dictionary with the predicted price and the input features used for the prediction."""
    img_facade: ImgFacadeImpl = injector.get(ImgFacadeImpl)
    img_response: ImgResponse = img_facade.create(
        prompt='A minimalist concrete house with floor-to-ceiling windows and '
               'an open floor plan, surrounded by a lush forest.')
    predict_price_facade: PredictPriceFacade = PredictPriceFacade(listing_model=house,
                                                                  trained_model=HousePricePredictor(),
                                                                  img_response=img_response)

    listing_result: IListingsModel = predict_price_facade.predict()

    return listing_result.to_json()


@app.get('/api/v1/apartment-price-predictor/')
async def get_apartment_predicted_price(apartment: IListingsModel = Depends(Apartment)):
    """ Predicts the price of an apartment based on its features.

    Parameters:
    - apartment: an instance of a class implementing IListingsModel with
     the features of the apartment to predict its price.

    Returns:
    A dictionary with the predicted price and the input features used for the prediction. """
    img_facade: ImgFacadeImpl = injector.get(ImgFacadeImpl)
    img_result: ImgResponse = img_facade.create(prompt='Industrial-style loft apartment with exposed brick walls and '
                                                       'open floor plan')
    predict_price_facade: PredictPriceFacade = PredictPriceFacade(listing_model=apartment,
                                                                  trained_model=ApartmentPricePredictor(),
                                                                  img_response=img_result)
    listing_result: IListingsModel = predict_price_facade.predict()

    return listing_result.to_json()


@app.get('/api/v1/open-ai/completion/{prompt}')
async def get_open_ai_completion(prompt: str):
    """ Obtains the response generated by OpenAI by providing a prompt.

    Parameters:
        prompt (str): The prompt for which a response is desired.

    Returns:
        dict[str, str] | None: A dictionary containing the text generated by OpenAI,
        in the format: {'text': 'text generated by OpenAI'}, or None if a response
        couldn't be obtained from OpenAI. """

    facade = injector.get(CompletionFacadeImpl)
    text_completion = facade.create(prompt=prompt)
    return text_completion.result


@app.get('/api/v1/open-ai/img/{prompt}')
async def get_open_ai_img(prompt: str):
    """ Obtains the response generated by OpenAI by providing a prompt.

    Parameters:
        prompt (str): The prompt for which a response is desired.

    Returns:
        dict[str, str] | None: A dictionary containing the text generated by OpenAI,
        in the format: {'text': 'text generated by OpenAI'}, or None if a response
        couldn't be obtained from OpenAI. """
    facade = injector.get(ImgFacadeImpl)
    img_response: ImgResponse = facade.create(prompt=prompt)
    return img_response.to_json()
