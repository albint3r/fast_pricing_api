import joblib
import numpy

from domain.i_trained_models import ITrainedModels


class HousePricePredictor(ITrainedModels):

    def load(self):
        self.gridSCV = joblib.load(r'data/pickle_trained_models/rf_casa_venta_15_7_2022')
        self.model = self.gridSCV.best_estimator_

    def predict(self, listing_array: numpy.array):
        return self.model.predict(listing_array)
