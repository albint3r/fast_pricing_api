# PredictPrice API
### v1.0.0
This is a simple API for predicting the price of a house or an apartment based on its features.

# Getting Started


To use this API, you will need to send an HTTP GET request to one of the following endpoints:

- /house/: to predict the price of a house
- /apartment/: to predict the price of an apartment

The API expects the input features to be provided as query parameters.

The available parameters are:

- m2_const: the price constant
- rooms: the number of rooms
- baths: the number of bathrooms
- cars: the number of parking spaces
- lat: the latitude of the listing
- long: the longitude of the listing

For example, to predict the price of a 3-bedroom, 2-bathroom house with 2 parking spaces located at (20.455478, -103.488211), you would send the following GET request:
```
GET /house/?m2_const=2500&rooms=3&baths=2&cars=2&lat=20.455478&long=-103.488211
```

# Response Format
The API will return a JSON object with the predicted price and the input features used for the prediction. The response format is as follows:

```
{
  "model_name": "Apartment",
  "additional_information_class": null,
  "price": 30368822.005333334, <------- THIS HIS THE PREDICTED PRICE :)
  "price_const": null,
  "m2_const": 2000,
  "rooms": 3,
  "baths": 23,
  "cars": 23,
  "lat": 20.455478,
  "long": -103.488211
}
```

# Technology Stack
This API was built using FastAPI, a modern web framework for building APIs with Python.
The machine learning models were implemented using scikit-learn, a popular machine learning library for Python. The code was written in Python 3.10.7

# Contributors
Alberto Ortiz:

A multi-disciplinary professional with expertise in 
psychology, marketing, programming, and data science. Alberto played a crucial role in the development of this API,
contributing his skills and knowledge to make it possible. He also led the development of a web version of the project,
which unfortunately didn't come to fruition due to technical difficulties and low participation.
With this lighter and more user-friendly version of the API, Alberto aims to provide users in the Jalisco region of
Mexico with a simple and efficient way to obtain property prices on their mobile devices,
regardless of whether they use Android or iOS.