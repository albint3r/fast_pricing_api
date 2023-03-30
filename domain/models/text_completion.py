class TextCompletion:
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
    def __init__(self, *, choices, created, id, model, object, usage):
        self._id = id
        self.choices = choices
        self.created = created
        self.model = model
        self._object = object
        self.usage = usage

    @classmethod
    def from_json(cls, json: dict):
        """
        Creates a new instance of the TextCompletion class from a JSON response returned by the OpenAI API.

        Parameters:
        json (dict): A JSON response returned by the OpenAI API.

        Returns:
        TextCompletion: A new instance of the TextCompletion class.
        """
        text_completion: TextCompletion = cls(**json)
        return text_completion

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
