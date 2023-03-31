from abc import ABC, abstractmethod

from domain.models.completion_response import CompletionResponse


class ICompletionFacade(ABC):
    """
    Interface for a service that provides a way to generate text completions
    using the OpenAI GPT-3 API.
    """
    @abstractmethod
    def create(self, prompt: str) -> CompletionResponse:
        """
        Generate a text completion using the OpenAI GPT-3 API.

        Parameters:
            prompt (str): The prompt to generate a completion for.

        Returns:
            CompletionResponse: A `TextCompletion` object representing the generated text completion.
        """
        pass
