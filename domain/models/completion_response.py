from dataclasses import dataclass, field

from domain.models._json_serialize import JsonSerialize


@dataclass
class CompletionResponse(JsonSerialize):
    """
        Represents a response from the OpenAI text completion API.

        Attributes: _id (str): The ID of the completion. choices (List[Dict[str, Any]]): A list of possible
        completions, where each completion is represented as a dictionary. created (int): The timestamp of when the
        completion was created. model (str): The ID of the model used for the completion. _object (str): The type of
        object returned by the API. usage (Dict[str, int]): A dictionary containing information about the API usage.

        Methods:
            from_json(json: Dict[str, Any]) -> TextCompletion:
                Returns a new TextCompletion object constructed from a dictionary.

            result_text() -> str or None:
                Returns the completed text from the API response, or None if no text was provided.

            result() -> Dict[str, str] or None: Returns the completed text from the API response as a dictionary with
            a single 'text' key, or None if no text was provided.
    """
    choices: list[dict[str, any]]
    created: int
    id: str
    model: str
    usage: dict
    object: str

    @property
    def result_text(self) -> str | None:
        """
        Gets the generated text from the first choice.

        Returns:
        str | None: The generated text from the first choice or None if the choices list is empty.
        """
        choices: dict[str] = self._get_choices()
        return choices.get('text')

    @property
    def result(self) -> dict[str] | None:
        """
        Gets the generated text in a dictionary format.

        Returns:
        dict[str, str] | None: A dictionary with a single key-value pair of 'text' and the generated text
        or None if the choices list is empty.
        """
        choices: dict[str] = self._get_choices()
        text: str = choices.get('text')
        if text:
            return {'text': text}

    def _get_choices(self) -> dict[str] | None:
        if self.choices:
            return self.choices[0]
