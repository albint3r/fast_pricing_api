from abc import ABC, abstractmethod
import numpy
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV


class ITrainedModels(ABC):
    gridSCV: GridSearchCV | None = None
    model: RandomForestRegressor | None = None

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def predict(self, listing_array: numpy.array):
        pass
