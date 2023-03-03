from abc import ABC, abstractmethod
import numpy
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV


class ITrainedModels(ABC):
    """Abstract base class for trained models used for price prediction."""
    gridSCV: GridSearchCV | None = None
    model: RandomForestRegressor | None = None

    @abstractmethod
    def load(self) -> None:
        """Loads a pre-trained model into memory."""
        pass

    @abstractmethod
    def predict(self, listing_array: numpy.array) -> numpy.array:
        """Predicts the price for a given listing using the trained model.

        Parameters:
            listing_array (numpy.array): An array containing the features of the listing.

        Returns:
            numpy.array: An array containing the predicted price."""
        pass
